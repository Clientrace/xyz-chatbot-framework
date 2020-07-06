
import unittest
from unittest import mock
from core.e2e.handlers.statemanager import Context, StateRouter
from core.e2e.handlers.exceptions import MasterFileError

class TestContext(unittest.TestCase):

  def test_update_user_info(self):
    db = mock.Mock()
    userProfile = {
      'id' : 'testUserId'
    }
    context = Context(db, userProfile)
    context.update_user_info('testKey', 'testValue')

    db.update_item.assert_called_with(
      {
        'userId' : { 'S' : 'testUserId' }
      },
      {
        'testKey' : { 'Value' :  {'S' : 'testValue'}}
      }
    )


  def test_get_context(self):
    db = mock.Mock()
    userProfile = {
      'id' : 'testUserId',
      'contextInfo:testKey' : 'testValue'
    }

    context = Context(db, userProfile)
    self.assertEqual(context.get_context('testNone'), None)
    self.assertEqual(context.get_context('testKey'), 'testValue')


  def test_save_context(self):
    db = mock.Mock()
    userProfile = {
      'id' : 'testUserId'
    }

    context = Context(db, userProfile)
    context.save_context({
      'key' : 'testKey',
      'value' : 'testValue'
    })

    db.update_item.assert_called_with(
      {
        'userId' : {'S' : 'testUserId'}
      },
      {
        'contextInfo:testKey' : {
          'Value' : {
            'S' : 'testValue'
          }
        }
      }
    )


  def test_next_state(self):
    userObject = {
      'id' : 'testUserId'
    }
    msgObject = {
      'msg' : 'test message'
    }

    stateService = mock.Mock()
    outputBuilder = mock.Mock()
    profileBuilder = mock.Mock()

    stateRouter = StateRouter(
      userObject,
      msgObject,
      outputBuilder,
      stateService,
      profileBuilder
    )

    stateRouter._next_state('nextStateTest')
    stateService.update_session_state.assert_called_with(
      'testUserId',
      'nextStateTest'
    )


  def test_init_user(self):
    userObject = {
      'id' : 'testUserId'
    }
    msgObject = {
      'msg' : 'test message'
    }


    stateService = mock.Mock()
    outputBuilder = mock.Mock()
    profileBuilder = mock.Mock()

    profileBuilder.return_value = mock.Mock(return_value={
      'id' : 'testUserId',
      'first_name' : 'testFirstName',
      'last_name' : 'testLastName'
    })

    stateRouter = StateRouter(
      userObject,
      msgObject,
      outputBuilder,
      stateService,
      profileBuilder
    )

    stateRouter._init_user()
    profileBuilder.assert_called_with('testUserId', stateService)
    stateService.init_user_session.assert_called_with({
      'id' : 'testUserId',
      'first_name' : 'testFirstName',
      'last_name' : 'testLastName'
    })

  @mock.patch('builtins.open')
  def test_get_init_state(self, mock_open):
    mock_open.return_value.read.return_value = "botname: testBotName\ninit_state: welcome\n"

    userObject = {
      'id' : 'testUserId'
    }
    msgObject = {
      'msg' : 'test message'
    }

    stateService = mock.Mock()
    outputBuilder = mock.Mock()
    profileBuilder = mock.Mock()

    stateRouter = StateRouter(
      userObject,
      msgObject,
      outputBuilder,
      stateService,
      profileBuilder
    )

    resp = stateRouter._get_init_state()
    mock_open.assert_called_with('src/views/master.yml')

    self.assertEqual(resp, 'welcome')

  def test_master_file_validations(self):
    self.fail()


  def test_execute_state(self):
    userObject = {
      'id' : 'testUserId'
    }
    msgObject = {
      'msg' : 'test message'
    }

    stateService = mock.Mock()
    outputBuilder = mock.Mock()
    profileBuilder = mock.Mock()

    stateService._get_user_profile.return_value = {
      'userId' : 'testUserId',
      'first_name' : ''
    }

    stateRouter = StateRouter(
      userObject,
      msgObject,
      outputBuilder,
      stateService,
      profileBuilder
    )

    stateRouter.execute()




