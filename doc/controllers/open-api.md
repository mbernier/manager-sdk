# Open Api

```python
open_api_controller = client.open_api
```

## Class Name

`OpenApiController`


# Openapi Openapi by Version GET

Get the OpenAPI spec for a specific API version

```python
def openapi_openapi_by_version_get(self,
                                  version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
version = 'version4'

result = open_api_controller.openapi_openapi_by_version_get(version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

