from app.ingestion.blob_operations import upload_blob, download_blob
from app.ingestion.text_extracter import analyze_layout
from app.data_preprocessing.chunker import split_sentences_spacy

if __name__ == "__main__":  
    # upload_blob(file_path="AirIndiaPlaneCrashReport.pdf")
    # download_blob(container_name="rag-container", download_directory="./Downloads")
    # analyze_layout(document_directory="Downloads", extracted_directory="./extracted")
    chunked_text = split_sentences_spacy(input_directory="/Users/pardeepkaushik/Desktop/AzureAI-RAG/extracted")
    