"""
aoe2netwrapper.models.lobbies
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/lobbies
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from aoe2netwrapper.models.lobbies import MatchLobby


class LastMatchResponse(BaseModel):
    """An object to encapsulate the response from the last_match API."""

    profile_id: int | None = Field(None, description="The ID attributed to the player by AoE II")
    steam_id: int | None = Field(None, description="ID of the player on the Steam platform")
    name: str | None = Field(None, description="Name of the player the query was made for")
    country: str | None = Field(None, description="Country the player connected from")
    last_match: MatchLobby | None = Field(None, description="MatchLobby  of the last match")
