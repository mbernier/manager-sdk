
# Vendor Shipping Api Post

## Structure

`VendorShippingApiPost`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `markup_shipping` | `bool` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `options` | `string` | Optional | - |
| `shipping_markup_amount` | `float` | Optional | - |
| `shipping_variable` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `vendor` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "markup_shipping": null,
  "name": "name0",
  "options": null,
  "shipping_markup_amount": null,
  "shipping_variable": "shipping_variable8",
  "vendor": null
}
```

