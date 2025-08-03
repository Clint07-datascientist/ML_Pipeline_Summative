# src/api/utils.py

import os
from typing import List
from fastapi import UploadFile
import shutil

def save_upload_file(upload_file: UploadFile, destination: str) -> str:
    """
    Save a single uploaded file to the given destination directory.
    Returns the full path to the saved file.
    """
    os.makedirs(destination, exist_ok=True)
    file_path = os.path.join(destination, upload_file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path


def save_bulk_files(files: List[UploadFile], destination: str) -> List[str]:
    """
    Save multiple uploaded files to the destination directory.
    Returns a list of saved file paths.
    """
    saved_paths = []
    for file in files:
        path = save_upload_file(file, destination)
        saved_paths.append(path)
    return saved_paths


def clear_directory(folder_path: str):
    """
    Deletes all files in a directory.
    Useful for cleaning temp upload folders after processing.
    """
    if not os.path.exists(folder_path):
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
