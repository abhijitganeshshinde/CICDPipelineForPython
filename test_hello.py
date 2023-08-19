import hello

def test_hello():
    client = hello.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'hello'