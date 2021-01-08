"""
aoe2netwrapper.models.strings
-----------------------------

This module contains the model objects to encapsulate the responses from the endpoint at
https://aoe2.net/api/strings
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class AgeString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class CivilizationString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class GameTypeString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class LeaderBoardString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class MapSizeString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class MapTypeString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class RatingTypeString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class ResourcesString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class SpeedString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class VictoryString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class VisibilityString(BaseModel):
    id: Optional[int] = Field(None)
    string: Optional[str] = Field(None)


class StringsResponse(BaseModel):
    language: Optional[str] = Field(None)
    age: Optional[List[AgeString]] = Field(None)
    civ: Optional[List[CivilizationString]] = Field(None)
    game_type: Optional[List[GameTypeString]] = Field(None)
    leaderboard: Optional[List[LeaderBoardString]] = Field(None)
    map_size: Optional[List[MapSizeString]] = Field(None)
    map_type: Optional[List[MapTypeString]] = Field(None)
    rating_type: Optional[List[RatingTypeString]] = Field(None)
    resources: Optional[List[ResourcesString]] = Field(None)
    speed: Optional[List[SpeedString]] = Field(None)
    victory: Optional[List[VictoryString]] = Field(None)
    visibility: Optional[List[VisibilityString]] = Field(None)
