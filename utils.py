"""
Utils to process information
"""
import base64


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
