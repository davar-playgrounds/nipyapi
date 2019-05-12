# coding: utf-8

"""
    Cloudera Edge Flow Manager REST API

    This REST API provides remote access to the EFM Server.                                             Endpoints that are marked as [BETA] are subject to change in future releases of the application without backwards compatibility and without a major version change.

    OpenAPI spec version: 1.0.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FlowMappingsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_flow_mapping(self, body, **kwargs):
        """
        Creates a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_flow_mapping(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowMapping body: The flow mapping to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_flow_mapping_with_http_info(body, **kwargs)
        else:
            (data) = self.create_flow_mapping_with_http_info(body, **kwargs)
            return data

    def create_flow_mapping_with_http_info(self, body, **kwargs):
        """
        Creates a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_flow_mapping_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowMapping body: The flow mapping to create (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_flow_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_flow_mapping`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/flow-mappings', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_flow_mapping(self, agent_class_name, **kwargs):
        """
        Deletes a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_flow_mapping(agent_class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to delete the mapping for (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_flow_mapping_with_http_info(agent_class_name, **kwargs)
        else:
            (data) = self.delete_flow_mapping_with_http_info(agent_class_name, **kwargs)
            return data

    def delete_flow_mapping_with_http_info(self, agent_class_name, **kwargs):
        """
        Deletes a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_flow_mapping_with_http_info(agent_class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to delete the mapping for (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_class_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_flow_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_class_name' is set
        if ('agent_class_name' not in params) or (params['agent_class_name'] is None):
            raise ValueError("Missing the required parameter `agent_class_name` when calling `delete_flow_mapping`")


        collection_formats = {}

        path_params = {}
        if 'agent_class_name' in params:
            path_params['agentClassName'] = params['agent_class_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/flow-mappings/{agentClassName}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlowMapping',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_flow_mappings(self, **kwargs):
        """
        Gets all flow mappings. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_flow_mappings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FlowMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_flow_mappings_with_http_info(**kwargs)
        else:
            (data) = self.get_all_flow_mappings_with_http_info(**kwargs)
            return data

    def get_all_flow_mappings_with_http_info(self, **kwargs):
        """
        Gets all flow mappings. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_flow_mappings_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FlowMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_flow_mappings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/flow-mappings', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlowMappings',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_flow_mapping(self, agent_class_name, **kwargs):
        """
        Gets a flow mapping for a given agent class. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_flow_mapping(agent_class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to retrieve (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_flow_mapping_with_http_info(agent_class_name, **kwargs)
        else:
            (data) = self.get_flow_mapping_with_http_info(agent_class_name, **kwargs)
            return data

    def get_flow_mapping_with_http_info(self, agent_class_name, **kwargs):
        """
        Gets a flow mapping for a given agent class. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_flow_mapping_with_http_info(agent_class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to retrieve (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_class_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flow_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_class_name' is set
        if ('agent_class_name' not in params) or (params['agent_class_name'] is None):
            raise ValueError("Missing the required parameter `agent_class_name` when calling `get_flow_mapping`")


        collection_formats = {}

        path_params = {}
        if 'agent_class_name' in params:
            path_params['agentClassName'] = params['agent_class_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/flow-mappings/{agentClassName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlowMapping',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_flow_mapping(self, agent_class_name, body, **kwargs):
        """
        Updates a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_flow_mapping(agent_class_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to update the mapping for (required)
        :param FlowMapping body: The flow mapping to update (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_flow_mapping_with_http_info(agent_class_name, body, **kwargs)
        else:
            (data) = self.update_flow_mapping_with_http_info(agent_class_name, body, **kwargs)
            return data

    def update_flow_mapping_with_http_info(self, agent_class_name, body, **kwargs):
        """
        Updates a flow mapping. [BETA]
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_flow_mapping_with_http_info(agent_class_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_class_name: The name of the class to update the mapping for (required)
        :param FlowMapping body: The flow mapping to update (required)
        :return: FlowMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_class_name', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_flow_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_class_name' is set
        if ('agent_class_name' not in params) or (params['agent_class_name'] is None):
            raise ValueError("Missing the required parameter `agent_class_name` when calling `update_flow_mapping`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_flow_mapping`")


        collection_formats = {}

        path_params = {}
        if 'agent_class_name' in params:
            path_params['agentClassName'] = params['agent_class_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/flow-mappings/{agentClassName}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlowMapping',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
