# Order Notes Api

```python
order_notes_api_controller = client.order_notes_api
```

## Class Name

`OrderNotesApiController`

## Methods

* [Order Notes GET](/doc/controllers/order-notes-api.md#order-notes-get)
* [Order Notes POST](/doc/controllers/order-notes-api.md#order-notes-post)
* [Order Notes Info GET](/doc/controllers/order-notes-api.md#order-notes-info-get)
* [Order Notes by Pk DELETE](/doc/controllers/order-notes-api.md#order-notes-by-pk-delete)
* [Order Notes by Pk GET](/doc/controllers/order-notes-api.md#order-notes-by-pk-get)
* [Order Notes by Pk PUT](/doc/controllers/order-notes-api.md#order-notes-by-pk-put)


# Order Notes GET

Get a list of models

```python
def order_notes_get(self)
```

## Response Type

[`OrderNotesResponse`](/doc/models/order-notes-response.md)

## Example Usage

```python
result = order_notes_api_controller.order_notes_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Notes POST

```python
def order_notes_post(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrderNotesApiPost`](/doc/models/order-notes-api-post.md) | Body, Required | Model schema |

## Response Type

[`OrderNotesResponse1`](/doc/models/order-notes-response-1.md)

## Example Usage

```python
body = OrderNotesApiPost()
body.note = 'note8'

result = order_notes_api_controller.order_notes_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Notes Info GET

Get metadata information about this API resource

```python
def order_notes_info_get(self)
```

## Response Type

[`OrderNotesInfoResponse`](/doc/models/order-notes-info-response.md)

## Example Usage

```python
result = order_notes_api_controller.order_notes_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Notes by Pk DELETE

```python
def order_notes_by_pk_delete(self,
                            pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`OrderNotesResponse2`](/doc/models/order-notes-response-2.md)

## Example Usage

```python
pk = 200

result = order_notes_api_controller.order_notes_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Notes by Pk GET

Get an item model

```python
def order_notes_by_pk_get(self,
                         pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`OrderNotesResponse3`](/doc/models/order-notes-response-3.md)

## Example Usage

```python
pk = 200

result = order_notes_api_controller.order_notes_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Order Notes by Pk PUT

```python
def order_notes_by_pk_put(self,
                         pk,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`OrderNotesApiPut`](/doc/models/order-notes-api-put.md) | Body, Required | Model schema |

## Response Type

[`OrderNotesResponse4`](/doc/models/order-notes-response-4.md)

## Example Usage

```python
pk = 200
body = OrderNotesApiPut()
body.note = 'note8'

result = order_notes_api_controller.order_notes_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

