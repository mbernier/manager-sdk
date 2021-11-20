# Vendor Shipping Api

```python
vendor_shipping_api_controller = client.vendor_shipping_api
```

## Class Name

`VendorShippingApiController`

## Methods

* [Vendor Shipping by Pk DELETE](/doc/controllers/vendor-shipping-api.md#vendor-shipping-by-pk-delete)
* [Vendor Shipping by Pk GET](/doc/controllers/vendor-shipping-api.md#vendor-shipping-by-pk-get)
* [Vendor Shipping by Pk PUT](/doc/controllers/vendor-shipping-api.md#vendor-shipping-by-pk-put)
* [Vendor Shipping GET](/doc/controllers/vendor-shipping-api.md#vendor-shipping-get)
* [Vendor Shipping Info GET](/doc/controllers/vendor-shipping-api.md#vendor-shipping-info-get)
* [Vendor Shipping POST](/doc/controllers/vendor-shipping-api.md#vendor-shipping-post)


# Vendor Shipping by Pk DELETE

```python
def vendor_shipping_by_pk_delete(self,
                                pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorShippingResponse2`](/doc/models/vendor-shipping-response-2.md)

## Example Usage

```python
pk = 200
result = vendor_shipping_api_controller.vendor_shipping_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Shipping by Pk GET

Get an item model

```python
def vendor_shipping_by_pk_get(self,
                             pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorShippingResponse3`](/doc/models/vendor-shipping-response-3.md)

## Example Usage

```python
pk = 200
result = vendor_shipping_api_controller.vendor_shipping_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Shipping by Pk PUT

```python
def vendor_shipping_by_pk_put(self,
                             options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`VendorShippingApiPut`](/doc/models/vendor-shipping-api-put.md) | Body, Required | Model schema |

## Response Type

[`VendorShippingResponse4`](/doc/models/vendor-shipping-response-4.md)

## Example Usage

```python
collect = {}
pk = 200
collect['pk'] = pk

body = VendorShippingApiPut()
body.name = 'name6'
body.shipping_variable = 'shipping_variable4'
collect['body'] = body

result = vendor_shipping_api_controller.vendor_shipping_by_pk_put(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Shipping GET

Get a list of models

```python
def vendor_shipping_get(self)
```

## Response Type

[`VendorShippingResponse`](/doc/models/vendor-shipping-response.md)

## Example Usage

```python
result = vendor_shipping_api_controller.vendor_shipping_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Shipping Info GET

Get metadata information about this API resource

```python
def vendor_shipping_info_get(self)
```

## Response Type

[`VendorShippingInfoResponse`](/doc/models/vendor-shipping-info-response.md)

## Example Usage

```python
result = vendor_shipping_api_controller.vendor_shipping_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Shipping POST

```python
def vendor_shipping_post(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VendorShippingApiPost`](/doc/models/vendor-shipping-api-post.md) | Body, Required | Model schema |

## Response Type

[`VendorShippingResponse1`](/doc/models/vendor-shipping-response-1.md)

## Example Usage

```python
body = VendorShippingApiPost()
body.name = 'name6'
body.shipping_variable = 'shipping_variable4'
result = vendor_shipping_api_controller.vendor_shipping_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

