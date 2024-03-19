import boto3 as b3


def list_all_users():
    iam = b3.client('iam')
    paginator = iam.get_paginator('list_users')
    # print(paginator)
    for page in paginator.paginate():
        print(page['IsTruncated'])
        print(page['ResponseMetadata']['RetryAttempts'])
        # print(page['Users'][''])
        for user in page['Users']:
            print(' user is {} create Date is {}'.format(user['UserName'], user['CreateDate']))


list_all_users()
