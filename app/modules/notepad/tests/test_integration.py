import pytest

def test_notepad_requires_login_redirects_to_login(test_client):
    """
    Como /notepad tiene @login_required, sin sesión debe redirigir a /login (302)
    o devolver 401 según la config.
    """
    resp = test_client.get("/notepad", follow_redirects=False)
    assert resp.status_code in (302, 401)
    if resp.status_code == 302:
        assert "/login" in resp.headers.get("Location", "")