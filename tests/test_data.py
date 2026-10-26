from heart_diease.data import load_clean,features,target

def test_patient_counts():
  df = load_clean()
  assert len(df) == 302                                  # 303 rows minus 1 duplicate
  assert target(df).sum == 138                           # patients with disease

def test_cp_and_raw_target_removed():
    df = load_clean()
    assert "cp" not in df.columns
    assert "output" not in df.columns


def test_features_and_missing_codes():
    df = load_clean()
    assert features(df).shape[1] == 12
    assert df["caa"].max() <= 3      # no 4 values
    assert df["thall"].min() >= 1    # no 0 values
