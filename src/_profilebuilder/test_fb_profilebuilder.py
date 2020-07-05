
import unittest
from unittest import mock
from src._profilebuilde.fb_profile_builder import FBProfileBuilder

class TestFBProfileBuilder(unittest.TestSuite):

  @mock.patch('requests')
  def test_init_fb_profilebuilder(self, mockReq):
    stateService = mock.Mock()
    fbProfileBuilder = FBProfileBuilder(
      'testUserId',
      stateService
    )

    mockReq.get.return_value = {
      'testkey' : 'testValue'
    }

    userInfo = fbProfileBuilder._get_user_info()




