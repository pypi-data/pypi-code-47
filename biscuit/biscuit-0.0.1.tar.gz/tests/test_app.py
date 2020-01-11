import requests
import pytest

from biscuit.api import API


class TestApp:
    """Test sample web application"""

    def test_default_response_when_no_path(self):
        """Should receive default response with no route handler"""
        resp = requests.get("http://localhost:8000/notreal")

        assert resp.text == "handler not found"
        assert resp.status_code == 404

    def test_handle_request_params(self):
        """Should handle parameterized request paths"""
        resp = requests.get("http://localhost:8000/hello/jake")

        assert resp.text == "hi jake"
        assert resp.status_code == 200

    def test_handle_request(self):
        """Should handle regular request paths"""
        resp = requests.get("http://localhost:8000/home")

        assert resp.text == "Hi from home"
        assert resp.status_code == 200

    def test_handle_class_based_view_get(self):
        """Should handle GET requests for CBV"""
        resp = requests.get("http://localhost:8000/article")

        assert resp.text == "Article GET"
        assert resp.status_code == 200

    def test_handle_class_based_view_post(self):
        """Should handle POST requests for CBV"""
        resp = requests.post("http://localhost:8000/article")

        assert resp.text == "Article POST"
        assert resp.status_code == 200
