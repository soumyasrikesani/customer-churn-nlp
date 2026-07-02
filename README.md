# Customer Churn Risk Prediction from Financial Support Tickets

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sri-churn-classifier.streamlit.app)

An end-to-end NLP pipeline that predicts churn risk from consumer complaint narratives using real federal data from the Consumer Financial Protection Bureau (CFPB).

## Project Overview

This project explores whether the text of a customer complaint can predict how a company will respond to it — a proxy for customer churn risk. It uses ~550,000 real consumer complaints filed with the CFPB against major U.S. financial institutions.

## 🚀 Live Demo

Try the deployed app: **https://sri-churn-classifier.streamlit.app**

**Business Question:** Can we identify at-risk customers from their complaint language alone, so companies can proactively intervene before they churn?

## Architecture

CFPB Public Data (CSV, ~767MB) → Snowflake Data Warehouse → Python (pandas + scikit-learn) → Streamlit Dashboard

## Tech Stack

- **Data Warehouse:** Snowflake
- **Language:** Python 3.13
- **ML:** scikit-learn (TF-IDF, Logistic Regression, Naive Bayes)
- **App:** Streamlit
- **Version Control:** Git + GitHub

## Data

- **Source:** CFPB Consumer Complaints Database (consumerfinance.gov)
- **Size:** ~550,000 complaints with narrative text
- **Products covered:** Credit reporting, Debt collection, Checking/savings accounts

## Label Design

Churn risk is defined by company response type:
- **At Risk** — Company closed with explanation OR gave untimely response
- **Retained** — Company provided monetary or non-monetary relief

Class distribution: 63.8% At Risk, 36.2% Retained

## Model Results

| Model | Accuracy | At Risk Recall | At Risk Precision |
|---|---|---|---|
| Logistic Regression | 64% | 60% | 78% |
| Naive Bayes | 64% | 79% | 69% |

**Naive Bayes was selected** for higher recall on the At Risk class — in a churn context, catching at-risk customers matters more than avoiding false alarms.

## Key Finding

The complaint text alone is a moderate but not strong predictor of company response. This suggests companies respond to complaints based on internal policies and complaint categories more than on the specific language customers use. This is a business insight in itself — text-based early warning has limits, and richer signals like product type, company history, and customer tenure would be needed for stronger prediction.

## Project Structure

- `sql/` — Snowflake table & view definitions
- `src/` — Data loading and connection scripts
- `notebooks/` — EDA and modeling notebook
- `app/` — Streamlit dashboard + saved models
- `data/` — Local data (gitignored)

## How to Run Locally

1. Clone the repo and cd into it
2. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in Snowflake credentials
5. Run the app: `streamlit run app/streamlit_app.py`

## Author

Built by Soumya Sri Kesani as a portfolio project targeting Analytics Engineer and Data Analyst roles.
