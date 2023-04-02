import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# readonly
MODEL_PATH = "./models/covid_linear_regression.joblib"


if __name__ == "__main__":
    training_csv = "./data/national-history-update.csv"
    df = pd.read_csv(training_csv)

    model = LinearRegression()
    X = df[["day", "totalTestResultsIncrease"]].values
    y = df["positiveIncrease"].values
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
