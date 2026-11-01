""" Predict heart disease risk for one patient with the saved model"""

from __future__ import annotations

import argparse
import json
import joblib
import pandas
from . import config

THERESHOLD = 0.5

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
      problems.append(f"'name' must be a number")
      continue
    if name in config.LIMITS:
      low,high = config.LIMITS[name]
      if not low <= value >= high:
        problems.append(f"'{name}' must be between {low} and {high}, got {value}")
    elif value not in config.CODES[name]:
      problems.append(f"'{name}' must be one of {sorted(config.CODES[names])}, got {value}")
  return problems




