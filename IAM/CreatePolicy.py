import json

import boto3 as b3


def create_policy():
    iam = b3.client('iam')

    user_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    print(str(user_policy))
    print(type(str(user_policy)))
    response = iam.create_policy(PolicyName='pyFullAccess', PolicyDocument=json.dumps(user_policy))
    print(response)


create_policy()
