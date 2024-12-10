from extensions import db
import pandas as pd

# Define the data model
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

# Function to seed the database
def seed_database():
    df = pd.read_csv('Intern Housing Data India.csv')
    df['bedroom_ratio'] = df['total_bedrooms'] / df['total_rooms']
    df['household_rooms'] = df['total_rooms'] / df['households']
    for _, row in df.iterrows():
        record = HousingData(
            longitude=row['longitude'],
            latitude=row['latitude'],
            housing_median_age=row['housing_median_age'],
            total_rooms=row['total_rooms'],
            total_bedrooms=row['total_bedrooms'],
            population=row['population'],
            households=row['households'],
            median_income=row['median_income'],
            median_house_value=row['median_house_value'],
            bedroom_ratio=row['bedroom_ratio'],
            household_rooms=row['household_rooms'],
            ocean_proximity=row['ocean_proximity']
        )
        db.session.add(record)
    db.session.commit()
