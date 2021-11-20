# Customer Api

```python
customer_api_controller = client.customer_api
```

## Class Name

`CustomerApiController`

## Methods

* [Customer by Pk DELETE](/doc/controllers/customer-api.md#customer-by-pk-delete)
* [Customer by Pk GET](/doc/controllers/customer-api.md#customer-by-pk-get)
* [Customer by Pk PUT](/doc/controllers/customer-api.md#customer-by-pk-put)
* [Customer GET](/doc/controllers/customer-api.md#customer-get)
* [Customer Info GET](/doc/controllers/customer-api.md#customer-info-get)
* [Customer POST](/doc/controllers/customer-api.md#customer-post)


# Customer by Pk DELETE

```python
def customer_by_pk_delete(self,
                         pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`CustomerResponse2`](/doc/models/customer-response-2.md)

## Example Usage

```python
pk = 200
result = customer_api_controller.customer_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Customer by Pk GET

Get an item model

```python
def customer_by_pk_get(self,
                      pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`CustomerResponse3`](/doc/models/customer-response-3.md)

## Example Usage

```python
pk = 200
result = customer_api_controller.customer_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Customer by Pk PUT

```python
def customer_by_pk_put(self,
                      options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`CustomerApiPut`](/doc/models/customer-api-put.md) | Body, Required | Model schema |

## Response Type

[`CustomerResponse4`](/doc/models/customer-response-4.md)

## Example Usage

```python
collect = {}
pk = 200
collect['pk'] = pk

body = CustomerApiPut()
body.billing_address = 'billing_address2'
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'
body.shipping_address = 'shipping_address4'
collect['body'] = body

result = customer_api_controller.customer_by_pk_put(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Customer GET

Get a list of models

```python
def customer_get(self)
```

## Response Type

[`CustomerResponse`](/doc/models/customer-response.md)

## Example Usage

```python
result = customer_api_controller.customer_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Customer Info GET

Get metadata information about this API resource

```python
def customer_info_get(self)
```

## Response Type

[`CustomerInfoResponse`](/doc/models/customer-info-response.md)

## Example Usage

```python
result = customer_api_controller.customer_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Customer POST

```python
def customer_post(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CustomerApiPost`](/doc/models/customer-api-post.md) | Body, Required | Model schema |

## Response Type

[`CustomerResponse1`](/doc/models/customer-response-1.md)

## Example Usage

```python
body = CustomerApiPost()
body.billing_address = 'billing_address2'
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'
body.shipping_address = 'shipping_address4'
result = customer_api_controller.customer_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

