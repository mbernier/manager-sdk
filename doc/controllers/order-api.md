# Order Api

```python
order_api_controller = client.order_api
```

## Class Name

`OrderApiController`

## Methods

* [Order GET](/doc/controllers/order-api.md#order-get)
* [Order POST](/doc/controllers/order-api.md#order-post)
* [Order Info GET](/doc/controllers/order-api.md#order-info-get)
* [Order by Pk DELETE](/doc/controllers/order-api.md#order-by-pk-delete)
* [Order by Pk GET](/doc/controllers/order-api.md#order-by-pk-get)
* [Order by Pk PUT](/doc/controllers/order-api.md#order-by-pk-put)


# Order GET

Get a list of models

```python
def order_get(self)
```

## Response Type

[`OrderResponse`](/doc/models/order-response.md)

## Example Usage

```python
result = order_api_controller.order_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order POST

```python
def order_post(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrderApiPost`](/doc/models/order-api-post.md) | Body, Required | Model schema |

## Response Type

[`OrderResponse1`](/doc/models/order-response-1.md)

## Example Usage

```python
body = OrderApiPost()
body.billing_address = 'billing_address2'
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'
body.shipping_address = 'shipping_address4'

result = order_api_controller.order_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Info GET

Get metadata information about this API resource

```python
def order_info_get(self)
```

## Response Type

[`OrderInfoResponse`](/doc/models/order-info-response.md)

## Example Usage

```python
result = order_api_controller.order_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order by Pk DELETE

```python
def order_by_pk_delete(self,
                      pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`OrderResponse2`](/doc/models/order-response-2.md)

## Example Usage

```python
pk = 200

result = order_api_controller.order_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order by Pk GET

Get an item model

```python
def order_by_pk_get(self,
                   pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`OrderResponse3`](/doc/models/order-response-3.md)

## Example Usage

```python
pk = 200

result = order_api_controller.order_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order by Pk PUT

```python
def order_by_pk_put(self,
                   pk,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`OrderApiPut`](/doc/models/order-api-put.md) | Body, Required | Model schema |

## Response Type

[`OrderResponse4`](/doc/models/order-response-4.md)

## Example Usage

```python
pk = 200
body = OrderApiPut()
body.billing_address = 'billing_address2'
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'
body.shipping_address = 'shipping_address4'

result = order_api_controller.order_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

