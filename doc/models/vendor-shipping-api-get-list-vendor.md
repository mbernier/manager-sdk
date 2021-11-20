
# Vendor Shipping Api Get List Vendor

## Structure

`VendorShippingApiGetListVendor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Optional | **Constraints**: *Maximum Length*: `564` |
| `changed_on` | `datetime` | Optional | - |
| `corporate_phone` | `string` | Optional | **Constraints**: *Maximum Length*: `15` |
| `created_on` | `datetime` | Optional | - |
| `id` | `int` | Optional | - |
| `markup` | `float` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `support_email` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `support_phone` | `string` | Optional | **Constraints**: *Maximum Length*: `15` |
| `url` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `vendor_is_manufacturer` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "address": null,
  "changed_on": null,
  "corporate_phone": null,
  "created_on": null,
  "id": null,
  "markup": null,
  "name": "name0",
  "support_email": null,
  "support_phone": null,
  "url": null,
  "vendor_is_manufacturer": null
}
```

