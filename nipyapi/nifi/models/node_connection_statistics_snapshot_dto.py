# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.12.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NodeConnectionStatisticsSnapshotDTO(object):
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
        'node_id': 'str',
        'address': 'str',
        'api_port': 'int',
        'statistics_snapshot': 'ConnectionStatisticsSnapshotDTO'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'address': 'address',
        'api_port': 'apiPort',
        'statistics_snapshot': 'statisticsSnapshot'
    }

    def __init__(self, node_id=None, address=None, api_port=None, statistics_snapshot=None):
        """
        NodeConnectionStatisticsSnapshotDTO - a model defined in Swagger
        """

        self._node_id = None
        self._address = None
        self._api_port = None
        self._statistics_snapshot = None

        if node_id is not None:
          self.node_id = node_id
        if address is not None:
          self.address = address
        if api_port is not None:
          self.api_port = api_port
        if statistics_snapshot is not None:
          self.statistics_snapshot = statistics_snapshot

    @property
    def node_id(self):
        """
        Gets the node_id of this NodeConnectionStatisticsSnapshotDTO.
        The unique ID that identifies the node

        :return: The node_id of this NodeConnectionStatisticsSnapshotDTO.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this NodeConnectionStatisticsSnapshotDTO.
        The unique ID that identifies the node

        :param node_id: The node_id of this NodeConnectionStatisticsSnapshotDTO.
        :type: str
        """

        self._node_id = node_id

    @property
    def address(self):
        """
        Gets the address of this NodeConnectionStatisticsSnapshotDTO.
        The API address of the node

        :return: The address of this NodeConnectionStatisticsSnapshotDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this NodeConnectionStatisticsSnapshotDTO.
        The API address of the node

        :param address: The address of this NodeConnectionStatisticsSnapshotDTO.
        :type: str
        """

        self._address = address

    @property
    def api_port(self):
        """
        Gets the api_port of this NodeConnectionStatisticsSnapshotDTO.
        The API port used to communicate with the node

        :return: The api_port of this NodeConnectionStatisticsSnapshotDTO.
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """
        Sets the api_port of this NodeConnectionStatisticsSnapshotDTO.
        The API port used to communicate with the node

        :param api_port: The api_port of this NodeConnectionStatisticsSnapshotDTO.
        :type: int
        """

        self._api_port = api_port

    @property
    def statistics_snapshot(self):
        """
        Gets the statistics_snapshot of this NodeConnectionStatisticsSnapshotDTO.
        The connection status snapshot from the node.

        :return: The statistics_snapshot of this NodeConnectionStatisticsSnapshotDTO.
        :rtype: ConnectionStatisticsSnapshotDTO
        """
        return self._statistics_snapshot

    @statistics_snapshot.setter
    def statistics_snapshot(self, statistics_snapshot):
        """
        Sets the statistics_snapshot of this NodeConnectionStatisticsSnapshotDTO.
        The connection status snapshot from the node.

        :param statistics_snapshot: The statistics_snapshot of this NodeConnectionStatisticsSnapshotDTO.
        :type: ConnectionStatisticsSnapshotDTO
        """

        self._statistics_snapshot = statistics_snapshot

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
        if not isinstance(other, NodeConnectionStatisticsSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
