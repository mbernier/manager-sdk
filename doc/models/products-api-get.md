
# Products Api Get

## Structure

`ProductsApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_photos` | `string` | Optional | - |
| `handle` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `options` | `string` | Optional | - |
| `orders` | [`ProductsApiGetOrderProducts`](/doc/models/products-api-get-order-products.md) | Required | - |
| `product_notes` | [`ProductsApiGetProductNotes`](/doc/models/products-api-get-product-notes.md) | Required | - |
| `product_type` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `seo_description` | `string` | Optional | - |
| `seo_name` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `tags` | `string` | Optional | - |
| `variations` | `string` | Optional | - |
| `vendor` | [`ProductsApiGetVendor`](/doc/models/products-api-get-vendor.md) | Optional | - |
| `vendor_photos` | `string` | Optional | - |
| `vendor_product_options` | [`ProductsApiGetVendorProductOptions`](/doc/models/products-api-get-vendor-product-options.md) | Optional | - |
| `vendor_shipping` | [`ProductsApiGetVendorShipping`](/doc/models/products-api-get-vendor-shipping.md) | Optional | - |
| `vendor_sku` | `string` | Required | **Constraints**: *Maximum Length*: `200` |
| `vendor_url` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `websites` | [`ProductsApiGetWebsitesProducts`](/doc/models/products-api-get-websites-products.md) | Required | - |

## Example (as JSON)

```json
{
  "customer_photos": null,
  "handle": "handle6",
  "name": "name0",
  "options": null,
  "orders": {
    "changed_on": null,
    "created_on": null
  },
  "product_notes": {
    "action_type": null,
    "changed_on": null,
    "created_on": null,
    "id": null,
    "note": "note6"
  },
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
  "websites": {
    "changed_on": null,
    "created_on": null
  }
}
```

