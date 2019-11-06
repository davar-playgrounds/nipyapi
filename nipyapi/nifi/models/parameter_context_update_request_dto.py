# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.10.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ParameterContextUpdateRequestDTO(object):
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
        'request_id': 'str',
        'uri': 'str',
        'submission_time': 'datetime',
        'last_updated': 'datetime',
        'complete': 'bool',
        'failure_reason': 'str',
        'percent_completed': 'int',
        'state': 'str',
        'update_steps': 'list[ParameterContextUpdateStepDTO]',
        'parameter_context': 'ParameterContextDTO',
        'referencing_components': 'list[AffectedComponentEntity]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'uri': 'uri',
        'submission_time': 'submissionTime',
        'last_updated': 'lastUpdated',
        'complete': 'complete',
        'failure_reason': 'failureReason',
        'percent_completed': 'percentCompleted',
        'state': 'state',
        'update_steps': 'updateSteps',
        'parameter_context': 'parameterContext',
        'referencing_components': 'referencingComponents'
    }

    def __init__(self, request_id=None, uri=None, submission_time=None, last_updated=None, complete=None, failure_reason=None, percent_completed=None, state=None, update_steps=None, parameter_context=None, referencing_components=None):
        """
        ParameterContextUpdateRequestDTO - a model defined in Swagger
        """

        self._request_id = None
        self._uri = None
        self._submission_time = None
        self._last_updated = None
        self._complete = None
        self._failure_reason = None
        self._percent_completed = None
        self._state = None
        self._update_steps = None
        self._parameter_context = None
        self._referencing_components = None

        if request_id is not None:
          self.request_id = request_id
        if uri is not None:
          self.uri = uri
        if submission_time is not None:
          self.submission_time = submission_time
        if last_updated is not None:
          self.last_updated = last_updated
        if complete is not None:
          self.complete = complete
        if failure_reason is not None:
          self.failure_reason = failure_reason
        if percent_completed is not None:
          self.percent_completed = percent_completed
        if state is not None:
          self.state = state
        if update_steps is not None:
          self.update_steps = update_steps
        if parameter_context is not None:
          self.parameter_context = parameter_context
        if referencing_components is not None:
          self.referencing_components = referencing_components

    @property
    def request_id(self):
        """
        Gets the request_id of this ParameterContextUpdateRequestDTO.
        The ID of the request

        :return: The request_id of this ParameterContextUpdateRequestDTO.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this ParameterContextUpdateRequestDTO.
        The ID of the request

        :param request_id: The request_id of this ParameterContextUpdateRequestDTO.
        :type: str
        """

        self._request_id = request_id

    @property
    def uri(self):
        """
        Gets the uri of this ParameterContextUpdateRequestDTO.
        The URI for the request

        :return: The uri of this ParameterContextUpdateRequestDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ParameterContextUpdateRequestDTO.
        The URI for the request

        :param uri: The uri of this ParameterContextUpdateRequestDTO.
        :type: str
        """

        self._uri = uri

    @property
    def submission_time(self):
        """
        Gets the submission_time of this ParameterContextUpdateRequestDTO.
        The timestamp of when the request was submitted

        :return: The submission_time of this ParameterContextUpdateRequestDTO.
        :rtype: datetime
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """
        Sets the submission_time of this ParameterContextUpdateRequestDTO.
        The timestamp of when the request was submitted

        :param submission_time: The submission_time of this ParameterContextUpdateRequestDTO.
        :type: datetime
        """

        self._submission_time = submission_time

    @property
    def last_updated(self):
        """
        Gets the last_updated of this ParameterContextUpdateRequestDTO.
        The timestamp of when the request was last updated

        :return: The last_updated of this ParameterContextUpdateRequestDTO.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this ParameterContextUpdateRequestDTO.
        The timestamp of when the request was last updated

        :param last_updated: The last_updated of this ParameterContextUpdateRequestDTO.
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def complete(self):
        """
        Gets the complete of this ParameterContextUpdateRequestDTO.
        Whether or not the request is completed

        :return: The complete of this ParameterContextUpdateRequestDTO.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """
        Sets the complete of this ParameterContextUpdateRequestDTO.
        Whether or not the request is completed

        :param complete: The complete of this ParameterContextUpdateRequestDTO.
        :type: bool
        """

        self._complete = complete

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this ParameterContextUpdateRequestDTO.
        The reason for the request failing, or null if the request has not failed

        :return: The failure_reason of this ParameterContextUpdateRequestDTO.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this ParameterContextUpdateRequestDTO.
        The reason for the request failing, or null if the request has not failed

        :param failure_reason: The failure_reason of this ParameterContextUpdateRequestDTO.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def percent_completed(self):
        """
        Gets the percent_completed of this ParameterContextUpdateRequestDTO.
        A value between 0 and 100 (inclusive) indicating how close the request is to completion

        :return: The percent_completed of this ParameterContextUpdateRequestDTO.
        :rtype: int
        """
        return self._percent_completed

    @percent_completed.setter
    def percent_completed(self, percent_completed):
        """
        Sets the percent_completed of this ParameterContextUpdateRequestDTO.
        A value between 0 and 100 (inclusive) indicating how close the request is to completion

        :param percent_completed: The percent_completed of this ParameterContextUpdateRequestDTO.
        :type: int
        """

        self._percent_completed = percent_completed

    @property
    def state(self):
        """
        Gets the state of this ParameterContextUpdateRequestDTO.
        A description of the current state of the request

        :return: The state of this ParameterContextUpdateRequestDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ParameterContextUpdateRequestDTO.
        A description of the current state of the request

        :param state: The state of this ParameterContextUpdateRequestDTO.
        :type: str
        """

        self._state = state

    @property
    def update_steps(self):
        """
        Gets the update_steps of this ParameterContextUpdateRequestDTO.
        The steps that are required in order to complete the request, along with the status of each

        :return: The update_steps of this ParameterContextUpdateRequestDTO.
        :rtype: list[ParameterContextUpdateStepDTO]
        """
        return self._update_steps

    @update_steps.setter
    def update_steps(self, update_steps):
        """
        Sets the update_steps of this ParameterContextUpdateRequestDTO.
        The steps that are required in order to complete the request, along with the status of each

        :param update_steps: The update_steps of this ParameterContextUpdateRequestDTO.
        :type: list[ParameterContextUpdateStepDTO]
        """

        self._update_steps = update_steps

    @property
    def parameter_context(self):
        """
        Gets the parameter_context of this ParameterContextUpdateRequestDTO.
        The Parameter Context that is being operated on. This may not be populated until the request has successfully completed.

        :return: The parameter_context of this ParameterContextUpdateRequestDTO.
        :rtype: ParameterContextDTO
        """
        return self._parameter_context

    @parameter_context.setter
    def parameter_context(self, parameter_context):
        """
        Sets the parameter_context of this ParameterContextUpdateRequestDTO.
        The Parameter Context that is being operated on. This may not be populated until the request has successfully completed.

        :param parameter_context: The parameter_context of this ParameterContextUpdateRequestDTO.
        :type: ParameterContextDTO
        """

        self._parameter_context = parameter_context

    @property
    def referencing_components(self):
        """
        Gets the referencing_components of this ParameterContextUpdateRequestDTO.
        The components that are referenced by the update.

        :return: The referencing_components of this ParameterContextUpdateRequestDTO.
        :rtype: list[AffectedComponentEntity]
        """
        return self._referencing_components

    @referencing_components.setter
    def referencing_components(self, referencing_components):
        """
        Sets the referencing_components of this ParameterContextUpdateRequestDTO.
        The components that are referenced by the update.

        :param referencing_components: The referencing_components of this ParameterContextUpdateRequestDTO.
        :type: list[AffectedComponentEntity]
        """

        self._referencing_components = referencing_components

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
        if not isinstance(other, ParameterContextUpdateRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
