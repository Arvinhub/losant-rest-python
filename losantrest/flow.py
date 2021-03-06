""" Module for Losant API Flow wrapper class """
# pylint: disable=C0301

class Flow(object):
    """ Class containing all the actions for the Flow Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a flow

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If flow was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a flow

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Flow information (https://api.losant.com/#/definitions/flow)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_log_entries(self, **kwargs):
        """
        Retrieve the recent log entries about the flows

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} limit - Max log entries to return (ordered by time descending)
        *  {string} since - Look for log entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent log entries (https://api.losant.com/#/definitions/flowLog)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if device was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "since" in kwargs:
            query_params["since"] = kwargs["since"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/logs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_storage_entries(self, **kwargs):
        """
        Gets the current values in persistent storage

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - The stored values (https://api.losant.com/#/definitions/flowStorageEntries)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/storage".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a flow

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {hash} flow - Object containing new properties of the flow (https://api.losant.com/#/definitions/flowPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated flow information (https://api.losant.com/#/definitions/flow)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow is not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "flow" in kwargs:
            body = kwargs["flow"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def press_virtual_button(self, **kwargs):
        """
        Presses the specified virtual button on the flow

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {hash} button - Object containing button key and payload (https://api.losant.com/#/definitions/virtualButtonPress)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Virtual button was pressed (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "button" in kwargs:
            body = kwargs["button"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/virtualButton".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def set_storage_entry(self, **kwargs):
        """
        Sets a storage value

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} flowId - ID associated with the flow
        *  {hash} entry - Object containing storage entry (https://api.losant.com/#/definitions/flowStorageEntry)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Value was successfully stored (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if flow was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "flowId" in kwargs:
            path_params["flowId"] = kwargs["flowId"]
        if "entry" in kwargs:
            body = kwargs["entry"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/{flowId}/storage".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

