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


class FDRevision(object):
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
        'client_id': 'str',
        'version': 'int',
        'last_modifier': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'version': 'version',
        'last_modifier': 'lastModifier'
    }

    def __init__(self, client_id=None, version=None, last_modifier=None):
        """
        FDRevision - a model defined in Swagger
        """

        self._client_id = None
        self._version = None
        self._last_modifier = None

        if client_id is not None:
          self.client_id = client_id
        if version is not None:
          self.version = version
        if last_modifier is not None:
          self.last_modifier = last_modifier

    @property
    def client_id(self):
        """
        Gets the client_id of this FDRevision.
        A client identifier used to make a request. By including a client identifier, the API can allow multiple requests without needing the current revision. Due to the asynchronous nature of requests/responses this was implemented to allow the client to make numerous requests without having to wait for the previous response to come back

        :return: The client_id of this FDRevision.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this FDRevision.
        A client identifier used to make a request. By including a client identifier, the API can allow multiple requests without needing the current revision. Due to the asynchronous nature of requests/responses this was implemented to allow the client to make numerous requests without having to wait for the previous response to come back

        :param client_id: The client_id of this FDRevision.
        :type: str
        """

        self._client_id = client_id

    @property
    def version(self):
        """
        Gets the version of this FDRevision.
        C2 Flow Designer employs an optimistic locking strategy where the client must include a revision in their request when performing an update. In a response to a mutable flow request, this field represents the updated base version.

        :return: The version of this FDRevision.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FDRevision.
        C2 Flow Designer employs an optimistic locking strategy where the client must include a revision in their request when performing an update. In a response to a mutable flow request, this field represents the updated base version.

        :param version: The version of this FDRevision.
        :type: int
        """

        self._version = version

    @property
    def last_modifier(self):
        """
        Gets the last_modifier of this FDRevision.
        The user that last modified the flow.

        :return: The last_modifier of this FDRevision.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        """
        Sets the last_modifier of this FDRevision.
        The user that last modified the flow.

        :param last_modifier: The last_modifier of this FDRevision.
        :type: str
        """

        self._last_modifier = last_modifier

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
        if not isinstance(other, FDRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
