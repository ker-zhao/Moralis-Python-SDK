# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_streams import schemas  # noqa: F401


class HistoryModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "streamId",
            "tinyPayload",
            "errorMessage",
            "id",
            "tag",
            "webhookUrl",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['UUID']:
                return UUID
            date = schemas.DateTimeSchema
        
            @staticmethod
            def tinyPayload() -> typing.Type['WebhookTypesITinyPayload']:
                return WebhookTypesITinyPayload
            errorMessage = schemas.StrSchema
            webhookUrl = schemas.StrSchema
            streamId = schemas.StrSchema
            tag = schemas.StrSchema
        
            @staticmethod
            def payload() -> typing.Type['WebhookTypesIWebhookUnParsed']:
                return WebhookTypesIWebhookUnParsed
            __annotations__ = {
                "id": id,
                "date": date,
                "tinyPayload": tinyPayload,
                "errorMessage": errorMessage,
                "webhookUrl": webhookUrl,
                "streamId": streamId,
                "tag": tag,
                "payload": payload,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    date: MetaOapg.properties.date
    streamId: MetaOapg.properties.streamId
    tinyPayload: 'WebhookTypesITinyPayload'
    errorMessage: MetaOapg.properties.errorMessage
    id: 'UUID'
    tag: MetaOapg.properties.tag
    webhookUrl: MetaOapg.properties.webhookUrl
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streamId"]) -> MetaOapg.properties.streamId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tinyPayload"]) -> 'WebhookTypesITinyPayload': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'UUID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> 'WebhookTypesIWebhookUnParsed': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date"], typing_extensions.Literal["streamId"], typing_extensions.Literal["tinyPayload"], typing_extensions.Literal["errorMessage"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["webhookUrl"], typing_extensions.Literal["payload"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streamId"]) -> MetaOapg.properties.streamId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tinyPayload"]) -> 'WebhookTypesITinyPayload': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'UUID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union['WebhookTypesIWebhookUnParsed', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date"], typing_extensions.Literal["streamId"], typing_extensions.Literal["tinyPayload"], typing_extensions.Literal["errorMessage"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["webhookUrl"], typing_extensions.Literal["payload"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, datetime, ],
        streamId: typing.Union[MetaOapg.properties.streamId, str, ],
        tinyPayload: 'WebhookTypesITinyPayload',
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, ],
        id: 'UUID',
        tag: typing.Union[MetaOapg.properties.tag, str, ],
        webhookUrl: typing.Union[MetaOapg.properties.webhookUrl, str, ],
        payload: typing.Union['WebhookTypesIWebhookUnParsed', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'HistoryModel':
        return super().__new__(
            cls,
            *_args,
            date=date,
            streamId=streamId,
            tinyPayload=tinyPayload,
            errorMessage=errorMessage,
            id=id,
            tag=tag,
            webhookUrl=webhookUrl,
            payload=payload,
            _configuration=_configuration,
        )

from openapi_streams.model.uuid import UUID
from openapi_streams.model.webhook_types_i_tiny_payload import WebhookTypesITinyPayload
from openapi_streams.model.webhook_types_i_webhook_un_parsed import WebhookTypesIWebhookUnParsed
