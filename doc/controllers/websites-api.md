# Websites Api

```python
websites_api_controller = client.websites_api
```

## Class Name

`WebsitesApiController`

## Methods

* [Websites GET](/doc/controllers/websites-api.md#websites-get)
* [Websites POST](/doc/controllers/websites-api.md#websites-post)
* [Websites Info GET](/doc/controllers/websites-api.md#websites-info-get)
* [Websites by Pk DELETE](/doc/controllers/websites-api.md#websites-by-pk-delete)
* [Websites by Pk GET](/doc/controllers/websites-api.md#websites-by-pk-get)
* [Websites by Pk PUT](/doc/controllers/websites-api.md#websites-by-pk-put)


# Websites GET

Get a list of models

```python
def websites_get(self)
```

## Response Type

[`WebsitesResponse`](/doc/models/websites-response.md)

## Example Usage

```python
result = websites_api_controller.websites_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Websites POST

```python
def websites_post(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebsitesApiPost`](/doc/models/websites-api-post.md) | Body, Required | Model schema |

## Response Type

[`WebsitesResponse1`](/doc/models/websites-response-1.md)

## Example Usage

```python
body = WebsitesApiPost()
body.name = 'name6'
body.shopify_prefix = 'shopify_prefix6'
body.url = 'url0'

result = websites_api_controller.websites_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Websites Info GET

Get metadata information about this API resource

```python
def websites_info_get(self)
```

## Response Type

[`WebsitesInfoResponse`](/doc/models/websites-info-response.md)

## Example Usage

```python
result = websites_api_controller.websites_info_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Websites by Pk DELETE

```python
def websites_by_pk_delete(self,
                         pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`WebsitesResponse2`](/doc/models/websites-response-2.md)

## Example Usage

```python
pk = 200

result = websites_api_controller.websites_by_pk_delete(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Websites by Pk GET

Get an item model

```python
def websites_by_pk_get(self,
                      pk)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |

## Response Type

[`WebsitesResponse3`](/doc/models/websites-response-3.md)

## Example Usage

```python
pk = 200

result = websites_api_controller.websites_by_pk_get(pk)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Websites by Pk PUT

```python
def websites_by_pk_put(self,
                      pk,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pk` | `int` | Template, Required | - |
| `body` | [`WebsitesApiPut`](/doc/models/websites-api-put.md) | Body, Required | Model schema |

## Response Type

[`WebsitesResponse4`](/doc/models/websites-response-4.md)

## Example Usage

```python
pk = 200
body = WebsitesApiPut()
body.name = 'name6'
body.shopify_prefix = 'shopify_prefix6'
body.url = 'url0'

result = websites_api_controller.websites_by_pk_put(pk, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 404 | Not found | [`M400Exception`](/doc/models/m400-exception.md) |
| 422 | Could not process entity | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

