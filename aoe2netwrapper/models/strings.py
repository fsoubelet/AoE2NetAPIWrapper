"""
aoe2netwrapper.models.strings
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/strings

Any confusing with a specific attribute being an INTEGER in the models can be cleared by checking the
corresponding string the API / system attributes to this ID.
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class AgeString(BaseModel):
    """An object to encapsulate any entry for the available age strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'age' ID")


class CivilizationString(BaseModel):
    """An object to encapsulate any entry for the available civilization strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'civ' ID")


class GameTypeString(BaseModel):
    """An object to encapsulate any entry for the available game type strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'game_type' ID")


class LeaderBoardString(BaseModel):
    """An object to encapsulate any entry for the available leaderboard strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'leaderboard' ID")


class MapSizeString(BaseModel):
    """An object to encapsulate any entry for the available map size strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'map_size' ID")


class MapTypeString(BaseModel):
    """An object to encapsulate any entry for the available map type strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'map_type' ID")


class RatingTypeString(BaseModel):
    """An object to encapsulate any entry for the available rating type strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'rating_type' ID")


class ResourcesString(BaseModel):
    """An object to encapsulate any entry for the available resources strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'resources' ID")


class SpeedString(BaseModel):
    """An object to encapsulate any entry for the available speed strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'speed' ID")


class VictoryString(BaseModel):
    """An object to encapsulate any entry for the available victory strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'victory' ID")


class VisibilityString(BaseModel):
    """An object to encapsulate any entry for the available visibiliity strings and their respective IDs."""

    id: Optional[int] = Field(None, description="ID for this specific string value")
    string: Optional[str] = Field(None, description="String value for this specific 'visibility' ID")


class StringsResponse(BaseModel):
    """An object to encapsulate the response from the strings API endpoint."""

    language: Optional[str] = Field(None, description="Language of the returned strings")
    age: Optional[List[AgeString]] = Field(None, description="List of all strings and their IDs for ages")
    civ: Optional[List[CivilizationString]] = Field(
        None, description="List of all strings and their IDs for civilizations"
    )
    game_type: Optional[List[GameTypeString]] = Field(
        None, description="List of all strings and their IDs for game types"
    )
    leaderboard: Optional[List[LeaderBoardString]] = Field(
        None, description="List of all strings and their IDs for leaderboards"
    )
    map_size: Optional[List[MapSizeString]] = Field(
        None, description="List of all strings and their IDs for map sizes"
    )
    map_type: Optional[List[MapTypeString]] = Field(
        None, description="List of all strings and their IDs for map types"
    )
    rating_type: Optional[List[RatingTypeString]] = Field(
        None, description="List of all strings and their IDs for rating types"
    )
    resources: Optional[List[ResourcesString]] = Field(
        None, description="List of all strings and their IDs for resources"
    )
    speed: Optional[List[SpeedString]] = Field(
        None, description="List of all strings and their IDs for game speeds"
    )
    victory: Optional[List[VictoryString]] = Field(
        None, description="List of all strings and their IDs for victory types"
    )
    visibility: Optional[List[VisibilityString]] = Field(
        None, description="List of all strings and their IDs for visibility"
    )
