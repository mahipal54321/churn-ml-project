import pandas as pd

# Load data
df = pd.read_csv("data/churn.csv")

# Cleaning
df['TotalCharges'] = df['TotalCharges'].replace(" ", 0)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
df.fillna(0, inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Drop ID
df.drop('customerID', axis=1, inplace=True)

# Encoding
df = pd.get_dummies(df, drop_first=True)

# 👉 NOW create X and y
X = df.drop('Churn', axis=1)
y = df['Churn']

# 👉 DEBUG (put here, AFTER X is defined)
print("\nObject columns in X:")
print(X.select_dtypes(include=['object']).columns)

# Force numeric (fix)
X = X.apply(pd.to_numeric)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

import joblib

joblib.dump(model, "model.pkl")

print("\nModel saved successfully!")

import joblib

# Save model
joblib.dump(model, "model.pkl")

# ✅ Save feature columns (THIS IS THE MISSING PART)
joblib.dump(X.columns.tolist(), "columns.pkl")

print("Model and columns saved!")