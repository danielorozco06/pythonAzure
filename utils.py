"""
Utils to process information
"""
from collections import defaultdict
import base64
import re


def get_authorization_header(pat: str) -> dict[str, str]:
    """
    Generates the authorization header.
    """
    authorization = str(base64.b64encode(bytes(":" + pat, "ascii")), "ascii")
    headers = {
        "Accept": "application/json",
        "Authorization": "Basic " + authorization,
    }
    return headers


def get_path_files(response: any) -> list[str]:
    """
    Retrieves all files from a specified repository in an Azure DevOps project.
    """
    file_paths = []

    # Iterate over each item in the response value
    for item in response["value"]:
        # Check if 'isFolder' key is missing in item dictionary
        if "isFolder" not in item:
            # If it's a file, append its path to the file_paths list
            file_paths.append(item["path"])

    return file_paths


def get_repo_id(response: dict[object]) -> str:
    """
    Extracts the repository ID from the response.
    """
    return response["id"]


def groups_files_by_extension(file_list: list[str]) -> dict[str, list[str]]:
    """
    Groups files by their extension from a given list of file names.
    """
    inventory = defaultdict(list)
    for file in file_list:
        match = re.search(r"\.([a-zA-Z0-9]+)$", file)
        if match:
            extension = match.group(1)
        else:
            extension = "No_Extension"
        inventory[extension].append(file)
    return inventory


def print_sorted_inventory(inventory: dict[str, list[str]]) -> None:
    """
    Prints the inventory of files sorted by the number of files per extension.
    """
    sorted_inventory = sorted(
        inventory.items(), key=lambda item: len(item[1]), reverse=True
    )

    for extension, files in sorted_inventory:
        print(f"Extension {extension} -> {len(files)} files")
