import boto3 
import sys
from os import system

AWS_M_CON=boto3.session.Session(profile_name="root")
EC2_RE=AWS_M_CON.resource("ec2", "eu-cental-1")
EC2_CLI=AWS_M_CON.client("ec2", "eu-central-1")

def chosen_id():
    inst_id=input('Please specify EC2 IP address: ')
    chosen_inst=EC2_RE.Instance(inst_id)
    system('clear')
    print(dir(chosen_inst))
    chosen_inst.start()
    return 0

while True:
    print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

PRESS:  - - - - - - - - - - - 
 1. Start 
 2. Stop  
 3. Terminate  
 4. Exit 
        - - - - - - - - - - - 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    opt=int(input("Enter the number: "))
    if opt==1:
        chosen_id()
        print("Starting ec2 instance...")

    elif opt==2:
        chosen_id()  
        print("Stoping ec2 instance...")

    elif opt==3:
        chosen_id()
        print("Terminating ec2 instance...")

    elif opt==4:
        system('clear')
        print("Goodbye")
        sys.exit()

    else:
        print("Your input is invalid. Try again.")
