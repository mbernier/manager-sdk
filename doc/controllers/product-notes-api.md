# Product Notes Api

```python
product_notes_api_controller = client.product_notes_api
```

## Class Name

`ProductNotesApiController`

## Methods

* [Product Notes by Pk DELETE](/doc/controllers/product-notes-api.md#product-notes-by-pk-delete)
* [Product Notes by Pk GET](/doc/controllers/product-notes-api.md#product-notes-by-pk-get)
* [Product Notes by Pk PUT](/doc/controllers/product-notes-api.md#product-notes-by-pk-put)
* [Product Notes GET](/doc/controllers/product-notes-api.md#product-notes-get)
* [Product Notes Info GET](/doc/controllers/product-notes-api.md#product-notes-info-get)
* [Product Notes POST](/doc/controllers/product-notes-api.md#product-notes-post)


# Product Notes by Pk DELETE

```python
def product_notes_by_pk_delete(self,
                              pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`ProductNotesResponse2`](/doc/models/product-notes-response-2.md)

## Example Usage

```python
pk = 200
result = product_notes_api_controller.product_notes_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Product Notes by Pk GET

Get an item model

```python
def product_notes_by_pk_get(self,
                           pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`ProductNotesResponse3`](/doc/models/product-notes-response-3.md)

## Example Usage

```python
pk = 200
result = product_notes_api_controller.product_notes_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Product Notes by Pk PUT

```python
def product_notes_by_pk_put(self,
                           options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`ProductNotesApiPut`](/doc/models/product-notes-api-put.md) | Body, Required | Model schema |

## Response Type

[`ProductNotesResponse4`](/doc/models/product-notes-response-4.md)

## Example Usage

```python
collect = {}
pk = 200
collect['pk'] = pk

body = ProductNotesApiPut()
body.note = 'note8'
collect['body'] = body

result = product_notes_api_controller.product_notes_by_pk_put(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Product Notes GET

Get a list of models

```python
def product_notes_get(self)
```

## Response Type

[`ProductNotesResponse`](/doc/models/product-notes-response.md)

## Example Usage

```python
result = product_notes_api_controller.product_notes_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Product Notes Info GET

Get metadata information about this API resource

```python
def product_notes_info_get(self)
```

## Response Type

[`ProductNotesInfoResponse`](/doc/models/product-notes-info-response.md)

## Example Usage

```python
result = product_notes_api_controller.product_notes_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Product Notes POST

```python
def product_notes_post(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProductNotesApiPost`](/doc/models/product-notes-api-post.md) | Body, Required | Model schema |

## Response Type

[`ProductNotesResponse1`](/doc/models/product-notes-response-1.md)

## Example Usage

```python
body = ProductNotesApiPost()
body.note = 'note8'
result = product_notes_api_controller.product_notes_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

