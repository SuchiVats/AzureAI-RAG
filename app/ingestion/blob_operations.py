"""This module is responsible for downloading a blob from an Azure storage container to a download directory."""
import os
from azure.storage.blob import BlobServiceClient
from config.load_config import AZURE_STORAGE_CONNECTION_STRING

 # Ensure the connection string is available
if not AZURE_STORAGE_CONNECTION_STRING:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set in the environment variables.")

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_blob(file_path):
    """Uploads a file to an Azure Blob Storage container."""
   
    # Create a file in the local data directory to upload and download
    upload_file_path = file_path
    container_name = "rag-container"

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=upload_file_path)
    print("\nUploading to Azure Storage as blob:\n\t" + upload_file_path)

    # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)

def list_blobs(container_name):
    """Lists all blobs in an Azure Blob Storage container."""
    container_client = blob_service_client.get_container_client(container=container_name)
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    return blob_list


def download_blob(container_name, download_directory):
    os.makedirs(download_directory, exist_ok=True)
    # Download the blob to a local file
    # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
    container_client = blob_service_client.get_container_client(container= container_name) 
    blob_list = list_blobs(container_name)
    print("\nDownloading blob to \n\t" + download_directory)

    for blob in container_client.list_blobs():
        download_file_path = os.path.join(download_directory, blob.name)
        print("\t" + download_file_path)

        # Download the blob to a file
        with open(file=download_file_path, mode="wb") as download_file:
            download_file.write(container_client.download_blob(blob.name).readall())
        






   