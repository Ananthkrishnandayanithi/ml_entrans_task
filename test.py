import unittest
from app import app, db, HousingData
import os
import json

data_dir = 'static/'

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client and database
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_housing_data.db'
        self.client = app.test_client()
        self.db = db

        # Create tables
        with app.app_context():
            self.db.create_all()

    def tearDown(self):
        # Drop all tables after the tests
        with app.app_context():
            self.db.session.remove()
            self.db.drop_all()

        # Remove test database file
        if os.path.exists('test_housing_data.db'):
            os.remove('test_housing_data.db')

    def test_home_page(self):
        # Test home page rendering
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'prediction', response.data)

    def test_prediction(self):
        # Test prediction endpoint with mock data
        test_data = {
            'longitude': '-121.89',
            'latitude': '37.29',
            'housing_median_age': '20',
            'total_rooms': '880',
            'total_bedrooms': '129',
            'population': '322',
            'households': '126',
            'median_income': '8.3252',
            'bedroom_ratio': '0.1466',
            'household_rooms': '6.9841',
            '<1H OCEAN': '1',
            'INLAND': '0',
            'ISLAND': '0',
            'NEAR BAY': '0',
            'NEAR OCEAN': '0',
        }
        response = self.client.post('/predict', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction', response.data)

    def test_missing_prediction_field(self):
        # Test missing field in prediction
        test_data = {
            'longitude': '-121.89',
            'latitude': '37.29',
            'housing_median_age': '20',
            'total_rooms': '880',
            # Missing total_bedrooms
        }
        response = self.client.post('/predict', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing feature', response.data)

    def test_analysis_page(self):
        # Test analysis page rendering
        response = self.client.get('/analysis')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'descriptive', response.data)

    def test_visualization_page(self):
        # Test visualization page rendering
        response = self.client.get('/visualization')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists(data_dir + 'visualization1.png'))
        self.assertTrue(os.path.exists(data_dir + 'visualization2.png'))
        self.assertTrue(os.path.exists(data_dir + 'visualization3.png'))
        self.assertTrue(os.path.exists(data_dir + 'visualization4.png'))

if __name__ == '__main__':
    unittest.main()
