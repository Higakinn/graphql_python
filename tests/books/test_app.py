from fastapi.testclient import TestClient

from books.app import app

client = TestClient(app)


def test_main_graphiql():
    response = client.get("/",headers={"accept": "text/html"})
    print(response)
    print(response.text)
    assert response.status_code == 404
    assert response.text == 'Not Found'

    