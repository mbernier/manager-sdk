# Vendor Contact Api

```python
vendor_contact_api_controller = client.vendor_contact_api
```

## Class Name

`VendorContactApiController`

## Methods

* [Vendor Contact GET](/doc/controllers/vendor-contact-api.md#vendor-contact-get)
* [Vendor Contact POST](/doc/controllers/vendor-contact-api.md#vendor-contact-post)
* [Vendor Contact Info GET](/doc/controllers/vendor-contact-api.md#vendor-contact-info-get)
* [Vendor Contact by Pk DELETE](/doc/controllers/vendor-contact-api.md#vendor-contact-by-pk-delete)
* [Vendor Contact by Pk GET](/doc/controllers/vendor-contact-api.md#vendor-contact-by-pk-get)
* [Vendor Contact by Pk PUT](/doc/controllers/vendor-contact-api.md#vendor-contact-by-pk-put)


# Vendor Contact GET

Get a list of models

```python
def vendor_contact_get(self)
```

## Response Type

[`VendorContactResponse`](/doc/models/vendor-contact-response.md)

## Example Usage

```python
result = vendor_contact_api_controller.vendor_contact_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Contact POST

```python
def vendor_contact_post(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VendorContactApiPost`](/doc/models/vendor-contact-api-post.md) | Body, Required | Model schema |

## Response Type

[`VendorContactResponse1`](/doc/models/vendor-contact-response-1.md)

## Example Usage

```python
body = VendorContactApiPost()
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'

result = vendor_contact_api_controller.vendor_contact_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Contact Info GET

Get metadata information about this API resource

```python
def vendor_contact_info_get(self)
```

## Response Type

[`VendorContactInfoResponse`](/doc/models/vendor-contact-info-response.md)

## Example Usage

```python
result = vendor_contact_api_controller.vendor_contact_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Contact by Pk DELETE

```python
def vendor_contact_by_pk_delete(self,
                               pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorContactResponse2`](/doc/models/vendor-contact-response-2.md)

## Example Usage

```python
pk = 200

result = vendor_contact_api_controller.vendor_contact_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Contact by Pk GET

Get an item model

```python
def vendor_contact_by_pk_get(self,
                            pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`VendorContactResponse3`](/doc/models/vendor-contact-response-3.md)

## Example Usage

```python
pk = 200

result = vendor_contact_api_controller.vendor_contact_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Vendor Contact by Pk PUT

```python
def vendor_contact_by_pk_put(self,
                            pk,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`VendorContactApiPut`](/doc/models/vendor-contact-api-put.md) | Body, Required | Model schema |

## Response Type

[`VendorContactResponse4`](/doc/models/vendor-contact-response-4.md)

## Example Usage

```python
pk = 200
body = VendorContactApiPut()
body.email = 'email0'
body.name = 'name6'
body.phone = 'phone4'

result = vendor_contact_api_controller.vendor_contact_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

