import pulumi
import pulumi_aws as aws
import random
import string

def generate_random_bucket_name(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

bucket_name = generate_random_bucket_name()

# Create an AWS S3 bucket
s3_bucket = aws.s3.Bucket(bucket_name)

# Export the name of the bucket
pulumi.export('bucket_name', s3_bucket.id)
