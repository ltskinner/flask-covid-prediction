import joblib
from flask import Flask, jsonify, render_template, request

model = joblib.load("./models/covid_linear_regression.joblib")

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("index.html")


@application.route("/predict", methods=["POST"])
def predict():
    # TODO: input verification
    # json request
    if len(request.form) == 0:
        print("\n\n\n\nJSON REQUEST\n\n\n\n")
        json_payload = request.json
        prediction = model.predict(
            [[int(json_payload["day"]), int(json_payload["total"])]]
        )
        return jsonify({"prediction": prediction[0]})

    # form-based request
    day = request.form.get("day")
    total = request.form.get("total")
    prediction = model.predict([[int(day), int(total)]])

    prediction_text = f"Predicted positive cases: {prediction[0]}"
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8080, debug=True)
