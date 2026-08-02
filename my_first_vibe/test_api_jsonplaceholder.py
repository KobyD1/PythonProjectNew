import requests


def test_get_post_jsonplaceholder():
    """Example API test (no-auth) for jsonplaceholder.typicode.com/posts/1

    Verifies HTTP 200 and that the returned JSON has id == 1.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200, f"Unexpected status: {resp.status_code}"
    data = resp.json()
    assert isinstance(data, dict), "Response is not JSON object"
    assert data.get("id") == 1, f"Unexpected id: {data.get('id')}"
