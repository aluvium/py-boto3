#STS - Console - Security Token Service
import boto3

AWS_M_CON=boto3.session.Session(profile_name="root")
STS_CON=AWS_M_CON.client("sts")
response=STS_CON.get_caller_identity()
print(response)

# - - - - - - - - - - - - - - 
# For sepcific keys:
# print(response.get("UserId"))
# print(response["UserId"])
