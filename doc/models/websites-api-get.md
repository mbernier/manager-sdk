
# Websites Api Get

## Structure

`WebsitesApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `string` | Optional | **Constraints**: *Maximum Length*: `200` |
| `api_secret` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `private_app_password` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `products` | [`WebsitesApiGetWebsitesProducts`](/doc/models/websites-api-get-websites-products.md) | Required | - |
| `shopify_prefix` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `url` | `string` | Required | **Constraints**: *Maximum Length*: `150` |

## Example (as JSON)

```json
{
  "api_key": null,
  "api_secret": null,
  "name": "name0",
  "private_app_password": null,
  "products": {
    "changed_on": null,
    "created_on": null
  },
  "shopify_prefix": "shopify_prefix0",
  "url": "url4"
}
```

