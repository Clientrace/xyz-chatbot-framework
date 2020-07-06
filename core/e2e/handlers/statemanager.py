
import os
import json
import yaml


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
  """
  Chatbot State Transition Router
  """

  def __init__(self, userObject, msgObject, outputBuilder, stateService, profileBuilder=None):
    """
    Initialize State Router Module
    :param userObject: chatbot user info
    :param msgObject: chatbot user msg
    :param outputBuilder: messaging platform outbound builder
    :param stateService: chatbot state service
    :param profileBuilder: optional userprofile builder
    """

    self.profileBuilder = profileBuilder
    self.userObject = userObject
    self.msgObject = msgObject
    self.outputBuilder = outputBuilder
    self.stateService = stateService


  def _next_state(self, state):
    """
    Update User State
    :param state: state name
    :type state: string
    """

    self.stateService.update_session_state(
      self.userObject['id'],
      state
    )


  def _init_user(self):
    """
    Initilize User Record
    :returns: user profile object
    :rtype: json/dictionary
    """

    userProfile = self.profileBuilder(self.userObject['id'], self.stateService)()
    self.stateService.init_user_session(userProfile)
    return userProfile


  def _get_user_profile(self):
    """
    Get User Profile Record
    :returns: user profile record
    :rtype: json/dictionary
    """

    userProfile = self.stateService._get_user_profile(self.userObject['id'])
    if userProfile == None:
      return self._init_user()
    return userProfile


  def _get_init_state(self):
    """
    Get initial state
    :returns: initial chatbot state
    :rtype: string
    """

    masterFile = open('src/views/master.yml').read()
    masterConfig = yaml.safe_load(masterFile)
    return masterConfig['init_state']


  def execute(self):
    """
    Execute Current State
    """

    




