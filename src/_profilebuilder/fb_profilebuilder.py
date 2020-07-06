
import os
import requests

class FBProfileBuilder:

  def __init__(self, userId, stateService):
    self.userId = userId
    self.stateService = stateService

  def _get_user_info(self):
    """
    Get facebook user info for profile building
    :returns: user info
    :rtype: json/dictionary
    """
    URL = 'https://graph.facebook.com/v3.3/' + self.userId\
      + '?fields=first_name,last_name&access_token' + os.environ['FB_ACCESS_TOKEN']
    resp = requests.get(URL)
    return resp.json()

  def __call__(self):
    userInfo = self._get_user_info()
    self.stateService.init_user_session({
      'userId' : self.userId,
      'first_name' : userInfo['first_name'],
      'last_name' : userInfo['last_name']
    })
    return userInfo






