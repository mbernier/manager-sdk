
# Products Api Put

## Structure

`ProductsApiPut`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_photos` | `string` | Optional | - |
| `handle` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `options` | `string` | Optional | - |
| `orders` | `List of object` | Optional | - |
| `product_notes` | `List of object` | Optional | - |
| `product_type` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `seo_description` | `string` | Optional | - |
| `seo_name` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `tags` | `string` | Optional | - |
| `variations` | `string` | Optional | - |
| `vendor` | `object` | Optional | - |
| `vendor_photos` | `string` | Optional | - |
| `vendor_product_options` | `object` | Optional | - |
| `vendor_shipping` | `object` | Optional | - |
| `vendor_sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `vendor_url` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `websites` | `List of object` | Optional | - |

## Example (as JSON)

```json
{
  "customer_photos": null,
  "handle": "handle6",
  "name": "name0",
  "options": null,
  "orders": null,
  "product_notes": null,
  "product_type": null,
  "seo_description": null,
  "seo_name": null,
  "sku": "sku4",
  "tags": null,
  "variations": null,
  "vendor": null,
  "vendor_photos": null,
  "vendor_product_options": null,
  "vendor_shipping": null,
  "vendor_sku": "vendor_sku8",
  "vendor_url": "vendor_url4",
  "websites": null
}
```

