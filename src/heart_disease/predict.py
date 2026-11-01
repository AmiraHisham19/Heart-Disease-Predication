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
