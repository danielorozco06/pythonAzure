"""
This module is used to requesto to azure devops API
"""
import requests
import logging


def get_response(api_url: str, headers: dict[str, str]) -> dict[any]:
    """
    Sends a GET request to the specified API URL and returns the response.
    """
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"\n{e}\n")
        raise
