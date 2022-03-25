import boto3

AWS_M_CONF=boto3.session.Session(profile_name="root")
IAM_CONF=AWS_M_CONF.resource('iam')

for each_u in IAM_CONF.users.all():
    print(each_u)


