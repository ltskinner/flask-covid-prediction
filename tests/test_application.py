import json

import pytest

from application import application as flask_application


@pytest.fixture(name="app")
def app_fixture():
    flask_application.config.update({"TESTING": True})

    # other setup can go here
    yield flask_application
    # clean up / reset resources her


@pytest.fixture(name="client")
def client(app):
    return app.test_client()


def test_home(client):
    resp = client.get("/")

    expected_content = "Covid Prediction"

    assert expected_content in resp.text


def test_predict_json(client):
    """To send JSON data, pass an object to json
    https://flask.palletsprojects.com/en/2.2.x/testing/#json-data
    """
    resp = client.post(
        "/predict",
        json={
            "day": 45,
            "total": 67,
        },
    )

    result = resp.data.decode("utf-8")
    result = json.loads(result)

    pred_key = "prediction"
    assert pred_key in result.keys()
    assert isinstance(result[pred_key], float)


def test_predict_form(client):
    """To send form data, pass a dict to data
    https://flask.palletsprojects.com/en/2.2.x/testing/#form-data
    """
    resp = client.post(
        "/predict",
        data={
            "day": 45,
            "total": 67,
        },
    )
    expected_content = "Predicted positive cases"
    assert expected_content in resp.text
