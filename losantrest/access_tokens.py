""" Module for Losant API AccessTokens wrapper class """
# pylint: disable=C0301

class AccessTokens(object):
    """ Class containing all the actions for the Access Tokens Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the accessTokens for a user

        Parameters:
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of accessTokens (https://api.losant.com/#/definitions/accessTokens)

        Errors:
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

        path = "/access-tokens".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new accessKey for a user

        Parameters:
        *  {dict} accessToken - AccessToken information (https://api.losant.com/#/definitions/accessToken)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created access token (https://api.losant.com/#/definitions/accessToken)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "accessToken" in kwargs:
            body = kwargs["accessToken"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/access-tokens".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

