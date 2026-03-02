# Evaluation

This challenge uses two complementary evaluation metrics:

- Quadratic Weighted Kappa (QWK)
- Mean Absolute Error (MAE)

Because happiness is an **ordinal variable**, evaluation must reflect ordered prediction quality.

---

## 1️⃣ Quadratic Weighted Kappa (QWK)

Quadratic Weighted Kappa measures:

- Agreement between predicted and true labels
- Penalizes larger disagreements more heavily
- Takes ordinal structure into account

Why QWK?

- Predicting "Very Happy" instead of "Happy" is less severe than predicting "Very Unhappy"
- QWK penalizes large ordinal mistakes more strongly
- Widely used for ordinal classification problems

QWK ranges from:

- -1 (complete disagreement)
- 0 (random agreement)
- 1 (perfect agreement)

This is the **primary ranking metric**.

---

## 2️⃣ Mean Absolute Error (MAE)

MAE measures:

- The average absolute difference between predicted and true happiness scores

Why MAE?

- Directly captures how far predictions are from true values
- Simple and interpretable
- Sensitive to magnitude of errors

For ordinal targets, MAE naturally reflects ordering quality.

Lower MAE is better.

---

## Why Use Both?

QWK focuses on:

- Agreement quality
- Ordinal consistency

MAE focuses on:

- Absolute distance
- Numerical accuracy

Using both metrics ensures models:

- Respect ordinal structure
- Avoid large misclassifications
- Provide numerically stable predictions

---

## Final Ranking

- The public leaderboard is computed on `test_public`
- The final ranking is computed on `test_private`
- QWK is the primary ranking metric
- MAE is provided as a complementary metric