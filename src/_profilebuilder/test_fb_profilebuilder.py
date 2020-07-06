
import os
import requests
import unittest
from unittest import mock
from src._profilebuilder.fb_profilebuilder import FBProfileBuilder

class TestFBProfileBuilder(unittest.TestCase):

  os.environ['FB_ACCESS_TOKEN'] = 'testToken'

  @mock.patch('requests.get')
  def test_fb_profilebuilder(self, mockReqGet):
    stateService = mock.Mock()
    fbProfileBuilder = FBProfileBuilder(
      'testUserId',
      stateService
    )

    getReturn = {
      'first_name' : 'testFirstName',
      'last_name' : 'testLastName'
    }
    mockReqGet.return_value.json.return_value = getReturn

    resp = fbProfileBuilder()
    self.assertEqual(getReturn, resp)

    stateService.init_user_session.assert_called_with({
      'userId' : 'testUserId',
      'first_name' : 'testFirstName',
      'last_name' : 'testLastName'
    })







