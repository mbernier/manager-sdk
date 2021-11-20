
# Product Notes Api Get Products

## Structure

`ProductNotesApiGetProducts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_photos` | `string` | Optional | - |
| `handle` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `id` | `int` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `options` | `string` | Optional | - |
| `product_type` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `seo_description` | `string` | Optional | - |
| `seo_name` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `tags` | `string` | Optional | - |
| `variations` | `string` | Optional | - |
| `vendor_photos` | `string` | Optional | - |
| `vendor_sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `vendor_url` | `string` | Required | **Constraints**: *Maximum Length*: `250` |

## Example (as JSON)

```json
{
  "customer_photos": null,
  "handle": "handle6",
  "id": null,
  "name": "name0",
  "options": null,
  "product_type": null,
  "seo_description": null,
  "seo_name": null,
  "sku": "sku4",
  "tags": null,
  "variations": null,
  "vendor_photos": null,
  "vendor_sku": "vendor_sku8",
  "vendor_url": "vendor_url4"
}
```

