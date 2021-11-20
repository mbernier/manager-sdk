
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `access_token` | `string` | The OAuth 2.0 Access Token to use for API requests. |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from manager.manager_client import ManagerClient
from manager.configuration import Environment

client = ManagerClient(
    access_token='AccessToken',
    environment=Environment.PRODUCTION,)
```

## BDFS Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| customer_api | Gets CustomerApiController |
| menu | Gets MenuController |
| open_api | Gets OpenApiController |
| order_api | Gets OrderApiController |
| order_notes_api | Gets OrderNotesApiController |
| product_notes_api | Gets ProductNotesApiController |
| products_api | Gets ProductsApiController |
| security | Gets SecurityController |
| vendor_api | Gets VendorApiController |
| vendor_contact_api | Gets VendorContactApiController |
| vendor_product_options_api | Gets VendorProductOptionsApiController |
| vendor_shipping_api | Gets VendorShippingApiController |
| websites_api | Gets WebsitesApiController |

