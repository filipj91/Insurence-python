# -*- coding: utf-8 -*-
"""COST INSURECNE08.12ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aMAAJ6tEjljemubbqMQxK9LInXi4W4Wo
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/COST insurence/insurance.csv')
df.head()
df.shape
df.isnull().sum()
df.describe()
df.info()
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(df['age'])
plt.title('Age Destribution')
plt.show()
plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=df)
plt.title('Sex Distribution')
plt.show()
df['sex'].value_counts()
plt.figure(figsize=(6,6))
sns.distplot(df['bmi'])
plt.title('BMI Distribution')
plt.show()
plt.figure(figsize=(6,6))
sns.countplot(x='children', data=df)
plt.title('Children')
plt.show()
df['children'].value_counts()
plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=df)
plt.title('smoker')
plt.show()
df['smoker'].value_counts()
plt.figure(figsize=(6,6))
sns.countplot(x='region', data=df)
plt.title('region')
plt.show()
df['region'].value_counts()
plt.figure(figsize=(6,6))
sns.distplot(df['charges'])
plt.title('Charges Distribution')
plt.show()
# encoding sex column
df.replace({'sex':{'male':0,'female':1}}, inplace=True)

3 # encoding 'smoker' column
df.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)
X =df.drop(columns='charges', axis=1)
Y = df['charges']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
training_data_prediction =regressor.predict(X_train)
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared vale : ', r2_train)
test_data_prediction =regressor.predict(X_test)
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared vale : ', r2_test)
input_data = (31,1,25.74,0,1,0)

# changing input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost is USD ', prediction[0])

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
import warnings
warnings.filterwarnings("ignore")

# Wczytaj dane
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/COST insurence/insurance.csv')

# Kodowanie zmiennych kategorycznych
df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
df.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)
df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

# Features and target variable
X = df.drop(columns='charges', axis=1)
Y = df['charges']

# Podziel dane na zestaw treningowy i testowy
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Skalowanie danych
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Regresja Liniowa
linear_regressor = LinearRegression()
linear_regressor.fit(X_train_scaled, Y_train)

# Predykcje
training_data_prediction_lr = linear_regressor.predict(X_train_scaled)
r2_train_lr = r2_score(Y_train, training_data_prediction_lr)
print('R squared for training data (Linear Regression): ', r2_train_lr)

test_data_prediction_lr = linear_regressor.predict(X_test_scaled)
r2_test_lr = r2_score(Y_test, test_data_prediction_lr)
print('R squared for test data (Linear Regression): ', r2_test_lr)

# 2. Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train_scaled, Y_train)

# Predykcje
training_data_prediction_rf = rf_regressor.predict(X_train_scaled)
r2_train_rf = r2_score(Y_train, training_data_prediction_rf)
print('R squared for training data (Random Forest): ', r2_train_rf)

test_data_prediction_rf = rf_regressor.predict(X_test_scaled)
r2_test_rf = r2_score(Y_test, test_data_prediction_rf)
print('R squared for test data (Random Forest): ', r2_test_rf)

# 3. GridSearchCV do tuningu hiperparametrów dla Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train_scaled, Y_train)

print("Best parameters for Random Forest:", grid_search.best_params_)

# Model z najlepszymi parametrami
best_rf_regressor = grid_search.best_estimator_

# Predykcje
training_data_prediction_rf_best = best_rf_regressor.predict(X_train_scaled)
r2_train_rf_best = r2_score(Y_train, training_data_prediction_rf_best)
print('R squared for training data (Tuned Random Forest): ', r2_train_rf_best)

test_data_prediction_rf_best = best_rf_regressor.predict(X_test_scaled)
r2_test_rf_best = r2_score(Y_test, test_data_prediction_rf_best)
print('R squared for test data (Tuned Random Forest): ', r2_test_rf_best)

# 4. Predykcja dla nowych danych wejściowych
input_data = (31, 1, 25.74, 0, 1, 0)
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
input_data_scaled = scaler.transform(input_data_as_numpy_array)  # Skalowanie danych wejściowych

# Predykcja dla regresji liniowej
prediction_lr = linear_regressor.predict(input_data_scaled)
print('Predicted insurance cost using Linear Regression: USD', prediction_lr[0])

# Predykcja dla Random Forest
prediction_rf = rf_regressor.predict(input_data_scaled)
print('Predicted insurance cost using Random Forest: USD', prediction_rf[0])

# Predykcja dla najlepszego modelu Random Forest
prediction_rf_best = best_rf_regressor.predict(input_data_scaled)
print('Predicted insurance cost using Tuned Random Forest: USD', prediction_rf_best[0])