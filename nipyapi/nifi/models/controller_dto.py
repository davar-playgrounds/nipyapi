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


class ControllerDTO(object):
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
        'name': 'str',
        'comments': 'str',
        'running_count': 'int',
        'stopped_count': 'int',
        'invalid_count': 'int',
        'disabled_count': 'int',
        'active_remote_port_count': 'int',
        'inactive_remote_port_count': 'int',
        'input_port_count': 'int',
        'output_port_count': 'int',
        'remote_site_listening_port': 'int',
        'remote_site_http_listening_port': 'int',
        'site_to_site_secure': 'bool',
        'instance_id': 'str',
        'input_ports': 'list[PortDTO]',
        'output_ports': 'list[PortDTO]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'comments': 'comments',
        'running_count': 'runningCount',
        'stopped_count': 'stoppedCount',
        'invalid_count': 'invalidCount',
        'disabled_count': 'disabledCount',
        'active_remote_port_count': 'activeRemotePortCount',
        'inactive_remote_port_count': 'inactiveRemotePortCount',
        'input_port_count': 'inputPortCount',
        'output_port_count': 'outputPortCount',
        'remote_site_listening_port': 'remoteSiteListeningPort',
        'remote_site_http_listening_port': 'remoteSiteHttpListeningPort',
        'site_to_site_secure': 'siteToSiteSecure',
        'instance_id': 'instanceId',
        'input_ports': 'inputPorts',
        'output_ports': 'outputPorts'
    }

    def __init__(self, id=None, name=None, comments=None, running_count=None, stopped_count=None, invalid_count=None, disabled_count=None, active_remote_port_count=None, inactive_remote_port_count=None, input_port_count=None, output_port_count=None, remote_site_listening_port=None, remote_site_http_listening_port=None, site_to_site_secure=None, instance_id=None, input_ports=None, output_ports=None):
        """
        ControllerDTO - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._comments = None
        self._running_count = None
        self._stopped_count = None
        self._invalid_count = None
        self._disabled_count = None
        self._active_remote_port_count = None
        self._inactive_remote_port_count = None
        self._input_port_count = None
        self._output_port_count = None
        self._remote_site_listening_port = None
        self._remote_site_http_listening_port = None
        self._site_to_site_secure = None
        self._instance_id = None
        self._input_ports = None
        self._output_ports = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments
        if running_count is not None:
          self.running_count = running_count
        if stopped_count is not None:
          self.stopped_count = stopped_count
        if invalid_count is not None:
          self.invalid_count = invalid_count
        if disabled_count is not None:
          self.disabled_count = disabled_count
        if active_remote_port_count is not None:
          self.active_remote_port_count = active_remote_port_count
        if inactive_remote_port_count is not None:
          self.inactive_remote_port_count = inactive_remote_port_count
        if input_port_count is not None:
          self.input_port_count = input_port_count
        if output_port_count is not None:
          self.output_port_count = output_port_count
        if remote_site_listening_port is not None:
          self.remote_site_listening_port = remote_site_listening_port
        if remote_site_http_listening_port is not None:
          self.remote_site_http_listening_port = remote_site_http_listening_port
        if site_to_site_secure is not None:
          self.site_to_site_secure = site_to_site_secure
        if instance_id is not None:
          self.instance_id = instance_id
        if input_ports is not None:
          self.input_ports = input_ports
        if output_ports is not None:
          self.output_ports = output_ports

    @property
    def id(self):
        """
        Gets the id of this ControllerDTO.
        The id of the NiFi.

        :return: The id of this ControllerDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ControllerDTO.
        The id of the NiFi.

        :param id: The id of this ControllerDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ControllerDTO.
        The name of the NiFi.

        :return: The name of this ControllerDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ControllerDTO.
        The name of the NiFi.

        :param name: The name of this ControllerDTO.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this ControllerDTO.
        The comments for the NiFi.

        :return: The comments of this ControllerDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ControllerDTO.
        The comments for the NiFi.

        :param comments: The comments of this ControllerDTO.
        :type: str
        """

        self._comments = comments

    @property
    def running_count(self):
        """
        Gets the running_count of this ControllerDTO.
        The number of running components in the NiFi.

        :return: The running_count of this ControllerDTO.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """
        Sets the running_count of this ControllerDTO.
        The number of running components in the NiFi.

        :param running_count: The running_count of this ControllerDTO.
        :type: int
        """

        self._running_count = running_count

    @property
    def stopped_count(self):
        """
        Gets the stopped_count of this ControllerDTO.
        The number of stopped components in the NiFi.

        :return: The stopped_count of this ControllerDTO.
        :rtype: int
        """
        return self._stopped_count

    @stopped_count.setter
    def stopped_count(self, stopped_count):
        """
        Sets the stopped_count of this ControllerDTO.
        The number of stopped components in the NiFi.

        :param stopped_count: The stopped_count of this ControllerDTO.
        :type: int
        """

        self._stopped_count = stopped_count

    @property
    def invalid_count(self):
        """
        Gets the invalid_count of this ControllerDTO.
        The number of invalid components in the NiFi.

        :return: The invalid_count of this ControllerDTO.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        """
        Sets the invalid_count of this ControllerDTO.
        The number of invalid components in the NiFi.

        :param invalid_count: The invalid_count of this ControllerDTO.
        :type: int
        """

        self._invalid_count = invalid_count

    @property
    def disabled_count(self):
        """
        Gets the disabled_count of this ControllerDTO.
        The number of disabled components in the NiFi.

        :return: The disabled_count of this ControllerDTO.
        :rtype: int
        """
        return self._disabled_count

    @disabled_count.setter
    def disabled_count(self, disabled_count):
        """
        Sets the disabled_count of this ControllerDTO.
        The number of disabled components in the NiFi.

        :param disabled_count: The disabled_count of this ControllerDTO.
        :type: int
        """

        self._disabled_count = disabled_count

    @property
    def active_remote_port_count(self):
        """
        Gets the active_remote_port_count of this ControllerDTO.
        The number of active remote ports contained in the NiFi.

        :return: The active_remote_port_count of this ControllerDTO.
        :rtype: int
        """
        return self._active_remote_port_count

    @active_remote_port_count.setter
    def active_remote_port_count(self, active_remote_port_count):
        """
        Sets the active_remote_port_count of this ControllerDTO.
        The number of active remote ports contained in the NiFi.

        :param active_remote_port_count: The active_remote_port_count of this ControllerDTO.
        :type: int
        """

        self._active_remote_port_count = active_remote_port_count

    @property
    def inactive_remote_port_count(self):
        """
        Gets the inactive_remote_port_count of this ControllerDTO.
        The number of inactive remote ports contained in the NiFi.

        :return: The inactive_remote_port_count of this ControllerDTO.
        :rtype: int
        """
        return self._inactive_remote_port_count

    @inactive_remote_port_count.setter
    def inactive_remote_port_count(self, inactive_remote_port_count):
        """
        Sets the inactive_remote_port_count of this ControllerDTO.
        The number of inactive remote ports contained in the NiFi.

        :param inactive_remote_port_count: The inactive_remote_port_count of this ControllerDTO.
        :type: int
        """

        self._inactive_remote_port_count = inactive_remote_port_count

    @property
    def input_port_count(self):
        """
        Gets the input_port_count of this ControllerDTO.
        The number of input ports contained in the NiFi.

        :return: The input_port_count of this ControllerDTO.
        :rtype: int
        """
        return self._input_port_count

    @input_port_count.setter
    def input_port_count(self, input_port_count):
        """
        Sets the input_port_count of this ControllerDTO.
        The number of input ports contained in the NiFi.

        :param input_port_count: The input_port_count of this ControllerDTO.
        :type: int
        """

        self._input_port_count = input_port_count

    @property
    def output_port_count(self):
        """
        Gets the output_port_count of this ControllerDTO.
        The number of output ports in the NiFi.

        :return: The output_port_count of this ControllerDTO.
        :rtype: int
        """
        return self._output_port_count

    @output_port_count.setter
    def output_port_count(self, output_port_count):
        """
        Sets the output_port_count of this ControllerDTO.
        The number of output ports in the NiFi.

        :param output_port_count: The output_port_count of this ControllerDTO.
        :type: int
        """

        self._output_port_count = output_port_count

    @property
    def remote_site_listening_port(self):
        """
        Gets the remote_site_listening_port of this ControllerDTO.
        The Socket Port on which this instance is listening for Remote Transfers of Flow Files. If this instance is not configured to receive Flow Files from remote instances, this will be null.

        :return: The remote_site_listening_port of this ControllerDTO.
        :rtype: int
        """
        return self._remote_site_listening_port

    @remote_site_listening_port.setter
    def remote_site_listening_port(self, remote_site_listening_port):
        """
        Sets the remote_site_listening_port of this ControllerDTO.
        The Socket Port on which this instance is listening for Remote Transfers of Flow Files. If this instance is not configured to receive Flow Files from remote instances, this will be null.

        :param remote_site_listening_port: The remote_site_listening_port of this ControllerDTO.
        :type: int
        """

        self._remote_site_listening_port = remote_site_listening_port

    @property
    def remote_site_http_listening_port(self):
        """
        Gets the remote_site_http_listening_port of this ControllerDTO.
        The HTTP(S) Port on which this instance is listening for Remote Transfers of Flow Files. If this instance is not configured to receive Flow Files from remote instances, this will be null.

        :return: The remote_site_http_listening_port of this ControllerDTO.
        :rtype: int
        """
        return self._remote_site_http_listening_port

    @remote_site_http_listening_port.setter
    def remote_site_http_listening_port(self, remote_site_http_listening_port):
        """
        Sets the remote_site_http_listening_port of this ControllerDTO.
        The HTTP(S) Port on which this instance is listening for Remote Transfers of Flow Files. If this instance is not configured to receive Flow Files from remote instances, this will be null.

        :param remote_site_http_listening_port: The remote_site_http_listening_port of this ControllerDTO.
        :type: int
        """

        self._remote_site_http_listening_port = remote_site_http_listening_port

    @property
    def site_to_site_secure(self):
        """
        Gets the site_to_site_secure of this ControllerDTO.
        Indicates whether or not Site-to-Site communications with this instance is secure (2-way authentication).

        :return: The site_to_site_secure of this ControllerDTO.
        :rtype: bool
        """
        return self._site_to_site_secure

    @site_to_site_secure.setter
    def site_to_site_secure(self, site_to_site_secure):
        """
        Sets the site_to_site_secure of this ControllerDTO.
        Indicates whether or not Site-to-Site communications with this instance is secure (2-way authentication).

        :param site_to_site_secure: The site_to_site_secure of this ControllerDTO.
        :type: bool
        """

        self._site_to_site_secure = site_to_site_secure

    @property
    def instance_id(self):
        """
        Gets the instance_id of this ControllerDTO.
        If clustered, the id of the Cluster Manager, otherwise the id of the NiFi.

        :return: The instance_id of this ControllerDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this ControllerDTO.
        If clustered, the id of the Cluster Manager, otherwise the id of the NiFi.

        :param instance_id: The instance_id of this ControllerDTO.
        :type: str
        """

        self._instance_id = instance_id

    @property
    def input_ports(self):
        """
        Gets the input_ports of this ControllerDTO.
        The input ports available to send data to for the NiFi.

        :return: The input_ports of this ControllerDTO.
        :rtype: list[PortDTO]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this ControllerDTO.
        The input ports available to send data to for the NiFi.

        :param input_ports: The input_ports of this ControllerDTO.
        :type: list[PortDTO]
        """

        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this ControllerDTO.
        The output ports available to received data from the NiFi.

        :return: The output_ports of this ControllerDTO.
        :rtype: list[PortDTO]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this ControllerDTO.
        The output ports available to received data from the NiFi.

        :param output_ports: The output_ports of this ControllerDTO.
        :type: list[PortDTO]
        """

        self._output_ports = output_ports

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
        if not isinstance(other, ControllerDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
