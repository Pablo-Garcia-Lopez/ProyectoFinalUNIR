import os
import sys
import pytest

# Ensure project root is on sys.path so `import app` works when pytest runs from anywhere
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import create_app, db

@pytest.fixture
def app():
    # Use the named config that exists in app/config.py
    app = create_app("development")
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        # Clean up DB state after tests
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
