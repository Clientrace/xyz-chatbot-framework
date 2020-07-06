
class Error(Exception):
  """
  Base Class for Exceptions
  """
  pass


class MasterFileError(Error):
  """
  Master File View Error
  """

  def __init__(self, message):
    """
    Initialize Master File Error
    :param message: master file error message
    :type message: string
    """

    self.message = message



  