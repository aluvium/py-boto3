#ec2 list
import boto3

def ec2_list():
    AWS_M_CON=boto3.session.Session(profile_name="root")
    EC2_CON=AWS_M_CON.resource('ec2', 'eu-central-1')
    for each in EC2_CON.instances.all():
        print(each.id, each.state, each.public_ip_address)
    return 0

ec2_list()

