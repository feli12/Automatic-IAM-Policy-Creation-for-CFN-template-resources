# Automatic-IAM-Policy-Creation-for-CFN-template-resources
# Hackathon project


    import json
    import boto3
    from botocore.exceptions import ClientError

    def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
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
                    pol=l[1].lower()+':*'
                    l2.append(pol)
    
    for i in og["Statement"]:
        i["Action"]=l2
    poldoc = json.dumps(og)
    print(poldoc)
