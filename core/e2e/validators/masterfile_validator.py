
import os
import yaml
from core.e2e.handlers.exceptions import MasterFileError

def _validate_check_master_file_path():
  """
  Validate Master File if Exist
  """
  if not os.path.exists('src/views/master.yml'):
    raise MasterFileError('Master File YML not found (src/views/master.yml)')


def _validate_master_file_format():
  """
  Validate Master File Format
  """

  with open('src/views/master.yml') as file:
    masterFile = file.read()
    file.close()

  try:
    yaml.safe_load(masterFile)
  except Exception:
    raise MasterFileError('Invalid master file format.')

def _validate_master_file_config_values():
  with open('src/views/master.yml') as file:
    masterFile = file.read()
    file.close()

  config = yaml.safe_load(masterFile)
  requiredKeys = ['botname', 'description', 'init_state', 'states']
  for key in requiredKeys:
    if key not in config:
      raise MasterFileError('Invalid master file format. Missing key '+key)

  if config['init_state'] not in config['states']:
    raise MasterFileError("Invalid master file format. Invalid " + config['init_state']+" in init_state.")

  for state in config['states']:
    if 'next' not in config['states'][state]:
      raise MasterFileError("Invalid master file format. Next state missing in '"+state+"' state.")
    
    if config['states'][state]['next'] not in config['states']:
      raise MasterFileError("Invalid master file format. Value '"+config['states'][state]['next']+"' in state "+state + ".")



