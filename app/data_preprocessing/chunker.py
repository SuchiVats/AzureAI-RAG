"""This module contains functions for chunking text files into smaller segments after cleaning the text.
It uses the SpaCy library for natural language processing to split text into sentences.
It will create a directory of all the text files in the input directory and process each file to extract sentences.
Directry key will be the file name and value will be the list of sentences."""


import spacy
import os

def clean_text(text: str) -> str:
    """
    Cleans the input text by removing extra spaces and newlines and ">"
    
    Parameters:
    text (str): The input text to be cleaned.
    
    Returns:
    str: The cleaned text.
    """
    cleaned_text = ' '.join(text.split())
    cleaned_text = cleaned_text.replace("➢", "")
    return cleaned_text

def split_sentences_spacy(input_directory: str):
    """
    Splits text files into sentences using SpaCy NLP library.
    
    Parameters:
    input_directory (str): The directory containing text files to be processed.
    
    Returns:
    dict: A dictionary where keys are file names and values are lists of sentences.
    """
    
    nlp = spacy.load('en_core_web_sm')
    sentences_dict = {}

    for file in os.listdir(input_directory):
        if file.endswith(".txt"):
            input_path = os.path.join(input_directory, file)
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()

            # Process the text
            doc = nlp(clean_text(text))
            
            # Extract sentences
            sentences = [sent.text for sent in doc.sents]
            sentences_dict[file] = sentences
        else:
            raise ValueError("No .txt file found in the specified directory.")
    # print(sentences_dict)
    # print(f"Number of files processed: {len(sentences_dict)}")
        
    return sentences_dict

