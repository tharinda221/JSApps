# import classes
from backend.database.connection import *


def createUserTable():
    connection = getConnection()
    table = connection.create_table(
            TableName='Users',
            KeySchema=[
                {
                    'AttributeName': 'userId',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'userId',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
    )
    print("Table status:", table.table_status)

createUserTable()