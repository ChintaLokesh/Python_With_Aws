import boto3 as b3


def create_user():
    iam = b3.client('iam')
    resource = iam.create_user(UserName='test')
    print(resource)


create_user()
