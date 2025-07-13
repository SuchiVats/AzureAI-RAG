# import libraries
import os
from config.load_config import AZURE_FORM_RECOGNIZER_KEY, AZURE_FORM_RECOGNIZER_ENDPOINT

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Create a DocumentAnalysisClient
client = DocumentAnalysisClient(endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT, credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY))

# create a funtion save a document in text format
def analyze_layout(document_directory, extracted_directory="./extracted"):
    """Analyze the layout of a document using Azure Form Recognizer."""
    os.makedirs(extracted_directory, exist_ok=True)

    #create a list of documents in the directory
    documents = [f for f in os.listdir(document_directory) if os.path.isfile(os.path.join(document_directory, f))]

    # Read documents one by one and convert in text file using azure document intelligence
    for document in documents:
        document_path = os.path.join(document_directory, document)
        with open(document_path, "rb") as doc_file:
            
            poller = client.begin_analyze_document("prebuilt-read", doc_file)
            # print(poller.result())  # Wait for the operation to complete
            result = poller.result()

            # Save the extracted text to a file

            extracted_file_path = os.path.join(extracted_directory, f"{os.path.splitext(document)[0]}.txt")
            with open(extracted_file_path, "w", encoding="utf-8") as extracted_file:
                complete_data = []
                for page in result.pages:
                    for line in page.lines:
                        data = line.content
                        complete_data.append(data)
                extracted_file.write(" ".join(complete_data))
          
            print(f"Extracted text saved to {extracted_file_path}")
            print(f"Processed document: {document}")
            print("-" * 40)
    print("All documents processed successfully.")

