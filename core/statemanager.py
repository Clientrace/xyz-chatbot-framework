
import os
import json
from os import path


class Context:
  """
  Conversation Context Object
  """

  def __init__(self, db, userProfile):
    """
    Initialize Context Object
    :param db: database for state storage
    :param userProfile: user profile object
    :type db: db object
    :type userProfile: json/dictionary
    """

    self.db = db
    self.userProfile = userProfile

  def update_user_info(self, key, value):
    """
    Update dynamodb user detail
    :param value: value to update the item with
    :type key: string
    :type value: string
    """

    pk = {
      'userId' : {
        'S' : self.userProfile['id']
      }
    }

    self.db.update_item(
      pk,
      {
        key : {
          'Value' : {
            'S' : value
          }
        }
      }
    )

  def get_context(self, key):
    """
    Get Conversational Context
    :param key: context item key
    :type key: string
    :returns: context info
    :rtype: string
    """

    if 'contextInfo:' + key in self.userProfile:
      return self.userProfile['contextInfo:' + key]
    return None

  def save_context(self, keyVal):
    """
    Save conversational context
    :param keyVal: key value to save
    :type keyVal: json/dictionary
    """

    pk = {
      'userId' : {
        'S' : self.userProfile['id']
      }
    }

    self.db.update_item(
      pk,
      {
        'contextInfo:' + keyVal['key'] : {
          'Value' : {
            'S' : keyVal['value']
          }
        }
      }
    )


class StateRouter:

  def __init__(self, userObject, msgObject, outputBuilder, profileBuilder=None):
    """
    Initialize State Router Module
    :param userObject: chatbot user info
    :param msgObject: chatbot user msg
    :param outputBuilder: messaging platform outbound builder
    :param profileBuilder: optional userprofile builder
    """

    self.profileBuilder = profileBuilder
    self.userObject = userObject
    self.msgObject = msgObject
    self.outputBuilder = outputBuilder



