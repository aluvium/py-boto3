import boto3

def usr_list(name):
    AWS_M_CON=boto3.session.Session(profile_name="root")
    IAM_CON=AWS_M_CON.resource(name)
    for each_u in IAM_CON.users.all():
        print(each_u.name)
    return 0

usr_list('iam')

