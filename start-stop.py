import boto3 
import sys

AWS_M_CON=boto3.session.Session(profile_name="root")
EC2_CLI=AWS_M_CON.resource("ec2", "eu-cental-1")
EC2_RE=AWS_M_CON.client("ec2", "eu-central-1")

while True:
    print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

- - - - PRESS:  - - - - - - - - - - - 
         1. Start 
           2. Stop  
             3. Terminate  
                    4. Exit 
                            - - - - - - - - - - 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    opt=int(input("Enter the number: "))
    if opt==1:
        print("Starting ec2 instance...")
    elif opt==2:
        print("Stoping ec2 instance...")
    elif opt==3:
        print("Terminating ec2 instance...")
    elif opt==4:
        print("Goodbye")
        sys.exit()
    else:
        print("Your input is invalid. Try again.")
