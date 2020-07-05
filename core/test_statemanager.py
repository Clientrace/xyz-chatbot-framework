
import unittest
from unittest import mock
from engine.statemanager import Context

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



