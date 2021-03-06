# Flows Actions

Details on the various actions that can be performed on the
Flows resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the flows for an application

```python
result = client.flows.get(applicationId=my_application_id)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| sortField | string | N | Field to sort the results by. Accepted values are: name, id, creationDate | name | name |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 1000 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name |  | name |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my*flow |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Workflows](_schemas.md#workflows) | Collection of flows |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |

<br/>

## Post

Create a new flow for an application

```python
result = client.flows.post(
    applicationId=my_application_id,
    flow=my_flow)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| applicationId | string | Y | ID associated with the application |  | 575ec8687ae143cd83dc4a97 |
| flow | [Workflow Post](_schemas.md#workflow-post) | Y | New flow information |  | [Workflow Post Example](_schemas.md#workflow-post-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Workflow](_schemas.md#workflow) | Successfully created flow |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
| 404 | [Error](_schemas.md#error) | Error if application was not found |
