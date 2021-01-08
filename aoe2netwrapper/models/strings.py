"""
aoe2netwrapper.models.strings
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/strings
"""
from typing import List

from pydantic import BaseModel


class AgeString(BaseModel):
    id: int
    string: str


class CivilizationString(BaseModel):
    id: int
    string: str


class GameTypeString(BaseModel):
    id: int
    string: str


class LeaderBoardString(BaseModel):
    id: int
    string: str


class MapSizeString(BaseModel):
    id: int
    string: str


class MapTypeString(BaseModel):
    id: int
    string: str


class RatingTypeString(BaseModel):
    id: int
    string: str


class ResourcesString(BaseModel):
    id: int
    string: str


class SpeedString(BaseModel):
    id: int
    string: str


class VictoryString(BaseModel):
    id: int
    string: str


class VisibilityString(BaseModel):
    id: int
    string: str


class StringsResponse(BaseModel):
    language: str
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
