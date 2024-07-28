import datetime
import logging
import os
from azure.storage.blob import BlobServiceClient
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Azure Blob Cleanup function started')

    # Retrieve the storage account connection string from an environment variable
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # Name of the container
    container_name = "uploads"

    # Initialize the BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    # Expiration period 
    expiry_days = 30
    now = datetime.datetime.utcnow()
    expired_time = now - datetime.timedelta(days=expiry_days)

    # Iterate through the blobs in the container
    for blob in container_client.list_blobs():
        # Check if the blob's last modified date is older than the expiration period
        if blob.last_modified < expired_time:
            # Delete the expired blob
            container_client.delete_blob(blob.name)
            logging.info(f"Deleted blob: {blob.name}")

    logging.info('Azure Blob Cleanup function completed')
