"""
This module provides a function to construct URLs
"""


def create_url_repo_items(
    organization: str, project: str, repo_id: str, branch: str
) -> str:
    """
    Constructs a URL for accessing items in a specific repository of a project within an organization.
    """
    return (
        f"https://{organization}/{project}/_apis/git/repositories/{repo_id}/items"
        "?scopePath=/&recursionLevel=Full"
        "&versionDescriptor[versionOption]=0"
        f"&versionDescriptor[version]={branch}"
        "&versionDescriptor[versionType]=0"
        "&includeContentMetadata=true&api-version=6.0"
    )


def create_url_repo_info(organization: str, project: str, repo_name: str) -> str:
    """
    Constructs the URL for a specific repository in an Azure DevOps project.
    """
    return f"https://{organization}/{project}/_apis/git/repositories/{repo_name}?api-version=6.0"
