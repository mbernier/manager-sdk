# Vendor Api

```python
vendor_api_controller = client.vendor_api
```

## Class Name

`VendorApiController`

## Methods

* [Vendor by Pk DELETE](/doc/controllers/vendor-api.md#vendor-by-pk-delete)
* [Vendor by Pk GET](/doc/controllers/vendor-api.md#vendor-by-pk-get)
* [Vendor by Pk PUT](/doc/controllers/vendor-api.md#vendor-by-pk-put)
* [Vendor GET](/doc/controllers/vendor-api.md#vendor-get)
* [Vendor Info GET](/doc/controllers/vendor-api.md#vendor-info-get)
* [Vendor POST](/doc/controllers/vendor-api.md#vendor-post)


# Vendor by Pk DELETE

```python
def vendor_by_pk_delete(self,
                       pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorResponse2`](/doc/models/vendor-response-2.md)

## Example Usage

```python
pk = 200
result = vendor_api_controller.vendor_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor by Pk GET

Get an item model

```python
def vendor_by_pk_get(self,
                    pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorResponse3`](/doc/models/vendor-response-3.md)

## Example Usage

```python
pk = 200
result = vendor_api_controller.vendor_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor by Pk PUT

```python
def vendor_by_pk_put(self,
                    options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`VendorApiPut`](/doc/models/vendor-api-put.md) | Body, Required | Model schema |

## Response Type

[`VendorResponse4`](/doc/models/vendor-response-4.md)

## Example Usage

```python
collect = {}
pk = 200
collect['pk'] = pk

body = VendorApiPut()
body.name = 'name6'
collect['body'] = body

result = vendor_api_controller.vendor_by_pk_put(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor GET

Get a list of models

```python
def vendor_get(self)
```

## Response Type

[`VendorResponse`](/doc/models/vendor-response.md)

## Example Usage

```python
result = vendor_api_controller.vendor_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Info GET

Get metadata information about this API resource

```python
def vendor_info_get(self)
```

## Response Type

[`VendorInfoResponse`](/doc/models/vendor-info-response.md)

## Example Usage

```python
result = vendor_api_controller.vendor_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor POST

```python
def vendor_post(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VendorApiPost`](/doc/models/vendor-api-post.md) | Body, Required | Model schema |

## Response Type

[`VendorResponse1`](/doc/models/vendor-response-1.md)

## Example Usage

```python
body = VendorApiPost()
body.name = 'name6'
result = vendor_api_controller.vendor_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

