import boto3

def ec2_list_cl(alice, betty):
    AWS_M_CON=boto3.session.Session(profile_name='root')
    EC2_CON=AWS_M_CON.client('ec2','eu-central-1')
    response=EC2_CON.describe_instances()['Reservations']
    for each_group in response:
        for each_inst in each_group['Instances']:
            print (each_inst[alice], each_inst[betty])
    return 0

# Other usefull keys for monitorinig ==> 
# PrivateIpAddress, LaunchTime, ImageId, InstanceType, KeyName, BlockDeviceMapping, NetworkInterfaces
# for all --> print (each_inst) without key

ec2_list_cl('InstanceId','PublicIpAddress')

# if 0 instances it returns error ==> no IP -,- 
