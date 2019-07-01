import os
import boto3

s3 = boto3.resource('s3')
root_dir = '/Users/george/Downloads/images/'
s3_uploaded_root = 'images'

for (path, dirs, files) in os.walk(root_dir):
    for file in files:
        fullPath = os.path.join(path, file)
        print('uploading...' + fullPath)
        s3path = os.path.join(s3_uploaded_root, fullPath.replace(
            root_dir, '')).strip('/')
        s3.meta.client.upload_file(fullPath, 'diann', s3path, ExtraArgs={'ACL': 'public-read'})
        print('done!')
