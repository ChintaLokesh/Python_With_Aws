import boto3 as b3


def list_all_policies():
    iam = b3.client('iam')
    paginator = iam.get_paginator('list_policies')
    for response in paginator.paginate(Scope='Local'):
        for policy in response['Policies']:
            print('policy name :{}, policyID :{}'.format(policy['PolicyName'], policy['PolicyId']))


list_all_policies()
