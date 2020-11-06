# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 0.7.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class User(object):
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
        'identity': 'str',
        'configurable': 'bool',
        'resource_permissions': 'ResourcePermissions',
        'access_policies': 'list[AccessPolicySummary]',
        'revision': 'RevisionInfo',
        'user_groups': 'list[Tenant]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'identity': 'identity',
        'configurable': 'configurable',
        'resource_permissions': 'resourcePermissions',
        'access_policies': 'accessPolicies',
        'revision': 'revision',
        'user_groups': 'userGroups'
    }

    def __init__(self, identifier=None, identity=None, configurable=None, resource_permissions=None, access_policies=None, revision=None, user_groups=None):
        """
        User - a model defined in Swagger
        """

        self._identifier = None
        self._identity = None
        self._configurable = None
        self._resource_permissions = None
        self._access_policies = None
        self._revision = None
        self._user_groups = None

        if identifier is not None:
          self.identifier = identifier
        self.identity = identity
        if configurable is not None:
          self.configurable = configurable
        if resource_permissions is not None:
          self.resource_permissions = resource_permissions
        if access_policies is not None:
          self.access_policies = access_policies
        if revision is not None:
          self.revision = revision
        if user_groups is not None:
          self.user_groups = user_groups

    @property
    def identifier(self):
        """
        Gets the identifier of this User.
        The computer-generated identifier of the tenant.

        :return: The identifier of this User.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this User.
        The computer-generated identifier of the tenant.

        :param identifier: The identifier of this User.
        :type: str
        """

        self._identifier = identifier

    @property
    def identity(self):
        """
        Gets the identity of this User.
        The human-facing identity of the tenant. This can only be changed if the tenant is configurable.

        :return: The identity of this User.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """
        Sets the identity of this User.
        The human-facing identity of the tenant. This can only be changed if the tenant is configurable.

        :param identity: The identity of this User.
        :type: str
        """
        if identity is None:
            raise ValueError("Invalid value for `identity`, must not be `None`")

        self._identity = identity

    @property
    def configurable(self):
        """
        Gets the configurable of this User.
        Indicates if this tenant is configurable, based on which UserGroupProvider has been configured to manage it.

        :return: The configurable of this User.
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """
        Sets the configurable of this User.
        Indicates if this tenant is configurable, based on which UserGroupProvider has been configured to manage it.

        :param configurable: The configurable of this User.
        :type: bool
        """

        self._configurable = configurable

    @property
    def resource_permissions(self):
        """
        Gets the resource_permissions of this User.
        A summary top-level resource access policies granted to this tenant.

        :return: The resource_permissions of this User.
        :rtype: ResourcePermissions
        """
        return self._resource_permissions

    @resource_permissions.setter
    def resource_permissions(self, resource_permissions):
        """
        Sets the resource_permissions of this User.
        A summary top-level resource access policies granted to this tenant.

        :param resource_permissions: The resource_permissions of this User.
        :type: ResourcePermissions
        """

        self._resource_permissions = resource_permissions

    @property
    def access_policies(self):
        """
        Gets the access_policies of this User.
        The access policies granted to this tenant.

        :return: The access_policies of this User.
        :rtype: list[AccessPolicySummary]
        """
        return self._access_policies

    @access_policies.setter
    def access_policies(self, access_policies):
        """
        Sets the access_policies of this User.
        The access policies granted to this tenant.

        :param access_policies: The access_policies of this User.
        :type: list[AccessPolicySummary]
        """

        self._access_policies = access_policies

    @property
    def revision(self):
        """
        Gets the revision of this User.
        The revision of this entity used for optimistic-locking during updates.

        :return: The revision of this User.
        :rtype: RevisionInfo
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this User.
        The revision of this entity used for optimistic-locking during updates.

        :param revision: The revision of this User.
        :type: RevisionInfo
        """

        self._revision = revision

    @property
    def user_groups(self):
        """
        Gets the user_groups of this User.
        The groups to which the user belongs.

        :return: The user_groups of this User.
        :rtype: list[Tenant]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """
        Sets the user_groups of this User.
        The groups to which the user belongs.

        :param user_groups: The user_groups of this User.
        :type: list[Tenant]
        """

        self._user_groups = user_groups

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
