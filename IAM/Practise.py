import boto3 as b3


def attach_policy(policyArn, username):
    response = b3.client('iam').attach_user_policy(UserName=username, PolicyArn=policyArn)
    print(response['ResponseMetadata']['HTTPStatusCode'])

attach_policy('arn:aws:iam::379148671212:policy/p1','programmmer')
