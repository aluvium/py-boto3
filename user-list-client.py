import boto3

def usr_list_cl(alice,betty):
    AWS_M_CON=boto3.session.Session(profile_name='root')
    IAM_CON=AWS_M_CON.client('iam')
    for each_u in IAM_CON.list_users()['Users']:
        print(each_u[alice])
        print(each_u[betty])
    return 0
usr_list_cl('UserName','UserId')    
# UserName, UserId, Arn, CreateDate, Path  == >  possible keys to use
