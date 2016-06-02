""" Module for Losant API Me wrapper class """
# pylint: disable=C0301

class Me(object):
    """ Class containing all the actions for the Me Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Retrieves information on the current user

        Parameters:
        *  {undefined} includeRecent - Should the user include recent app/dashboard info
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Current user information (https://api.losant.com/#/definitions/me)

        Errors:
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "includeRecent" in kwargs:
            query_params["includeRecent"] = kwargs["includeRecent"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about the current user

        Parameters:
        *  {dict} user - Object containing new user properties (https://api.losant.com/#/definitions/mePatch)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "user" in kwargs:
            body = kwargs["user"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes the current user

        Parameters:
        *  {dict} credentials - User authentication credentials (https://api.losant.com/#/definitions/userCredentials)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If the user was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "credentials" in kwargs:
            body = kwargs["credentials"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/delete".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def verify_email(self, **kwargs):
        """
        Sends and email verification to the user

        Parameters:
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If email verification was successfully sent (https://api.losant.com/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/verify-email".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def enable_two_factor_auth(self, **kwargs):
        """
        Enables two factor auth for the current user

        Parameters:
        *  {dict} data - Object containing two factor auth properties (https://api.losant.com/#/definitions/enableTwoFactorAuth)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/enableTwoFactorAuth".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def disable_two_factor_auth(self, **kwargs):
        """
        Disables two factor auth for the current user

        Parameters:
        *  {dict} data - Object containing two factor auth properties (https://api.losant.com/#/definitions/disableTwoFactorAuth)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/disableTwoFactorAuth".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def disconnect_github(self, **kwargs):
        """
        Disconnects the user from Github

        Parameters:
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/disconnectGithub".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def disconnect_twitter(self, **kwargs):
        """
        Disconnects the user from Twitter

        Parameters:
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated user information (https://api.losant.com/#/definitions/me)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/disconnectTwitter".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def add_recent_item(self, **kwargs):
        """
        Adds an item to a recent item list

        Parameters:
        *  {dict} data - Object containing recent item info (https://api.losant.com/#/definitions/recentItem)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated recent item list (https://api.losant.com/#/definitions/recentItemList)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "data" in kwargs:
            body = kwargs["data"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/recentItems".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def fetch_recent_items(self, **kwargs):
        """
        Gets a recent item list

        Parameters:
        *  {string} parentId
        *  {undefined} itemType
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent item list (https://api.losant.com/#/definitions/recentItemList)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "parentId" in kwargs:
            query_params["parentId"] = kwargs["parentId"]
        if "itemType" in kwargs:
            query_params["itemType"] = kwargs["itemType"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/me/recentItems".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

