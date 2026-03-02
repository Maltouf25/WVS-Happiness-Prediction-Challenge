# Data Description

## Source

World Values Survey (WVS) Time-Series Dataset (1981–2022)  
Version V3.0  
Official link:  
https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp

The data is used for non-commercial academic purposes only. Redistribution of the original dataset is prohibited.

---

## What Each Row Represents

Each row corresponds to:

> One individual respondent from a nationally representative survey sample conducted during one WVS wave in a specific country.

There is no continuity between waves. Respondent IDs across waves represent different individuals.

---

## What Each Column Represents

Columns include:

- Demographic variables (age, gender, education, etc.)
- Socioeconomic indicators
- Political opinions
- Cultural beliefs
- Religious attitudes
- Social trust measures
- Value-based responses

Many variables are ordinal survey responses.

Some variables use special missing codes such as:
- -1
- -2
- -4 (Not asked)
- -5

Proper handling of these codes is crucial for good performance.

---

## Target Variable

The target is the individual's:

> Self-reported happiness score

This is an ordinal variable representing increasing levels of happiness.

The task is to predict this score.

---

## Dataset Splits

The dataset is split into:

- `train.csv`
- `test_public.csv`
- `test_private.csv`

The labels are provided for:
- `train.csv`
- `test_public_labels.csv` (used for leaderboard evaluation)

The `test_private` labels are hidden and used for final ranking.

---

## Splitting Strategy

We used a **stratified split based on the happiness score** to ensure:

- Balanced representation of happiness levels
- Fair distribution across training and test sets
- Stable evaluation across classes

This preserves the ordinal distribution of the target.

---

## Baseline Model

A simple baseline model is provided:

**HistGradientBoostingClassifier**

The baseline uses:

- Top 30 features most correlated with the target
- Minimal preprocessing
- No advanced feature engineering

The baseline is intentionally simple and leaves significant room for improvement through:

- Better feature engineering
- Proper handling of missing codes
- Ordinal-aware modeling
- Cross-feature interactions