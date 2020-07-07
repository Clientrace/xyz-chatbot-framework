
import os
import unittest
from unittest import mock
from core.e2e.validators import masterfile_validator
from core.e2e.handlers.exceptions import MasterFileError


class TestMasterFileValidator(unittest.TestCase):

  @mock.patch('os.path')
  def test_check_master_file_path(self, mock_os):
    mock_os.exists.return_value = False
    with self.assertRaises(Exception) as context:
      masterfile_validator._validate_check_master_file_path()

    self.assertEqual(
      context.exception.args[0],
      'Master File YML not found (src/views/master.yml)'
    )


  @mock.patch('yaml.safe_load')
  def test_validate_master_file_format(self, safe_load):
    safe_load.side_effect = Exception

    with self.assertRaises(Exception) as context:
      masterfile_validator._validate_master_file_format()

    self.assertEqual(
      context.exception.args[0],
      'Invalid master file format.'
    )


  @mock.patch('yaml.safe_load')
  def test_validate_master_file_config(self, safe_load):
    safe_load.return_value = {}

    with self.assertRaises(Exception) as context:
      masterfile_validator._validate_master_file_config_values()

    self.assertEqual(
      context.exception.args[0],
      'Invalid master file format.'
    )


  @mock.patch('yaml.safe_load')
  def test_validate_master_file_states(self, safe_load):
    safe_load.return_value = {
      'botname' : 'testBotName',
      'description' : 'testDescription',
      'init_state' : 'main',
      'states' : {
        'welcome' : {}
      }
    }

    with self.assertRaises(Exception) as context:
      masterfile_validator._validate_master_file_config_values()

    self.assertEqual(
      context.exception.args[0],
      "Invalid master file format. Invalid main in init_state."
    )

    safe_load.return_value = {
      'botname' : 'testBotName',
      'description' : 'testDescription',
      'init_state' : 'welcome',
      'states' : {
        'welcome' : {}
      }
    }

    with self.assertRaises(Exception) as context:
      masterfile_validator._validate_master_file_config_values()

    self.assertEqual(
      context.exception.args[0],
      "Invalid master file format. Next state missing in 'welcome' state."
    )




