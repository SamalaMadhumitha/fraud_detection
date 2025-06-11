# 💳 Credit Card Fraud Detection Web App

This is an AI project that detects fraudulent credit card transactions using a trained machine learning model. It features a web-based interface using **Streamlit**, where users can upload transaction data and get instant predictions of which transactions are ❌ Fraud and which are ✅ Safe.

##  Project Structure
fraud_detection_app/
├── dataset/
│ └── creditcard.csv # Dataset file used to train the model
├── train_model.py # Python script to train the machine learning model
├── model.pkl # Saved trained model after training
├── app.py # Streamlit web application
├── requirements.txt # Required Python libraries
└── README.md # Project documentation 
##  Project Objective

The aim is to build an intelligent system that:
- ✅ Detects safe transactions
- ❌ Flags fraudulent transactions  
based on transaction features like `Time`, `Amount`, `V1` to `V28` etc.
##  Technologies & Tools Used

- Python 3.x  
- Pandas  
- scikit-learn  
- Streamlit  
- Joblib  
- Jinja2  
- Dataset: Real-world credit card fraud dataset from Kaggle
##  Setup and Execution

### Step 1: Install Required Libraries

Before starting, open terminal
pip install -r requirements.txt 
### Step 2: Train the Machine Learning Model
Run the training script to generate model.pkl:

python train_model.py
Step 3: Launch the Streamlit Web App
Run the following command:
streamlit run app.py
### It will open the app in your browser at http://localhost:8501.

### How to Use the App
Click “Browse files” to upload your .csv file (similar to creditcard.csv).

Click “🔍 Detect Fraud”.

The app will show each transaction as either:

✅ Safe (green)

❌ Fraud (red)

You can scroll and explore predictions in a styled table.

### Model Details
Algorithm: Random Forest Classifier

Library: scikit-learn

Data: Kaggle creditcard.csv with 284,807 transactions

Model Output:

0 → Safe

1 → Fraud

The model learns patterns and anomalies in transaction behavior.

 ### This project is useful for:
  Real-time fraud detection in banking systems.
