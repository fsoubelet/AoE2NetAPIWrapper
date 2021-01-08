"""
aoe2netwrapper.models.strings
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/strings
"""
from typing import List

from pydantic import BaseModel


class AgeString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class CivilizationString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class GameTypeString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class LeaderBoardString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class MapSizeString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class MapTypeString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class RatingTypeString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class ResourcesString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class SpeedString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class VictoryString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class VisibilityString(BaseModel):
    id: Optional[int] = Field(...)
    string: Optional[str] = Field(...)


class StringsResponse(BaseModel):
    language: Optional[str] = Field(...)
    age: List[AgeString]
    civ: List[CivilizationString]
    game_type: List[GameTypeString]
    leaderboard: List[LeaderBoardString]
    map_size: List[MapSizeString]
    map_type: List[MapTypeString]
    rating_type: List[RatingTypeString]
    resources: List[ResourcesString]
    speed: List[SpeedString]
    victory: List[VictoryString]
    visibility: List[VisibilityString]
