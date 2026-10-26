"""Project-wide constants: paths, features and labels"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "heart.csv"
MODELS_DIR = ROOT / "models"
MODEL_PATH = MODELS_DIR / "heart_attack_pipeline.pkl"
FEATURES_PATH = MODELS_DIR / "features.pkl"
FIGURES_DIR = ROOT / "reports" / "figures"

RANDOM_STATE = 1          # replace with the values from your final notebook
TEST_SIZE = 0.2           # stratified 80/20 split (61 test patients)
CV_FOLDS, CV_REPEATS = 5, 10
LR_C = 0.1

RAW_TARGET = "output"     # in this file output == 0 means DISEASE
TARGET = "disease"        # 1 = disease, 0 = no disease
DROPPED = ["cp"]          # excluded: referral selection bias

FEATURES = ["age", "sex", "trtbps", "chol", "fbs", "restecg",
            "thalachh", "exng", "oldpeak", "slp", "caa", "thall"]

LIMITS = {"age": (1, 120), "trtbps": (50, 250), "chol": (50, 700),
          "thalachh": (50, 250), "oldpeak": (0, 10)}

CODES = {
    "sex": {0: "Female", 1: "Male"},
    "fbs": {0: "<= 120 mg/dL", 1: "> 120 mg/dL"},
    "restecg": {0: "Left ventricular hypertrophy", 1: "Normal", 2: "ST-T wave abnormality"},
    "exng": {0: "No", 1: "Yes"},
    "slp": {0: "Downsloping", 1: "Flat", 2: "Upsloping"},
    "caa": {0: "0", 1: "1", 2: "2", 3: "3"},
    "thall": {1: "Fixed defect", 2: "Normal", 3: "Reversible defect"},
}
