#!/bin/bash

## had to do manually because it requires a login

base_url="https://huggingface.co/datasets/bigcode/the-stack-dedup/resolve/main/data/rust/data-"
middle_part="-of-00021.parquet?download=true"
destination_folder="../rust_data"

# Ensure the destination folder exists
mkdir -p $destination_folder

# Loop through the file numbers you want to download
for i in {2..20}
do
    # Format the number to be 5 digits long, filled with zeros
    formatted_number=$(printf "%05d" $i)

    # Create the full URL for this file
    file_url="${base_url}${formatted_number}${middle_part}"

    # Download the file
    wget -O "${destination_folder}/data-${formatted_number}-of-00021.parquet" "$file_url"
done
