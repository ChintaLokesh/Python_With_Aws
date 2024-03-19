import boto3 as b3


def update_user(old_username, new_username):
    iam = b3.client('iam')
    response = iam.update_user(UserName=old_username, NewUserName=new_username)
    print(response)


# update_user('tester', 'tester1')
update_user(old_username='tester1',new_username='tester2')