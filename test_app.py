from app import app


def test_home_returns_welcome():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_health_returns_up():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "UP"}


def test_about_returns_version():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
    assert response.get_json()["version"] == "1.0.0"
