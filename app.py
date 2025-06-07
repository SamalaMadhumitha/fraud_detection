import streamlit as st
import pandas as pd
import joblib

# Allow large styling
pd.set_option("styler.render.max_elements", 600000)

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")

# Load trained model
model = joblib.load("model.pkl")

st.title("💳 Credit Card Fraud Detection Web App")
st.markdown("Upload your CSV transaction file and detect which ones are **fraudulent**.")

uploaded_file = st.file_uploader("📤 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("📊 Preview of Uploaded Data:")
    st.dataframe(data.head())

    if st.button("🔍 Detect Fraud"):
        try:
            # Drop 'Class' column if present
            if "Class" in data.columns:
                data = data.drop("Class", axis=1)

            # Predict
            predictions = model.predict(data)

            # Create result DataFrame
            result = pd.DataFrame({
                "Transaction": range(1, len(predictions) + 1),
                "Prediction": ["❌ Fraud" if p == 1 else "✅ Safe" for p in predictions]
            })

            # Count
            total = len(predictions)
            frauds = sum(predictions)
            safes = total - frauds

            # Show summary
            st.write("📋 Prediction Summary:")
            st.markdown(f"- ✅ Safe Transactions: **{safes}**")
            st.markdown(f"- ❌ Fraudulent Transactions: **{frauds}**")

            # Color function
            def highlight_fraud(val):
                color = 'red' if val == '❌ Fraud' else 'green'
                return f'color: {color}'

            # Show all rows (with color)
            st.write("🔎 Full Prediction Results (first 500 shown):")
            st.dataframe(result.head(500).style.applymap(highlight_fraud, subset=["Prediction"]))

            # Download option
            csv = result.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download All Results as CSV", csv, "fraud_predictions.csv", "text/csv")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")