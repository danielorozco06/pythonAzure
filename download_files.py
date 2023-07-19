"""
Module to download different types of files from azure repository
"""

import requests
import os
import base64
import json


def remove_first_char(path: str) -> str:
    """
    Removes the first character from a string if it's a forward slash ('/').
    """
    if path.startswith("/"):
        return path[1:]
    else:
        return path


def download_file_from_azure_repo(
    organization: str,
    project: str,
    repository: str,
    pat: str,
    path_file: str,
    file_extensions_allowed: list[str],
) -> None:
    """
    Function to download files from azure repositoy
    """

    authorization = str(base64.b64encode(bytes(":" + pat, "ascii")), "ascii")
    headers = {
        "Accept": "application/json",
        "Authorization": "Basic " + authorization,
    }

    # Check if the file extension is allowed
    extension = os.path.splitext(path_file)[1].lower()
    if extension not in [ext.lower() for ext in file_extensions_allowed]:
        print(f"File extension {extension} not allowed.")
        return

    # Prepare the URL
    api_url = (
        f"https://{organization}/{project}/_apis/git/repositories/{repository}/items"
        f"?path={path_file}&api-version=5.0&download=true&includeContent=true"
    )

    # Make the request
    response = requests.get(api_url, headers=headers, stream=True)

    # Remove the first character from the path_file
    path_file = remove_first_char(path_file)

    full_path = os.path.join("repository", path_file)
    path = os.path.dirname(full_path)

    # Check if the request was successful
    if response.status_code == 200:
        # Create directories in the path if they don't exist
        os.makedirs(path, exist_ok=True)

        # open method to open a file on your system and write the contents
        with open(full_path, "wb") as file:
            file.write(response.content)

        data = json.loads(response.text)
        content = data.get("content", "")

        # Save content to a file
        with open(full_path, "w") as file:
            file.write(content)

    else:
        print(f"Failed to download file. Status code: {response.status_code}")


# Get the environment variables
organization = os.getenv("ORGANIZATION")
project = os.getenv("PROJECT")
pat = os.getenv("PAT")

# Use the function
download_file_from_azure_repo(
    organization=organization,
    project=project,
    repository="1b927269-b4fe-422e-bbb7-6c60f64a9938",
    pat=pat,
    path_file="/Lineamientos-Areas-Transversales-de-TI/DevOps/AI-for-Devs/Pull-Request-Verifier.md",
    file_extensions_allowed=[".md"],
)
