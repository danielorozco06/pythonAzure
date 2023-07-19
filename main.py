"""
Main file to orchestrate logic
"""

from azure import get_response
from utils import (
    get_repo_id,
    get_path_files,
    get_authorization_header,
    groups_files_by_extension,
    print_sorted_inventory,
)
from urls import create_url_repo_info, create_url_repo_items
import os


def main() -> None:
    """
    Entry function of the project
    """
    # Get the environment variables
    organization = os.getenv("ORGANIZATION")
    project = os.getenv("PROJECT")
    pat = os.getenv("PAT")

    # Set variables
    repo_name = "Vicepresidencia%20Servicios%20de%20Tecnología.wiki"
    branch = "wikiMaster"

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
    print(f"\nTotal files: {len(files)}\n")

    # Inventory of files
    inventory = groups_files_by_extension(files)
    print_sorted_inventory(inventory)


if __name__ == "__main__":
    main()
