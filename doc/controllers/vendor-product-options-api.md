# Vendor Product Options Api

```python
vendor_product_options_api_controller = client.vendor_product_options_api
```

## Class Name

`VendorProductOptionsApiController`

## Methods

* [Vendor Product Options GET](/doc/controllers/vendor-product-options-api.md#vendor-product-options-get)
* [Vendor Product Options POST](/doc/controllers/vendor-product-options-api.md#vendor-product-options-post)
* [Vendor Product Options Info GET](/doc/controllers/vendor-product-options-api.md#vendor-product-options-info-get)
* [Vendor Product Options by Pk DELETE](/doc/controllers/vendor-product-options-api.md#vendor-product-options-by-pk-delete)
* [Vendor Product Options by Pk GET](/doc/controllers/vendor-product-options-api.md#vendor-product-options-by-pk-get)
* [Vendor Product Options by Pk PUT](/doc/controllers/vendor-product-options-api.md#vendor-product-options-by-pk-put)


# Vendor Product Options GET

Get a list of models

```python
def vendor_product_options_get(self)
```

## Response Type

[`VendorProductOptionsResponse`](/doc/models/vendor-product-options-response.md)

## Example Usage

```python
result = vendor_product_options_api_controller.vendor_product_options_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Product Options POST

```python
def vendor_product_options_post(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VendorProductOptionsApiPost`](/doc/models/vendor-product-options-api-post.md) | Body, Required | Model schema |

## Response Type

[`VendorProductOptionsResponse1`](/doc/models/vendor-product-options-response-1.md)

## Example Usage

```python
body = VendorProductOptionsApiPost()
body.product_type = 'product_type8'

result = vendor_product_options_api_controller.vendor_product_options_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Product Options Info GET

Get metadata information about this API resource

```python
def vendor_product_options_info_get(self)
```

## Response Type

[`VendorProductOptionsInfoResponse`](/doc/models/vendor-product-options-info-response.md)

## Example Usage

```python
result = vendor_product_options_api_controller.vendor_product_options_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Product Options by Pk DELETE

```python
def vendor_product_options_by_pk_delete(self,
                                       pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorProductOptionsResponse2`](/doc/models/vendor-product-options-response-2.md)

## Example Usage

```python
pk = 200

result = vendor_product_options_api_controller.vendor_product_options_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Product Options by Pk GET

Get an item model

```python
def vendor_product_options_by_pk_get(self,
                                    pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorProductOptionsResponse3`](/doc/models/vendor-product-options-response-3.md)

## Example Usage

```python
pk = 200

result = vendor_product_options_api_controller.vendor_product_options_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Product Options by Pk PUT

```python
def vendor_product_options_by_pk_put(self,
                                    pk,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`VendorProductOptionsApiPut`](/doc/models/vendor-product-options-api-put.md) | Body, Required | Model schema |

## Response Type

[`VendorProductOptionsResponse4`](/doc/models/vendor-product-options-response-4.md)

## Example Usage

```python
pk = 200
body = VendorProductOptionsApiPut()
body.product_type = 'product_type8'

result = vendor_product_options_api_controller.vendor_product_options_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

