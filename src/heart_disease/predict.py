""" Predict heart disease risk for one patient with the saved model"""

from __future__ import annotations

import argparse
import json
import joblib
import pandas as pd
from . import config

THERSHOLD = 0.5

def load_model(path =config.MODEL_PATH):
  if not path.exists():
    raise FileNotFoundError(f"Model not found at {path}.")
  return joblib.load(path)

def check_inputs (row: dict) -> list[str]:
  problems = []
  for name in config.FEATURES:
    if name not in row:
      problems.append(f"missing value for '{name}'")
      continue
    try:
      value = float(row[name])
    except (TypeError,ValueError):
      problems.append(f"'{name}' must be a number, got {row[name]!r}")
      continue
    if name in config.LIMITS:
      low,high = config.LIMITS[name]
      if not low <= value <= high:
        problems.append(f"'{name}' must be between {low} and {high}, got {value}")
    elif value not in config.CODES[name]:
      problems.append(f"'{name}' must be one of {sorted(config.CODES[name])}, got {value}")
  return problems

def predict_proba(rows: list[dict], model=None):
    """Disease probability (0 to 1) for each patient in `rows`."""
    if model is None:
        model = load_model()
    X = pd.DataFrame(rows)[config.FEATURES]      # same columns, same order as training
    return model.predict_proba(X)[:, 1]          # column 1 = disease
 
 
def predict_one(row: dict, model=None) -> dict:
    """Validate one patient and return the probability and a label."""
    problems = check_inputs(row)
    if problems:
        raise ValueError("; ".join(problems))
    prob = float(predict_proba([row], model)[0])
    label = ("Higher likelihood of heart disease" if prob >= THERSHOLD
             else "Lower likelihood of heart disease")
    return {"probability": round(prob * 100, 1), "label": label}
 
 
def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate heart disease risk for one patient.")
    parser.add_argument("--json", required=True, help="One patient as a JSON object")
    row = json.loads(parser.parse_args().json)
    result = predict_one(row)
    print(f"{result['label']} ({result['probability']}%)")
 
 
if __name__ == "__main__":
    main()
 


