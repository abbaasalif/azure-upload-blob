import csv
from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient
# pip install azure-storage-file-share
# Azure account details
account_name = 'muonstore'
account_key = 'yteVBSIEU/t4ea1hplohb1eGRITE6ADm1Lpnw9MysRpkKtqzVRtodgik/kN93EP6tGMIL9Ff8J+o+ASt8d/Vfg=='
file_share_name = 'muon-data'
directory_name = 'new_dir'  # You can use an empty string if there's no specific directory
file_name = 'sample.csv'

# Ensure the directory exists
directory_client = ShareDirectoryClient(account_url=f"https://{account_name}.file.core.windows.net",
                                        share_name=file_share_name,
                                        directory_path=directory_name,
                                        credential=account_key)

if not directory_client.exists():
    directory_client.create_directory()

# Construct the full path for the file within the directory
full_path = directory_name + '/' + file_name if directory_name else file_name

# Upload CSV file to Azure File Share
file_client = ShareFileClient(account_url=f"https://{account_name}.file.core.windows.net",
                               share_name=file_share_name,
                               file_path=full_path,
                               credential=account_key)

with open(file_name, "rb") as source_file:
    file_client.upload_file(source_file)

print(f"{file_name} uploaded to Azure File Share in directory {directory_name}!")
