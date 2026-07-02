import streamlit as st
import joblib
import os

# Load models
BASE = os.path.dirname(__file__)
tfidf = joblib.load(f"{BASE}/tfidf_vectorizer.pkl")
models = {
    "Naive Bayes": joblib.load(f"{BASE}/nb_model.pkl"),
    "Logistic Regression": joblib.load(f"{BASE}/lr_model.pkl")
}

st.title("Customer Churn Risk Classifier")
st.markdown("Predict churn risk from financial complaint narratives using CFPB data.")
st.info("ℹ️ This model predicts likely company response patterns based on 550K CFPB complaints. Text signal is moderate (~64% accuracy) — a finding that itself reveals company responses depend on internal policy more than complaint content.")
# Sidebar
model_name = st.sidebar.selectbox("Select Model", list(models.keys()))
model = models[model_name]

# Input
narrative = st.text_area("Paste a complaint narrative here:", height=200)

if st.button("Predict"):
    if not narrative.strip():
        st.warning("Please enter a complaint narrative.")
    else:
        vec = tfidf.transform([narrative])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]

        label = "🔴 At Risk" if pred == 1 else "🟢 Retained"
        confidence = prob[pred] * 100

        st.subheader(f"Prediction: {label}")
        st.metric("Confidence", f"{confidence:.1f}%")
        st.progress(int(confidence))
