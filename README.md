# Predicting Individual Happiness from the World Values Survey

This repository contains the code and configuration for a Codabench machine learning challenge based on the World Values Survey (WVS).

The objective of the challenge is to predict the self-reported happiness score of individuals using large-scale cross-national survey data.

---

## 🌍 Dataset

The data is derived from:

World Values Survey (WVS) Time-Series Dataset (1981–2022)  
Version V3.0  

Official source:  
https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp

The WVS dataset combines seven waves of surveys conducted between 1981 and 2022 across multiple countries.

Important characteristics:

- Repeated cross-sectional dataset (not panel data)
- Each row represents a different individual
- Nationally representative samples per wave
- Special missing codes (-1, -2, -4, -5) must be handled carefully

⚠️ The original dataset cannot be redistributed.  
Please download it directly from the official WVS website.

---

## 🎯 Task

The goal is to predict the individual's happiness score (ordinal variable) using:

- Demographic variables  
- Socioeconomic indicators  
- Cultural and political attitudes  
- Value-based survey responses  

This challenge is primarily a **feature engineering task**, as most raw columns are intentionally kept to allow creative preprocessing and representation learning.

---