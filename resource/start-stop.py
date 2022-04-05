import boto3 
import sys
from os import system

AWS_M_CON=boto3.session.Session(profile_name="root")
EC2_RE=AWS_M_CON.resource("ec2", "eu-central-1")

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
        inst_id=input('Please specify EC2 id: ')
        chosen_inst=EC2_RE.Instance(inst_id)
        system('clear')
        print("Starting ec2 instance...")
        chosen_inst.start()

    elif opt==2:
        inst_id=input('Please specify EC2 id: ')
        chosen_inst=EC2_RE.Instance(inst_id)
        system('clear')
        print("Stopping ec2 instance...")
        chosen_inst.stop()

    elif opt==3:
        inst_id=input('Please specify EC2 id: ')
        chosen_inst=EC2_RE.Instance(inst_id)
        system('clear')
        print("Terminating ec2 instance...")
        chosen_inst.terminate()

    elif opt==4:
        system('clear')
        print("Goodbye")
        sys.exit()

    else:
        print("Your input is invalid. Try again.")
