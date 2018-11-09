# coding: utf-8

# import s3 session
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

# Create bucket
new_bucket = s3.create_bucket(Bucket='automatingawsmadux', CreateBucketConfiguration={'LocationConstraint': session.region_name})

# Upload index.html file
new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'})  

# Set the bucket policy
# First set the policy document 
policy = """  
    { 
     "Version":"2012-10-17", 
     "Statement":[{ 
     "Sid":"PublicReadGetObject", 
     "Effect":"Allow", 
     "Principal": "*", 
          "Action":["s3:GetObject"], 
          "Resource":["arn:aws:s3:::%s/*" 
          ] 
        } 
      ] 
    } 
    """ % new_bucket.name

# Then use the policy document to set the bucket policy

pol = new_bucket.Policy()
policy = policy.strip() 
pol.put(Policy=policy)
   
   
# Set up website configuration on bucket

ws = new_bucket.Website()

ws.put(WebsiteConfiguration={
   			'ErrorDocument': {
   				'Key': 'error.html'
   				},
   				'IndexDocument': {
   					'Suffix': 'index.html'
   					}})

# Get website address
url = "http://%s.s3-website.us-east-2.amazonaws.com"% new_bucket.name
























