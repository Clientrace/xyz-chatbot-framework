
import os
import boto3


class DynamodbSessRepo:


  def __init__(self, tableName, region):
    """
    Initialize Dynamodb Sess Repo
    """

    self.tableName = tableName
    self.DYNAMODB_c = boto3.client(
      'dynamodb',
      region_name = region
    )
    self.DYNAMODB_r = boto3.resource(
      'dynamodb',
      region_name = region
    )


  def update_state(self, userId, state):
    """
    Update user state in chabot
    :param userId: user id to update
    :param state: state to proceed to
    :type userId: string
    :type state: string
    """

    partitionKey = {
      'userId' : {'S' : userId}
    }

    self.DYNAMODB_c.update_item(
      partitionKey,
      {
        'state' : {'Value' : {'S' : state}}
      }
    )






