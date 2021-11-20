
# Websites Api Get List

## Structure

`WebsitesApiGetList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `string` | Optional | **Constraints**: *Maximum Length*: `200` |
| `api_secret` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `id` | `int` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `private_app_password` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `shopify_prefix` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `url` | `string` | Required | **Constraints**: *Maximum Length*: `150` |

## Example (as JSON)

```json
{
  "api_key": null,
  "api_secret": null,
  "id": null,
  "name": "name0",
  "private_app_password": null,
  "shopify_prefix": "shopify_prefix0",
  "url": "url4"
}
```

