# Orgs Actions

Details on the various actions that can be performed on the
Orgs resource, including the expected
parameters and the potential responses.

##### Contents

*   [Get](#get)
*   [Post](#post)

<br/>

## Get

Returns the organizations associated with the current user

```python
result = client.orgs.get(**optional_params)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| sortField | string | N | Field to sort the results by. Accepted values are: name, id, creationDate | name | name |
| sortDirection | string | N | Direction to sort the results by. Accepted values are: asc, desc | asc | asc |
| page | string | N | Which page of results to return | 0 | 0 |
| perPage | string | N | How many items to return per page | 1000 | 10 |
| filterField | string | N | Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name |  | name |
| filter | string | N | Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering. |  | my*org |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 200 | [Organizations](_schemas.md#organizations) | Collection of organizations |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |

<br/>

## Post

Create a new organization

```python
result = client.orgs.post(organization=my_organization)

print(result)
```

#### Available Parameters

| Name | Type | Required | Description | Default | Example |
| ---- | ---- | -------- | ----------- | ------- | ------- |
| organization | [Organization Post](_schemas.md#organization-post) | Y | New organization information |  | [Organization Post Example](_schemas.md#organization-post-example) |

#### Successful Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 201 | [Organization](_schemas.md#organization) | Successfully created organization |

#### Error Responses

| Code | Type | Description |
| ---- | ---- | ----------- |
| 400 | [Error](_schemas.md#error) | Error if malformed request |
