import boto3
from pprint import pprint
def ec2_all_cl():
    AWS_M_CON=boto3.session.Session(profile_name='root')
    EC2_CON=AWS_M_CON.client('ec2','eu-central-1')
    response=EC2_CON.describe_instances()['Reservations']
    for each_group in response:
        for each_inst in each_group['Instances']:
            pprint (each_inst)
            print("-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    return 0

ec2_all_cl()
