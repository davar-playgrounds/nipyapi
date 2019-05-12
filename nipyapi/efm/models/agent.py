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


class Agent(object):
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
        'identifier': 'str',
        'name': 'str',
        'agent_class': 'str',
        'agent_manifest_id': 'str',
        'status': 'AgentStatus',
        'first_seen': 'int',
        'last_seen': 'int'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'agent_class': 'agentClass',
        'agent_manifest_id': 'agentManifestId',
        'status': 'status',
        'first_seen': 'firstSeen',
        'last_seen': 'lastSeen'
    }

    def __init__(self, identifier=None, name=None, agent_class=None, agent_manifest_id=None, status=None, first_seen=None, last_seen=None):
        """
        Agent - a model defined in Swagger
        """

        self._identifier = None
        self._name = None
        self._agent_class = None
        self._agent_manifest_id = None
        self._status = None
        self._first_seen = None
        self._last_seen = None

        self.identifier = identifier
        if name is not None:
          self.name = name
        if agent_class is not None:
          self.agent_class = agent_class
        if agent_manifest_id is not None:
          self.agent_manifest_id = agent_manifest_id
        if status is not None:
          self.status = status
        if first_seen is not None:
          self.first_seen = first_seen
        if last_seen is not None:
          self.last_seen = last_seen

    @property
    def identifier(self):
        """
        Gets the identifier of this Agent.
        A unique identifier for the Agent

        :return: The identifier of this Agent.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Agent.
        A unique identifier for the Agent

        :param identifier: The identifier of this Agent.
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this Agent.
        An optional human-friendly name or alias for the agent

        :return: The name of this Agent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Agent.
        An optional human-friendly name or alias for the agent

        :param name: The name of this Agent.
        :type: str
        """
        if name is not None and len(name) > 120:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `120`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def agent_class(self):
        """
        Gets the agent_class of this Agent.
        The class or category label of the agent, e.g., 'sensor-collector'

        :return: The agent_class of this Agent.
        :rtype: str
        """
        return self._agent_class

    @agent_class.setter
    def agent_class(self, agent_class):
        """
        Sets the agent_class of this Agent.
        The class or category label of the agent, e.g., 'sensor-collector'

        :param agent_class: The agent_class of this Agent.
        :type: str
        """
        if agent_class is not None and len(agent_class) > 200:
            raise ValueError("Invalid value for `agent_class`, length must be less than or equal to `200`")
        if agent_class is not None and len(agent_class) < 0:
            raise ValueError("Invalid value for `agent_class`, length must be greater than or equal to `0`")

        self._agent_class = agent_class

    @property
    def agent_manifest_id(self):
        """
        Gets the agent_manifest_id of this Agent.
        The id of the agent manifest that applies to this agent.

        :return: The agent_manifest_id of this Agent.
        :rtype: str
        """
        return self._agent_manifest_id

    @agent_manifest_id.setter
    def agent_manifest_id(self, agent_manifest_id):
        """
        Sets the agent_manifest_id of this Agent.
        The id of the agent manifest that applies to this agent.

        :param agent_manifest_id: The agent_manifest_id of this Agent.
        :type: str
        """

        self._agent_manifest_id = agent_manifest_id

    @property
    def status(self):
        """
        Gets the status of this Agent.
        A summary of the runtime status of the agent

        :return: The status of this Agent.
        :rtype: AgentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Agent.
        A summary of the runtime status of the agent

        :param status: The status of this Agent.
        :type: AgentStatus
        """

        self._status = status

    @property
    def first_seen(self):
        """
        Gets the first_seen of this Agent.
        A timestamp (milliseconds since Epoch) for the first time the agent was seen by this C2 server

        :return: The first_seen of this Agent.
        :rtype: int
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """
        Sets the first_seen of this Agent.
        A timestamp (milliseconds since Epoch) for the first time the agent was seen by this C2 server

        :param first_seen: The first_seen of this Agent.
        :type: int
        """

        self._first_seen = first_seen

    @property
    def last_seen(self):
        """
        Gets the last_seen of this Agent.
        A timestamp (milliseconds since Epoch) for the most recent time the was seen by this C2 server

        :return: The last_seen of this Agent.
        :rtype: int
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """
        Sets the last_seen of this Agent.
        A timestamp (milliseconds since Epoch) for the most recent time the was seen by this C2 server

        :param last_seen: The last_seen of this Agent.
        :type: int
        """

        self._last_seen = last_seen

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
        if not isinstance(other, Agent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
