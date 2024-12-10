from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///housing_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the data model for the database
class HousingData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    housing_median_age = db.Column(db.Float)
    total_rooms = db.Column(db.Float)
    total_bedrooms = db.Column(db.Float)
    population = db.Column(db.Float)
    households = db.Column(db.Float)
    median_income = db.Column(db.Float)
    median_house_value = db.Column(db.Float)
    bedroom_ratio = db.Column(db.Float)
    household_rooms = db.Column(db.Float)
    ocean_proximity = db.Column(db.String)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    """Render the home page with the prediction form."""
    return render_template('prediction.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle the prediction logic."""
    try:
        data = request.form
        features = {
            'longitude': float(data['longitude']),
            'latitude': float(data['latitude']),
            'housing_median_age': float(data['housing_median_age']),
            'total_rooms': float(data['total_rooms']),
            'total_bedrooms': float(data['total_bedrooms']),
            'population': float(data['population']),
            'households': float(data['households']),
            'median_income': float(data['median_income']),
            'bedroom_ratio': float(data['bedroom_ratio']),
            'household_rooms': float(data['household_rooms']),
            '<1H OCEAN': int(data['<1H OCEAN']),
            'INLAND': int(data['INLAND']),
            'ISLAND': int(data['ISLAND']),
            'NEAR BAY': int(data['NEAR BAY']),
            'NEAR OCEAN': int(data['NEAR OCEAN']),
        }
        input_data = pd.DataFrame([features])
        prediction = model.predict(input_data)[0]
        return render_template('prediction.html', prediction=round(prediction, 2))
    except KeyError as e:
        return f"Missing feature: {str(e)}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/analysis')
@app.route('/analysis')
def analysis():
    """Render descriptive analysis of the dataset."""
    # Load dataset
    data = pd.read_csv('Intern Housing Data India.csv')

    # Perform descriptive analysis
    description = data.describe().to_html(classes='table table-striped table-bordered')

    # Render analysis page
    return render_template('analysis.html', description=description)
@app.route('/visualization')
def save_visualizations():
    df = pd.read_csv('Intern Housing Data India.csv')

    # Add the necessary columns to the dataframe
    df['bedroom_ratio'] = df['total_bedrooms'] / df['total_rooms']
    df['household_rooms'] = df['total_rooms'] / df['households']
    new_train = df.join(pd.get_dummies(df.ocean_proximity)).drop(['ocean_proximity'], axis=1)
    columns = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
    for col in columns:
        new_train[col] = new_train[col].astype(int)

    # Plot 1: Latitude vs Longitude with Hue (Median House Value)
    plt.figure(figsize=(15, 8))
    sns.scatterplot(x="latitude", y="longitude", data=df, hue="median_house_value", palette="viridis")
    plt.xlabel("Latitude", fontsize=14)
    plt.ylabel("Longitude", fontsize=14)
    plt.legend(title="Median House Value", loc="upper right")
    plt.savefig('static/visualization1.png')
    plt.close()

    # Plot 2: Bedroom Ratio vs Median House Value
    plt.figure(figsize=(15, 8))
    sns.scatterplot(x="bedroom_ratio", y="median_house_value", data=df, hue="median_house_value", palette="viridis")
    plt.xlabel("Bedroom Ratio", fontsize=14)
    plt.ylabel("Median House Value", fontsize=14)
    plt.savefig('static/visualization2.png')
    plt.close()

    # Plot 3: Household Rooms vs Median House Value
    plt.figure(figsize=(15, 8))
    sns.scatterplot(x="household_rooms", y="median_house_value", data=df, hue="median_house_value", palette="viridis")
    plt.xlabel("Household Rooms vs Price", fontsize=14)
    plt.ylabel("Median House Value", fontsize=14)
    plt.savefig('static/visualization3.png')
    plt.close()

    # Plot 4: Heatmap of Correlation Matrix
    plt.figure(figsize=(15, 8))
    sns.heatmap(new_train.corr(), annot=True, cmap='coolwarm')
    plt.savefig('static/visualization4.png')
    plt.close()
    return render_template('visualization.html')
if __name__ == '__main__':
    app.run(debug=True)
