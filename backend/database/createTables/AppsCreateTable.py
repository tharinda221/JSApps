# import classes
from backend.database.connection import *


def createAppTable():
    connection = getConnection()
    table = connection.create_table(
            TableName='Apps',
            KeySchema=[
                {
                    'AttributeName': 'AppID',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'AppCreatedTimeDate',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'AppID',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'AppCreatedTimeDate',
                    'AttributeType': 'S'
                }

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
    )
    print("Table status:", table.table_status)
createAppTable()