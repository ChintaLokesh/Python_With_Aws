import boto3 as b3


def create_user(username):
    iam = b3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)


create_user('tester')
