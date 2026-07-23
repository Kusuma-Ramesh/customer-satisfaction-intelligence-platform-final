# Customer Satisfaction Intelligence & Analytics Platform

An end-to-end Machine Learning and Analytics platform developed to predict customer satisfaction levels and provide actionable business insights using customer support interaction data.

The platform combines Machine Learning, Business Analytics, Data Visualization, and Interactive Dashboards to help organizations understand customer experience and improve service quality.


---

## Project Overview

The system performs:

- Customer Satisfaction Prediction
- Confidence Score Generation
- Risk Level Assessment
- Business Recommendations
- Customer Satisfaction Analytics
- Category-wise Performance Analysis
- Product-wise Performance Analysis
- Manager Performance Analysis
- Customer Satisfaction Trend Analysis
- Model Performance Visualization


---

## Features

### Prediction Center

The Prediction Center allows users to:

- Predict Customer Satisfaction Levels
- Generate Confidence Scores
- Identify Customer Risk Levels
- Download Prediction Reports
- View Business Interpretations
- Obtain Actionable Recommendations

Predicted satisfaction levels include:

- Highly Unsatisfied
- Unsatisfied
- Neutral
- Satisfied
- Highly Satisfied


---

### Analytics Center

The Analytics dashboard provides:

- CSAT Score Distribution Analysis
- Feature Importance Visualization
- Category Performance Analysis
- Product Category Analysis
- Customer Satisfaction Trends
- Manager Performance Analysis
- Business Summary Reports


---

### Business Insights

Provides business-focused insights including:

- Customer Experience Metrics
- Satisfaction Trends
- Service Performance Analysis
- Strategic Recommendations
- Operational Analytics


---

### Developer Hub

Provides:

- Technical Architecture Overview
- Dataset Information
- Feature Engineering Pipeline
- Model Information
- Deployment Details


---

### Model Center

Provides information regarding:

- Machine Learning Pipeline
- Random Forest Classifier
- Feature Engineering
- Cross Validation Results
- Model Performance Metrics
- Deployment Readiness


---

## Machine Learning Model

| Component | Details |
|----------|----------|
| Model | Random Forest Classifier |
| Classification Type | Multi-Class Classification |
| Target Classes | 5 |
| Validation Technique | Cross Validation |
| Class Balancing | SMOTE |
| Serialization | Joblib |
| Deployment | Streamlit |


---

## Technologies Used

### Frontend

- Streamlit

### Machine Learning

- Scikit-Learn
- Random Forest Classifier
- SMOTE

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

### Model Serialization

- Joblib

### Development Environment

- Python
- VS Code


---

## Project Structure

```
customer_satisfaction_platform

│ Home.py
│ README.md
│ requirements.txt
│ .gitignore
│
├── config
│      mappings.py
│
├── data
│      Customer_support_data.csv
│
├── deployment
│
├── engines
│      prediction_engine.py
│
├── models
│      categorical_columns.pkl
│      customer_satisfaction_model.pkl
│      feature_columns.pkl
│      ordinal_encoder.pkl
│
├── notebooks
│      Customer_Satisfaction.ipynb
│      PRODUCT REQUIREMENT DOCUMENT.docx
│
└── pages
       Analytics.py
       Business_Insights.py
       Developer_Hub.py
       Model_Center.py
       Prediction.py
```

---

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Move to the project directory:

```bash
cd customer_satisfaction_platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run Home.py
```


---

## Dataset Information

The dataset contains customer support interaction records including:

- Channel Name
- Category
- Sub Category
- Customer City
- Product Category
- Item Price
- Connected Handling Time
- Agent Information
- Customer Satisfaction Scores


---

## Output Generated

The platform generates:

- Satisfaction Prediction
- Confidence Scores
- Risk Levels
- Business Recommendations
- Analytics Reports
- Downloadable Prediction Reports


---

## Future Scope

- Real-time Customer Satisfaction Monitoring
- API Integration
- Cloud Deployment
- Advanced Business Intelligence Dashboards
- Automated Customer Retention Strategies
- Explainable AI Integration


---

## Developed Using

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
- Joblib


---

NOTE

The trained Random Forest model used for prediction exceeds GitHub's
100 MB file-size limitation.

The complete project runs successfully with the trained model file placed
inside the models folder.

For demonstration and evaluation purposes, the project has been tested
locally and all functionalities are working correctly.

## License

This project has been developed for educational and academic purposes.
