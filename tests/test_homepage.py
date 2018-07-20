def test_homepage(client):
    r = client.get('/')
    assert r.status_code == 200
    assert b'Hello World' in r.data
