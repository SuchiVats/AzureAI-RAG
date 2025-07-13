from app.ingestion.blob_operations import upload_blob, download_blob
from app.ingestion.text_extracter import analyze_layout

if __name__ == "__main__":  
    # upload_blob(file_path="AirIndiaPlaneCrashReport.pdf")
    download_blob(container_name="rag-container", download_directory="./Downloads")
    analyze_layout(document_directory="Downloads", extracted_directory="./extracted")
