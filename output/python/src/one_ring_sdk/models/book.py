# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Book(BaseModel):
    """Book

    :param _id: The unique identifier of the book (string)., defaults to None
    :type _id: str, optional
    :param name: The name of the book (string)., defaults to None
    :type name: str, optional
    """

    def __init__(self, _id: str = SENTINEL, name: str = SENTINEL, **kwargs):
        """Book

        :param _id: The unique identifier of the book (string)., defaults to None
        :type _id: str, optional
        :param name: The name of the book (string)., defaults to None
        :type name: str, optional
        """
        if _id is not SENTINEL:
            self._id = _id
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
