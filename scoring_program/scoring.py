import json
from pathlib import Path

import pandas as pd
from sklearn.metrics import cohen_kappa_score, mean_absolute_error


EVAL_SETS = ["test_public", "test_private"]


def compute_metrics(predictions, targets):
    # Flatten arrays
    predictions = predictions.fillna(-10).values.ravel()
    targets = targets.values.ravel()

    qwk = cohen_kappa_score(targets, predictions, weights="quadratic")
    mae = mean_absolute_error(targets, predictions)

    return qwk, mae


def main(reference_dir, prediction_dir, output_dir):
    scores = {}

    for eval_set in EVAL_SETS:
        print(f"Scoring {eval_set}")

        predictions = pd.read_csv(
            prediction_dir / f"{eval_set}_predictions.csv"
        )
        targets = pd.read_csv(
            reference_dir / f"{eval_set}_labels.csv"
        )

        qwk, mae = compute_metrics(predictions, targets)

        scores[f"{eval_set}_qwk"] = float(qwk)
        scores[f"{eval_set}_mae"] = float(mae)

    # Add train and test times
    json_durations = (prediction_dir / "metadata.json").read_text()
    durations = json.loads(json_durations)
    scores.update(**durations)

    print(scores)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "scores.json").write_text(json.dumps(scores))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Scoring program for codabench"
    )
    parser.add_argument(
        "--reference-dir",
        type=str,
        default="/app/input/ref",
    )
    parser.add_argument(
        "--prediction-dir",
        type=str,
        default="/app/input/res",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="/app/output",
    )

    args = parser.parse_args()

    main(
        Path(args.reference_dir),
        Path(args.prediction_dir),
        Path(args.output_dir),
    )