# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .character import Character


@JsonMap({})
class CharacterResponse(BaseModel):
    """CharacterResponse

    :param docs: docs, defaults to None
    :type docs: List[Character], optional
    """

    def __init__(self, docs: List[Character] = SENTINEL, **kwargs):
        """CharacterResponse

        :param docs: docs, defaults to None
        :type docs: List[Character], optional
        """
        if docs is not SENTINEL:
            self.docs = self._define_list(docs, Character)
        self._kwargs = kwargs
