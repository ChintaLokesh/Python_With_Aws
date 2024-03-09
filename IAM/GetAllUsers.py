import boto3 as b3


def get_all_users():
    iam = b3.client('iam')
    paginator = iam.get_paginator('list_users')
    for page in paginator.paginate():
        for user in page['Users']:
            print(user['UserName'])


get_all_users()
