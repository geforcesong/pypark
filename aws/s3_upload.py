import boto3

# list all bucket names
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# simple upload
with open('/Users/george/Downloads/house.jpeg', 'rb') as f:
    s3.Bucket('diann').put_object(Key='house.jpeg', Body=f)

# upload and make it upload
bucketName = 'diann'
s3key='house_public.jpeg'
with open('/Users/george/Downloads/house.jpeg', 'rb') as f:
    s3.Bucket(bucketName).put_object(Key=s3key, Body=f)
object_acl = s3.ObjectAcl(bucketName,s3key)
object_acl.put(ACL='public-read')
