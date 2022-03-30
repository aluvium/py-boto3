import boto3

def usr_list(name):
    AWS_M_CONF=boto3.session.Session(profile_name="root")
    IAM_CONF=AWS_M_CONF.resource(name)
    for each_u in IAM_CONF.users.all():
        print(each_u.name)
    return 0

usr_list('iam')

