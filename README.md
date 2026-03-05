# WVS Happiness Prediction Challenge

This repository contains the code and resources for the **WVS Happiness Prediction Challenge**, a machine learning competition hosted on Codabench.

Competition link:  
https://www.codabench.org/competitions/14351

## Overview

The goal of this challenge is to predict the **self-reported happiness score of individuals** using data from the **World Values Survey (WVS)**.

Participants build machine learning models that use demographic, social, and cultural survey responses to estimate the happiness level of each respondent.

## Dataset

The data comes from the **World Values Survey (WVS) Time-Series Dataset (1981–2022), Version V3.0**.

Official source:  
https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp

Key characteristics of the dataset:

- International survey covering multiple countries and waves
- Each row represents one individual respondent
- Contains demographic, socioeconomic, and value-based survey variables
- Includes special missing codes such as `-1`, `-2`, `-4`, and `-5`

⚠️ The original dataset cannot be redistributed.  
Please download it from the official WVS website.

## Task

Participants must train a model to predict the **happiness score (A008)** of individuals.

The competition focuses mainly on **feature engineering and preprocessing** of high-dimensional survey data.

## Evaluation

Submissions are evaluated using:

- **Quadratic Weighted Kappa (QWK)** — primary ranking metric  
- **Mean Absolute Error (MAE)** — complementary metric

The public leaderboard is computed on a public test set, while the final ranking uses a hidden private test set.

## Repository Contents

- `ingestion_program/` — ingestion pipeline used by Codabench  
- `scoring_program/` — evaluation code  
- `Starting_kit.ipynb` — starter notebook for participants  
- `competition.yaml` — competition configuration