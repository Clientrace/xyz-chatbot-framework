

class SessionDBService:

  def __init__(self, repo):
    """
    Initialize Session Repo
    """
    self.repo = repo


  def init_user_session(self, stateObject):
    """
    Initialize User Session
    :param stateObject: user state object to initialize
    :type stateObject: json/dictionary
    """

    self.repo.put_item(stateObject)

  def update_session_state(self, userId, state):
    """
    Update session state
    :param userId: user chatbot session id
    """

    self.repo.update_item(userId, state)




