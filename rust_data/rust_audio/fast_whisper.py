import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Directory containing the mp3 files
source_dir = './jonhoo'

# Directory to save the transcriptions
target_dir = './jonhoo_transcriptions'

logging.info(f"Source directory: {source_dir}")
logging.info(f"Target directory: {target_dir}")

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)
logging.info(f"Ensured target directory exists")

# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file is an mp3
    if filename.endswith('.mp3'):
        # Construct the full path to the file
        file_path = os.path.join(source_dir, filename)
        logging.info(f"Processing file: {file_path}")

        # Construct the command to run
        command = ['insanely-fast-whisper', '--file-name', file_path]
        logging.info(f"Command: {' '.join(command)}")

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Log the output
        logging.info(f"Command output: {result.stdout}")
        logging.error(f"Command error: {result.stderr}")
