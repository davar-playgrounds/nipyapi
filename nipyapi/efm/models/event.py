# coding: utf-8

"""
    Cloudera Edge Flow Manager REST API

    This REST API provides remote access to the EFM Server.                                             Endpoints that are marked as [BETA] are subject to change in future releases of the application without backwards compatibility and without a major version change.

    OpenAPI spec version: 1.0.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Event(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'level': 'str',
        'event_type': 'str',
        'message': 'str',
        'created': 'int',
        'event_source': 'ResourceReference',
        'event_detail': 'ResourceReference',
        'agent_class': 'str',
        'tags': 'dict(str, str)',
        'links': 'EventLinks'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'event_type': 'eventType',
        'message': 'message',
        'created': 'created',
        'event_source': 'eventSource',
        'event_detail': 'eventDetail',
        'agent_class': 'agentClass',
        'tags': 'tags',
        'links': 'links'
    }

    def __init__(self, id=None, level=None, event_type=None, message=None, created=None, event_source=None, event_detail=None, agent_class=None, tags=None, links=None):
        """
        Event - a model defined in Swagger
        """

        self._id = None
        self._level = None
        self._event_type = None
        self._message = None
        self._created = None
        self._event_source = None
        self._event_detail = None
        self._agent_class = None
        self._tags = None
        self._links = None

        if id is not None:
          self.id = id
        self.level = level
        self.event_type = event_type
        if message is not None:
          self.message = message
        if created is not None:
          self.created = created
        self.event_source = event_source
        if event_detail is not None:
          self.event_detail = event_detail
        if agent_class is not None:
          self.agent_class = agent_class
        if tags is not None:
          self.tags = tags
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this Event.

        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Event.

        :param id: The id of this Event.
        :type: str
        """

        self._id = id

    @property
    def level(self):
        """
        Gets the level of this Event.

        :return: The level of this Event.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this Event.

        :param level: The level of this Event.
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")
        allowed_values = ["DEBUG", "INFO", "WARN", "ERROR"]
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def event_type(self):
        """
        Gets the event_type of this Event.

        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this Event.

        :param event_type: The event_type of this Event.
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")
        if event_type is not None and len(event_type) > 200:
            raise ValueError("Invalid value for `event_type`, length must be less than or equal to `200`")
        if event_type is not None and len(event_type) < 0:
            raise ValueError("Invalid value for `event_type`, length must be greater than or equal to `0`")

        self._event_type = event_type

    @property
    def message(self):
        """
        Gets the message of this Event.

        :return: The message of this Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Event.

        :param message: The message of this Event.
        :type: str
        """
        if message is not None and len(message) > 8000:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `8000`")
        if message is not None and len(message) < 0:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")

        self._message = message

    @property
    def created(self):
        """
        Gets the created of this Event.

        :return: The created of this Event.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Event.

        :param created: The created of this Event.
        :type: int
        """

        self._created = created

    @property
    def event_source(self):
        """
        Gets the event_source of this Event.

        :return: The event_source of this Event.
        :rtype: ResourceReference
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """
        Sets the event_source of this Event.

        :param event_source: The event_source of this Event.
        :type: ResourceReference
        """
        if event_source is None:
            raise ValueError("Invalid value for `event_source`, must not be `None`")

        self._event_source = event_source

    @property
    def event_detail(self):
        """
        Gets the event_detail of this Event.

        :return: The event_detail of this Event.
        :rtype: ResourceReference
        """
        return self._event_detail

    @event_detail.setter
    def event_detail(self, event_detail):
        """
        Sets the event_detail of this Event.

        :param event_detail: The event_detail of this Event.
        :type: ResourceReference
        """

        self._event_detail = event_detail

    @property
    def agent_class(self):
        """
        Gets the agent_class of this Event.

        :return: The agent_class of this Event.
        :rtype: str
        """
        return self._agent_class

    @agent_class.setter
    def agent_class(self, agent_class):
        """
        Sets the agent_class of this Event.

        :param agent_class: The agent_class of this Event.
        :type: str
        """

        self._agent_class = agent_class

    @property
    def tags(self):
        """
        Gets the tags of this Event.

        :return: The tags of this Event.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Event.

        :param tags: The tags of this Event.
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def links(self):
        """
        Gets the links of this Event.

        :return: The links of this Event.
        :rtype: EventLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Event.

        :param links: The links of this Event.
        :type: EventLinks
        """

        self._links = links

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
