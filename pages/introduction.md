# Predicting Individual Happiness from the World Values Survey
Link for the starting kit : https://github.com/Maltouf25/WVS-Happiness-Prediction-Challenge/blob/main/Starting_kit.ipynb
## Overview

This challenge focuses on predicting the **self-reported happiness score** of individuals using data from the World Values Survey (WVS).

The dataset used in this competition comes from:

World Values Survey Time-Series Dataset (1981–2022)  
Version V3.0  
Official website:  
https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp

The dataset combines seven waves of surveys conducted between 1981 and 2022 across many countries worldwide.

---

## Nature of the Dataset

The WVS time-series dataset is:

- A **repeated cross-sectional survey**
- Not a panel dataset
- Each wave surveys nationally representative adult samples
- Respondent IDs do NOT refer to the same individuals across waves

This means:
- Each row represents a different individual
- There is no longitudinal tracking of the same person over time
- The data reflects societal values at different historical periods

---

## The Challenge

The objective is to predict an individual's **happiness score** based on:

- Demographic variables
- Socioeconomic indicators
- Cultural and value-based survey responses
- Political and social attitudes

---

## A Feature Engineering Challenge

This competition is intentionally designed to be **primarily a feature engineering task**.

We deliberately kept the majority of the available variables to allow participants to:

- Design meaningful derived features
- Handle missing-value codes (-1, -2, -4, -5, etc.)
- Discover latent structures and correlations
- Encode ordinal and categorical variables appropriately
- Perform cross-feature interactions
- Explore country-level and wave-level aggregations

The predictive performance will depend less on model complexity and more on:

- Smart preprocessing
- Careful handling of survey-specific missing codes
- Extraction of hidden structure in high-dimensional survey data

---

## Why This Is Interesting

Happiness prediction from social survey data is:

- A socially relevant problem
- A high-dimensional structured-data task
- A real-world example of noisy human-reported outcomes
- A strong benchmark for tabular ML and feature engineering methods

This challenge bridges:
- Social science
- Machine learning
- Interpretability
- Real-world structured data modeling
