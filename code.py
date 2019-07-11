import json
import boto3
import datetime
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    iam = boto3.client('iam')
    obj=s3.Object('buxbuxbuxbbux13','trythis.json')
    data=obj.get()['Body'].read().decode('utf-8')
    j=json.loads(data)
    og={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
    
                ],
                "Resource": "*"
            }
        ]
    }
    og1=og["Statement"][0]
    
    rsrc=j["Resources"]
    n=len(rsrc.keys())
    l1=list()
    l2=["iam:passrole","iam:getrole","iam:createservicelinkedrole"]
    for key in rsrc.keys():
        dic=rsrc[key]
        for key1 in dic.keys():
            if key1=="Type":
                l=dic[key1].split('::')
                if l[1] not in l1 and len(l)==3:
                    l1.append(l[1])
                    pol=l[1].lower()+':kissing_heart:'
                    l2.append(pol)
    
    for i in og["Statement"]:
        i["Action"]=l2
    poldoc = json.dumps(og)
    dict1=event["Records"]
    dict2=dict1[0]
    dict3=dict2["userIdentity"]
    uname=dict3["principalId"].split(':')
    username=uname[1]
    response=iam.list_users()
    dicx=str(response)
    n=dicx.find(key)+len(key)
    strdic=dicx[n:]
    num=strdic.find('arn:aws:iam::')
    strdic1=strdic[num+1:]
    listerine=strdic1.split(",")
    arnn=listerine[0].split(':')
    typeofser=arnn[-1].split('/')
    usersname=typeofser[1]
    userstype=typeofser[0]
    unnnnn=usersname[:-1]
    Response2 = iam.create_policy(PolicyName='testppolic',PolicyDocument=poldoc)
    policyarn = str(Response2['Policy']['Arn'])
    Response1 = iam.attach_user_policy(UserName=unnnnn,PolicyArn=policyarn)
