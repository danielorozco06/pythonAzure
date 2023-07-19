"""
Utils to process information
"""
from collections import defaultdict
import base64
import re
import datetime
import os


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


def sort_inventory(inventory: dict[str, list[str]]) -> str:
    """
    Sort by the number of files per extension.
    """
    sorted_inventory = sorted(
        inventory.items(), key=lambda item: len(item[1]), reverse=True
    )

    result = ""
    for extension, files in sorted_inventory:
        result += f"Extension {extension} -> {len(files)} files\n"
    return result


def write_to_file(data: str) -> None:
    """
    Writes the given data to a file in the 'inventories/' directory. The file's name is the current date.
    """
    # Ensure the 'inventories/' directory exists
    if not os.path.exists("inventories"):
        os.makedirs("inventories")

    filename = datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    filepath = os.path.join("inventories", filename)

    with open(filepath, "w") as f:
        f.write(data)
