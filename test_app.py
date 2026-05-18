import json
from app import app

client = app.test_client()


def test_home():
    response = client.get('/')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert data['message'] == 'Python Web App Running Successfully'


def test_health():
    response = client.get('/health')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert data['status'] == 'healthy'


def test_add_numbers():
    payload = {
        "num1": 10,
        "num2": 20
    }

    response = client.post(
        '/add',
        json=payload
    )

    assert response.status_code == 200

    data = json.loads(response.data)

    assert data['result'] == 30