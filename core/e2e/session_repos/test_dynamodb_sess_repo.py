
import boto3
import unittest
from unittest import mock
from core.e2e.session_repos.dynamodb_sess_repo import DynamodbSessRepo

class TestDynamodbSessRepo(unittest.TestCase):

  @mock.patch('boto3.client')
  @mock.patch('boto3.resource')
  def test_init_sess_repo(self, boto3Res, boto3Client):
    _ = DynamodbSessRepo('testTableName', 'testRegion')
    boto3Res.assert_called_with(
      'dynamodb',
      region_name='testRegion'
    )

    boto3Client.assert_called_with(
      'dynamodb',
      region_name='testRegion'
    )

  @mock.patch('boto3.client')
  @mock.patch('boto3.resource')
  def test_update_state(self, boto3Res, boto3Client):
    dbSessRepo = DynamodbSessRepo('testTableName', 'testRegion')

    dbSessRepo.update_state('testUserId', 'testState')

    boto3Client.return_value.update_item.assert_called_with(
      {'userId' : {'S' : 'testUserId'}},
      {'state' : {'Value' : {'S' : 'testState'}}}
    )

    






