import pytest

from heart_disease.predict import check_inputs,predict_one

HEALTHY = dict(age=40, sex=0, trtbps=120, chol=200, fbs=0, restecg=1,
               thalachh=175, exng=0, oldpeak=0.0, slp=2, caa=0, thall=2)
HIGH_RISK = dict(age=62, sex=1, trtbps=150, chol=280, fbs=1, restecg=0,
                 thalachh=110, exng=1, oldpeak=3.0, slp=1, caa=3, thall=3)

def test_vaild_inputs_no_problems():
  assert check_inputs(HEALTHY) == []

def test_bad_inputs():
    assert check_inputs({**HEALTHY, "age": 500})            # out of range
    assert check_inputs({**HEALTHY, "thall": 0})            # 0 is a missing-value code

def test_invalid_patient():
    with pytest.raises(ValueError):
        predict_one({**HEALTHY, "age": -5})

def test_healthy_scores_low_and_high_risk_scores_high():
    healthy = predict_one(HEALTHY)
    risky = predict_one(HIGH_RISK)
    assert healthy["probability"] < 50 < risky["probability"]
    assert healthy["label"].startswith("Lower")
    assert risky["label"].startswith("Higher")
