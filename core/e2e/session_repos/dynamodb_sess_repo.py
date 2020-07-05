
import os
import boto3


class DynamodbSessRepo(self):


  def __init__(self, tableName, region):
    """
    Initialize Dynamodb Sess Repo
    """

    self.tableName = tableName
    self.DYNAMODB_c = boto3.client(
      'dynamodb',
      region_name = region
    )
    self.DYNAMODB_r = boto3.client(
      'dynamodb',
      region_name = region
    )


