# coding: utf-8

"""
    Image Upload API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class ImagesGet200ResponseImagesInner(BaseModel):
    """
    ImagesGet200ResponseImagesInner
    """
    url: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    __properties = ["url", "name"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ImagesGet200ResponseImagesInner:
        """Create an instance of ImagesGet200ResponseImagesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImagesGet200ResponseImagesInner:
        """Create an instance of ImagesGet200ResponseImagesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImagesGet200ResponseImagesInner.parse_obj(obj)

        _obj = ImagesGet200ResponseImagesInner.parse_obj({
            "url": obj.get("url"),
            "name": obj.get("name")
        })
        return _obj

