# ML Entrans Task: Housing Price Prediction

## Project Overview
The `ml_entrans_task` project is a machine learning application designed to predict housing prices based on various input features. The project utilizes a dataset of housing data in India and provides functionalities such as predictions, data analysis, and visualizations through a Flask-based web application.

## Directory Structure
```
ml_entrans_task/
├── House_predict.ipynb        # Jupyter Notebook for housing price model development
├── Intern Housing Data India.csv # Dataset used for model training
├── README.md                  # Project documentation
├── __pycache__/               # Compiled Python files
│   ├── app.cpython-311.pyc
│   ├── extensions.cpython-311.pyc
│   └── models.cpython-311.pyc
├── app.py                     # Main Flask application
├── extensions.py              # Additional modules for Flask extensions
├── instance/
│   └── housing_data.db        # SQLite database for storing processed data
├── models.py                  # Data models and database schema
├── static/
│   ├── css/                   # Stylesheets for the web application
│   ├── visualization1.png     # Data visualization image 1
│   ├── visualization2.png     # Data visualization image 2
│   ├── visualization3.png     # Data visualization image 3
│   └── visualization4.png     # Data visualization image 4
└── templates/
    ├── analysis.html          # Webpage for data analysis
    ├── base.html              # Base template for the web application
    ├── prediction.html        # Webpage for housing price prediction
    └── visualization.html     # Webpage for data visualizations
```

## Features
1. **Prediction:** Predict median house prices based on user-provided input features.
2. **Visualization:** Display various data insights using pre-generated visualizations.
3. **Analysis:** Provide an analysis of the housing dataset.
4. **Database Integration:** Store processed data in a SQLite database.

## Requirements

### Dependencies
Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Key packages include:
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

### Files and Database
- `Intern Housing Data India.csv`: Dataset used for training and analysis.
- `housing_data.db`: SQLite database containing preprocessed data.

## Usage

### Running the Flask Application
1. Navigate to the project directory:
    ```bash
    cd ml_entrans_task
    ```
2. Run the Flask application:
    ```bash
    python app.py
    ```
3. Access the application in your browser at `http://127.0.0.1:5000/`.

### Project Workflow
- **Data Preparation:** Jupyter Notebook (`House_predict.ipynb`) is used to clean and preprocess data, as well as to train the predictive model.
- **Web Interface:** Flask provides a user-friendly interface for predictions, visualizations, and data analysis.
- **Database:** The processed data is stored in `housing_data.db` for efficient querying and storage.

## Web Application Pages
1. **Home:** Welcome page with project introduction.
2. **Prediction:** Input form for predicting housing prices based on input features.
![Screenshot 2024-12-10 204104](https://github.com/user-attachments/assets/23d44c4f-25de-458a-a9ea-8617f765bc01)
3. **Analysis:** Data analysis insights from the dataset.
![Screenshot 2024-12-10 204049](https://github.com/user-attachments/assets/c248e094-0ec7-4d88-8bda-e56a005f7e74)
4. **Visualization:** Display of pre-generated visualizations for better understanding of the data.
![Screenshot 2024-12-10 204035](https://github.com/user-attachments/assets/e68fb458-09a5-4ba2-85b0-383519686575)
## Visualizations
The `static/` directory contains visualizations illustrating key insights from the housing dataset. These are rendered on the `visualization.html` page.

### Visualizations Included:
- **visualization1.png:** Overview of price distribution.
- **visualization2.png:** Correlation between median income and house value.
- **visualization3.png:** Age of houses vs. price trends.
- **visualization4.png:** Geographic distribution of housing prices.
## Acknowledgments
- Dataset: `Intern Housing Data India.csv`
- Libraries: Flask, Pandas, NumPy, Scikit-learn, Matplotlib
