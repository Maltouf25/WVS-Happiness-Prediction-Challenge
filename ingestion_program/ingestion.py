import json
import sys
import time
from pathlib import Path

import pandas as pd


EVAL_SETS = ["test_public", "test_private"]


def evaluate_model(model, X_test):
    y_pred = model.predict(X_test)
    return pd.DataFrame(y_pred)


def get_train_data(data_dir):
    data_dir = Path(data_dir)

    # Load full train file
    train_df = pd.read_csv(data_dir / "train.csv")

    # Separate features and target
    X_train = train_df.drop(columns=["A008"])
    y_train = train_df["A008"]

    return X_train, y_train


def get_test_data(data_dir, eval_set):
    data_dir = Path(data_dir)
    return pd.read_csv(data_dir / f"{eval_set}.csv")


def main(data_dir, output_dir):

    from submission import get_model

    # -----------------------------
    # Load training data
    # -----------------------------
    X_train, y_train = get_train_data(data_dir)

    print("Training the model")

    model = get_model()

    start = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start

    print("-" * 10)
    print("Evaluate the model")

    # -----------------------------
    # Predict on test sets
    # -----------------------------
    start = time.time()

    res = {}
    for eval_set in EVAL_SETS:
        X_test = get_test_data(data_dir, eval_set)
        res[eval_set] = evaluate_model(model, X_test)

    test_time = time.time() - start

    print("-" * 10)
    duration = train_time + test_time
    print(f"Completed Prediction. Total duration: {duration}")

    # -----------------------------
    # Write outputs
    # -----------------------------
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save timing metadata
    with open(output_dir / "metadata.json", "w+") as f:
        json.dump(dict(train_time=train_time, test_time=test_time), f)

    # Save predictions
    for eval_set in EVAL_SETS:
        filepath = output_dir / f"{eval_set}_predictions.csv"
        res[eval_set].to_csv(filepath, index=False)

    print()
    print("Ingestion Program finished. Moving on to scoring")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Ingestion program for codabench"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default="/app/input_data",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="/app/output",
    )
    parser.add_argument(
        "--submission-dir",
        type=str,
        default="/app/ingested_program",
    )

    args = parser.parse_args()

    sys.path.append(args.submission_dir)
    sys.path.append(Path(__file__).parent.resolve())

    main(Path(args.data_dir), Path(args.output_dir))