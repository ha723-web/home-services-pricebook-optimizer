# ai_models.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_models():
    df = pd.read_csv('data/home_services_data.csv')

    # PRICE PREDICTOR
    X_price = df[['Labor Cost', 'Material Cost']]
    y_price = df['Price']
    model_price = RandomForestRegressor()
    model_price.fit(X_price, y_price)
    joblib.dump(model_price, 'models/price_predictor.pkl')

    # CATEGORY CLASSIFIER
    le = LabelEncoder()
    df['Category_encoded'] = le.fit_transform(df['Category'])
    X_cat = df[['Labor Cost', 'Material Cost']]
    y_cat = df['Category_encoded']
    model_cat = LogisticRegression(max_iter=1000)
    model_cat.fit(X_cat, y_cat)
    joblib.dump(model_cat, 'models/category_classifier.pkl')
    joblib.dump(le, 'models/category_label_encoder.pkl')

    print("✅ Models trained and saved successfully.")

def predict_price(labor_cost, material_cost):
    model = joblib.load('models/price_predictor.pkl')
    return round(model.predict([[labor_cost, material_cost]])[0], 2)

def predict_category(labor_cost, material_cost):
    model = joblib.load('models/category_classifier.pkl')
    le = joblib.load('models/category_label_encoder.pkl')
    pred = model.predict([[labor_cost, material_cost]])[0]
    return le.inverse_transform([pred])[0]
