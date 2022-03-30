import boto3

def s3_list(name):
    AWS_M_CONF=boto3.session.Session(profile_name="root")
    IAM_CONF=AWS_M_CONF.resource(name)
    for each_b in IAM_CONF.buckets.all():
        print(each_b.name)
    return 0

s3_list('s3')

