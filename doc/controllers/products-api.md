# Products Api

```python
products_api_controller = client.products_api
```

## Class Name

`ProductsApiController`

## Methods

* [Products GET](/doc/controllers/products-api.md#products-get)
* [Products POST](/doc/controllers/products-api.md#products-post)
* [Products Info GET](/doc/controllers/products-api.md#products-info-get)
* [Products by Pk DELETE](/doc/controllers/products-api.md#products-by-pk-delete)
* [Products by Pk GET](/doc/controllers/products-api.md#products-by-pk-get)
* [Products by Pk PUT](/doc/controllers/products-api.md#products-by-pk-put)


# Products GET

Get a list of models

```python
def products_get(self)
```

## Response Type

[`ProductsResponse`](/doc/models/products-response.md)

## Example Usage

```python
result = products_api_controller.products_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Products POST

```python
def products_post(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProductsApiPost`](/doc/models/products-api-post.md) | Body, Required | Model schema |

## Response Type

[`ProductsResponse1`](/doc/models/products-response-1.md)

## Example Usage

```python
body = ProductsApiPost()
body.handle = 'handle2'
body.name = 'name6'
body.sku = 'sku8'
body.vendor_sku = 'vendor_sku2'
body.vendor_url = 'vendor_url0'

result = products_api_controller.products_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Products Info GET

Get metadata information about this API resource

```python
def products_info_get(self)
```

## Response Type

[`ProductsInfoResponse`](/doc/models/products-info-response.md)

## Example Usage

```python
result = products_api_controller.products_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Products by Pk DELETE

```python
def products_by_pk_delete(self,
                         pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`ProductsResponse2`](/doc/models/products-response-2.md)

## Example Usage

```python
pk = 200

result = products_api_controller.products_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Products by Pk GET

Get an item model

```python
def products_by_pk_get(self,
                      pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`ProductsResponse3`](/doc/models/products-response-3.md)

## Example Usage

```python
pk = 200

result = products_api_controller.products_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Products by Pk PUT

```python
def products_by_pk_put(self,
                      pk,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`ProductsApiPut`](/doc/models/products-api-put.md) | Body, Required | Model schema |

## Response Type

[`ProductsResponse4`](/doc/models/products-response-4.md)

## Example Usage

```python
pk = 200
body = ProductsApiPut()
body.handle = 'handle2'
body.name = 'name6'
body.sku = 'sku8'
body.vendor_sku = 'vendor_sku2'
body.vendor_url = 'vendor_url0'

result = products_api_controller.products_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

