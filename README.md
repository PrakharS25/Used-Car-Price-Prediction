# 🚗 Used Car Price Prediction

A Machine Learning project that predicts the estimated resale price of used cars based on features such as brand, model, car age, kilometers driven, transmission, ownership, and fuel type.

---

## 📌 Project Overview

The used car market contains many factors that influence the resale value of a vehicle. This project uses Machine Learning regression techniques to estimate the price of a used car based on its characteristics.

The project covers the complete Machine Learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation, and deployment using Streamlit.

---

## 🎯 Objective

The main objective of this project is to build a Machine Learning model capable of predicting used car prices based on various vehicle-related features.

The project also includes a Streamlit-based application that provides an interactive interface for entering car details and obtaining an estimated resale price.

---

## 📊 Dataset

The dataset contains information about used cars and includes the following features:

- Brand
- Model
- Age
- Kilometers Driven
- Transmission
- Owner
- Fuel Type
- Ask Price (Target Variable)

---

## 🔄 Project Workflow

The project follows these major steps:

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Feature Selection
7. One-Hot Encoding
8. Feature Scaling
9. Train-Test Split
10. Model Training
11. Model Evaluation
12. Streamlit Deployment

---

## 📈 Exploratory Data Analysis

The project includes multiple visualizations to understand the relationships and patterns present in the dataset.

The visualizations include:

- Scatter Plot
- Regression Plot
- Box Plot
- Correlation Heatmap

---

## 🛠️ Data Preprocessing

The following preprocessing techniques were applied:

- Data cleaning
- Handling categorical features
- Feature selection
- One-Hot Encoding
- Feature scaling

The selected input features include:

```text
Brand
Model
Age
kmDriven
Transmission
Owner
FuelType
```

The target variable is:

```text
AskPrice
```

---

## 🤖 Machine Learning Models

Multiple regression algorithms were considered for the prediction task:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Machine Regressor
- K-Nearest Neighbors Regressor
- Gradient Boosting Regressor

The models were evaluated using regression performance metrics, including the R² Score.

### 🏆 Best Performing Model

**Random Forest Regressor**

**R² Score: 0.81**

---

## 🌐 Streamlit Application

The project also includes a Streamlit application that allows users to enter car details and receive an estimated resale price.

The application accepts:

- Brand
- Model
- Car Age
- Kilometers Driven
- Transmission
- Owner
- Fuel Type

The input data is processed using the saved preprocessing and scaling components before being passed to the trained Machine Learning model.

---

## 📁 Project Structure

```text
Used-Car-Price-Prediction/
│
├── README.md
├── Used_Car_Price_Prediction.ipynb
├── app.py
│
├── preprocessor.pkl
├── scaler.pkl
├── brand_model.pkl
│
└── model.pkl
```

> **Note:** The trained `model.pkl` file is not included in this repository because of its large file size.

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/PrakharS25/Used-Car-Price-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Used-Car-Price-Prediction
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib jupyter
```

### 4. Run the Jupyter Notebook

Open:

```text
Used_Car_Price_Prediction.ipynb
```

and run the cells sequentially.

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

> **Note:** The Streamlit application requires the trained `model.pkl` file to be present in the project directory.

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Advanced feature engineering
- Improved model optimization
- Model explainability
- Deployment using Streamlit Cloud
- Integration with a cloud-based model storage solution
- Development of a more advanced user interface

---

## 👨‍💻 Author

### Prakhar Sharma

GitHub: [PrakharS25](https://github.com/PrakharS25)

---

⭐ If you found this project interesting, consider giving the repository a star!
