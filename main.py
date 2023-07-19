"""
Main file to orchestrate logic
"""

from azure import get_response
from utils import get_repo_id, get_path_files, get_authorization_header
from urls import create_url_repo_info, create_url_repo_items
import os

# Get the environment variables
organization = os.getenv("ORGANIZATION")
project = os.getenv("PROJECT")
pat = os.getenv("PAT")

# Set variables
repo_name = "ISXXX0001"
branch = "master"
headers = get_authorization_header(pat)

# Repo id
url_repo_info = create_url_repo_info(organization, project, repo_name)
repo_info = get_response(url_repo_info, headers)
repo_id = get_repo_id(repo_info)
print(f"\nRepository name = {repo_name}")
print(f"Repostiry id = {repo_id}")

# Repo files
url_repo_items = create_url_repo_items(organization, project, repo_id, branch)
repo_items = get_response(url_repo_items, headers)
files = get_path_files(repo_items)
print(f"\nFiles number: {len(files)}")
print(f"Files list: {files}")
