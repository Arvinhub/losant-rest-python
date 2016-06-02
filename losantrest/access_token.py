""" Module for Losant API AccessToken wrapper class """
# pylint: disable=C0301

class AccessToken(object):
    """ Class containing all the actions for the Access Token Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Retrieves information on an accessToken

        Parameters:
        *  {string} accessTokenId - ID associated with the accessToken
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Device information (https://api.losant.com/#/definitions/accessToken)

        Errors:
        *  404 - Error if accessToken was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "accessTokenId" in kwargs:
            path_params["accessTokenId"] = kwargs["accessTokenId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/access-tokens/{accessTokenId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a accessToken

        Parameters:
        *  {string} accessTokenId - ID associated with the accessToken
        *  {dict} accessToken - Object containing new properties of the accessToken (https://api.losant.com/#/definitions/accessTokenPatch)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated accessToken information (https://api.losant.com/#/definitions/accessToken)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if accessToken was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "accessTokenId" in kwargs:
            path_params["accessTokenId"] = kwargs["accessTokenId"]
        if "accessToken" in kwargs:
            body = kwargs["accessToken"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/access-tokens/{accessTokenId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes a accessToken

        Parameters:
        *  {string} accessTokenId - ID associated with the accessToken
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If accessToken was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  404 - Error if accessToken was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "accessTokenId" in kwargs:
            path_params["accessTokenId"] = kwargs["accessTokenId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/access-tokens/{accessTokenId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

