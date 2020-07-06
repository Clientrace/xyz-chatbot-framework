
import unittest
from unittest import mock
from core.e2e.session_db_service import SessionDBService

class TestSessionDBService(unittest.TestCase):


  def test_init_user_session(self):
    repo = mock.Mock()
    service = SessionDBService(repo)

    stateObject = {'testKey' : 'testValue'}
    service.init_user_session(stateObject)
    repo.put_item.assert_called_with(stateObject)

  def test_update_session_state(self):
    repo = mock.Mock()
    service = SessionDBService(repo)

    service.update_session_state('testUserId', 'testState')
    repo.update_item('testUserid', 'testState')







