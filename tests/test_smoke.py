import pandas as pd

from src.pipeline import load_and_clean_data


def test_smoke():
    assert True


def test_load_and_clean_data_maps_churn(tmp_path):
    sample = pd.DataFrame(
        {
            "customerID": ["1", "2", "3"],
            "tenure": [1, 12, 24],
            "MonthlyCharges": [20.0, 70.5, 50.0],
            "TotalCharges": ["20.0", " 840.0 ", " "],
            "Churn": ["Yes", "No", "No"],
        }
    )
    csv_path = tmp_path / "sample.csv"
    sample.to_csv(csv_path, index=False)

    cleaned = load_and_clean_data(csv_path)

    assert "customerID" not in cleaned.columns
    assert cleaned["Churn"].tolist() == [1, 0, 0]
    assert cleaned["TotalCharges"].isna().sum() == 1
