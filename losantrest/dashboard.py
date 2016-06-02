""" Module for Losant API Dashboard wrapper class """
# pylint: disable=C0301

class Dashboard(object):
    """ Class containing all the actions for the Dashboard Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Retrieves information on an dashboard

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Dashboard information (https://api.losant.com/#/definitions/dashboard)

        Errors:
        *  404 - Error if dashboard was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a dashboard

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {dict} dashboard - Object containing new dashboard properties (https://api.losant.com/#/definitions/dashboardPatch)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Update dashboard information (https://api.losant.com/#/definitions/dashboard)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if dashboard was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "dashboard" in kwargs:
            body = kwargs["dashboard"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def delete(self, **kwargs):
        """
        Deletes an dashboard

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If dashboard was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  404 - Error if dashboard was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

