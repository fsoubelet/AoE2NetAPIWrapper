"""
aoe2netwrapper.exceptions
-------------------------
This module contains the set of exceptions used in the package.
"""


class Aoe2NetError(Exception):
    """Default exception for AoE2.net API interaction."""


class RemovedApiEndpointError(Exception):
    """Exception raised when an API endpoint is removed from AoE2.net."""

    def __init__(self, endpoint: str) -> None:
        msg = f"The API endpoint for '{endpoint}' has been removed from AoE2.net."
        super().__init__(msg)


class NightBotError(Exception):
    """Default exception for AoE2.net Nightbot API interaction."""
