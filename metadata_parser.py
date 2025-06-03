# forensics/metadata_parser.py
import os
import datetime

def extract_file_metadata(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    stats = os.stat(file_path)
    metadata = {
        'size': stats.st_size,
        'last_modified': datetime.datetime.fromtimestamp(stats.st_mtime),
        'created': datetime.datetime.fromtimestamp(stats.st_ctime),
    }
    return metadata
