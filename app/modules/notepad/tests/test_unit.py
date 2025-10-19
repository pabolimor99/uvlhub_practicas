import pytest
from types import SimpleNamespace
from app.modules.notepad.models import Notepad
from app.modules.notepad.services import NotepadService
from unittest.mock import MagicMock

@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass

    yield test_client



def test_notepad_service_delete_success():

    service = NotepadService()
    fake_repo = MagicMock()
    service.repository = fake_repo
    fake_repo.delete.return_value = True

    ok = service.delete(123)

    assert ok is True
    fake_repo.delete.assert_called_once_with(123)

def test_notepad_service_delete_failure():
    
    service = NotepadService()
    fake_repo = MagicMock()
    service.repository = fake_repo
    fake_repo.delete.return_value = False

    ok = service.delete(999)

    assert ok is False
    fake_repo.delete.assert_called_once_with(999)

def test_sample_assertion():
    """
    Igual que en el tutorial: un aserto simple para verificar el entorno de tests.
    """
    greeting = "Hello, World!"
    assert greeting == "Hello, World!"
