from __future__ import annotations

from pathlib import Path
import pandas as pd
from . import config

def load_raw (path:str | Path = config.DATA_PATH) -> pd.DataFrame:
  return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
  """ Disease = 1, Dropping Duplicates , Replacing missing vales with most common one, Dropping cp feature """
  out = df.drop_duplicates().reset_index(drop=True)   # 303 -> 302 patients
  out[config.TARGET] = (out[config.RAW_TARGET] == 0).astype(int)
  out = out.drop(columns =[config.RAW_TARGET] + config.DROPPED)
  out["caa"] = out["caa"].replace(4, 0)      # 4 = missing, most common value is 0
  out["thall"] = out["thall"].replace(0, 2)  # 0 = missing, most common value is 2
  return out

def load_clean (path:str | Path = config.DATA_PATH) -> pd.DataFrame:
  return clean(load_raw(path))

def features(df):
    return df[config.FEATURES]
  
def target(df):
    return df[config.TARGET]

