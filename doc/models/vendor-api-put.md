
# Vendor Api Put

## Structure

`VendorApiPut`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Optional | **Constraints**: *Maximum Length*: `564` |
| `changed_by` | `object` | Optional | - |
| `changed_on` | `datetime` | Optional | - |
| `contacts` | `List of object` | Optional | - |
| `corporate_phone` | `string` | Optional | **Constraints**: *Maximum Length*: `15` |
| `created_by` | `object` | Optional | - |
| `created_on` | `datetime` | Optional | - |
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
  "changed_by": null,
  "changed_on": null,
  "contacts": null,
  "corporate_phone": null,
  "created_by": null,
  "created_on": null,
  "markup": null,
  "name": "name0",
  "support_email": null,
  "support_phone": null,
  "url": null,
  "vendor_is_manufacturer": null
}
```

