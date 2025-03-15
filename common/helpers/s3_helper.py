import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from common.helpers.constants import DocumentTypes
from frac_prop import settings


class S3BucketHelper:
    def __init__(self):
        self.region_name = settings.AWS_S3_REGION_NAME

    @staticmethod
    def get_s3_connection():
        try:
            client = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_S3_REGION_NAME,
            )
            return client
        except ClientError as e:
            raise RuntimeError(f"Failed to create S3 client: {e}")

    def generate_presigned_url(
        self,
        object_key,
        expiration=3600,
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
    ):
        """
        Generate a pre-signed URL for an S3 object.

        :param bucket_name: Name of the S3 bucket.
        :param object_key: Key (path) of the file in the bucket.
        :param expiration: Time in seconds for the pre-signed URL to remain valid (default: 1 hour).
        :return: Pre-signed URL as a string, or None if an error occurred.
        """
        s3_client = self.get_s3_connection()
        try:
            presigned_url = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": bucket_name, "Key": object_key},
                ExpiresIn=expiration,
            )

        except ClientError as e:
            return None

        return presigned_url

    @staticmethod
    def get_s3_bucket(bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        try:
            client = S3BucketHelper.get_s3_connection()
            return client.Bucket(bucket_name)
        except ClientError as e:
            raise RuntimeError(f"Failed to access S3 bucket: {e}")

    def get_file(self, key, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        try:
            client = self.get_s3_connection()
            obj = client.get_object(Bucket=bucket_name, Key=key)
            return obj
        except ClientError as e:
            raise RuntimeError(f"Failed to get object from S3: {e}")

    def get_s3_url(self, key, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        region_name = self.region_name
        if region_name == "ap-south-1":
            return f"https://{bucket_name}.s3.amazonaws.com/{key}"
        else:
            return f"https://{bucket_name}.s3.{self.region_name}.amazonaws.com/{key}"

    def upload_file_to_s3(
        self,
        file,
        key,
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        file_type=DocumentTypes().PROPERTY_IMAGE,
    ):
        try:
            client = self.get_s3_connection()
            key = f"prod/{file_type.lower()}s/" + key

            if isinstance(file, bytes):
                response = client.put_object(Body=file, Bucket=bucket_name, Key=key)
            if isinstance(file, str):
                response = client.upload_file(file, bucket_name, key)

            file_url = self.get_s3_url(key, bucket_name)
            return {"Location": file_url, "ResponseMetadata": response}

        except ClientError as e:
            raise RuntimeError(f"Failed to upload file to S3: {e}")
        except TypeError as e:
            raise RuntimeError(f"Invalid type for file_name: {e}")

    def delete_file_from_s3(
        self,
        key,
        bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
        file_type=DocumentTypes().PROPERTY_IMAGE,
    ):
        """
        Delete a file from the S3 bucket.

        Args:
            key (str): The key (path) of the file to delete in the S3 bucket.
            bucket_name (str): The name of the S3 bucket.

        Returns:
            dict: A response indicating success or failure.
        """
        try:
            key = f"prod/{file_type.lower()}s/" + key
            client = self.get_s3_connection()
            response = client.delete_object(Bucket=bucket_name, Key=key)
            return {
                "Message": "File deleted successfully",
                "ResponseMetadata": response,
            }
        except ClientError as e:
            raise RuntimeError(f"Failed to delete object from S3: {e}")
