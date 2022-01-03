from django.shortcuts import render

import boto3
import boto3.session

print("Hiiii")

my_session = boto3.session.Session()

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

