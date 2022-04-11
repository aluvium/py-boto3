import boto3

def s3_list(name):
    AWS_M_CON=boto3.session.Session(profile_name="root")
    IAM_CON=AWS_M_CON.resource(name)
    for each_b in IAM_CON.buckets.all():
        print(each_b.name)
    return 0

s3_list('s3')

