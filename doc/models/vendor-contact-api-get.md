
# Vendor Contact Api Get

## Structure

`VendorContactApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_for_new_orders` | `bool` | Optional | - |
| `email` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `phone` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `vendor` | [`VendorContactApiGetVendor`](/doc/models/vendor-contact-api-get-vendor.md) | Optional | - |

## Example (as JSON)

```json
{
  "contact_for_new_orders": null,
  "email": "email6",
  "name": "name0",
  "phone": "phone0",
  "vendor": null
}
```

