import pulumi
import pulumi_aws as aws

# Create an AWS S3 bucket
s3_bucket = aws.s3.Bucket("my_bucket")

# Export the name of the bucket
pulumi.export('bucket_name', s3_bucket.id)
