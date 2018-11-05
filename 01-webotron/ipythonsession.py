# coding: utf-8
import boto3
get_ipython().run_line_magic('cat', '~/ .aws/config')
get_ipython().run_line_magic('cat', '~/.aws/config')
get_ipython().run_line_magic('cat', '~/.aws/config')
get_ipython().run_line_magic('cat', '~/.aws/config')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('pwd', '')
aws s3 mb s3://automatingawsmadux-cli
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('history', '')
s3.create_bucket(Bucket='automatingawsmadux-boto3', CreateBucketConfiguration={'LocationConstraint': us-east-2})
new_bucket = s3.create_bucket(Bucket='automatingawsmadux-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('history', '')
