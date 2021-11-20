
# Vendor Product Options Api Get

## Structure

`VendorProductOptionsApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `handle_generation` | `string` | Optional | - |
| `options` | `string` | Optional | - |
| `product_type` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `sku_generation` | `string` | Optional | - |
| `variations` | `string` | Optional | - |
| `vendor` | [`VendorProductOptionsApiGetVendor`](/doc/models/vendor-product-options-api-get-vendor.md) | Optional | - |

## Example (as JSON)

```json
{
  "handle_generation": null,
  "options": null,
  "product_type": "product_type4",
  "sku_generation": null,
  "variations": null,
  "vendor": null
}
```

