import boto3 
import sys
from os import system
from ec2_list import ec2_list

AWS_M_CON=boto3.session.Session(profile_name="root")
EC2_RE=AWS_M_CON.resource("ec2", "eu-central-1")

def input_1():
    inst_id=input('Please specify EC2 id: ')
    value=EC2_RE.Instance(inst_id)
    system('clear')
    return value

def main():
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
        ec2_list()
        opt=int(input("Enter the number: "))
        if opt==1:
            chosen_inst=input_1()
            print("Starting ec2 instance...")
            chosen_inst.start()
            chosen_inst.wait_until_running()  
        elif opt==2:
            chosen_inst=input_1()
            print("Stopping ec2 instance...")
            chosen_inst.stop()
            chosen_inst.wait_until_stopped()
        elif opt==3:
            chosen_inst=EC2_RE.Instance(inst_id)
            print("Terminating ec2 instance...")
            chosen_inst.terminate()
            chosen_inst.wait_until_terminated()
        elif opt==4:
            system('clear')
            print("Goodbye")
            sys.exit()
        else:
            print("Your input is invalid. Try again.")
    return None

if __name__=="__main__":
    main()


