
# Vendor Api Get

## Structure

`VendorApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Optional | **Constraints**: *Maximum Length*: `564` |
| `changed_by` | [`VendorApiGetUser`](/doc/models/vendor-api-get-user.md) | Required | - |
| `changed_on` | `datetime` | Optional | - |
| `contacts` | [`VendorApiGetVendorContact`](/doc/models/vendor-api-get-vendor-contact.md) | Required | - |
| `corporate_phone` | `string` | Optional | **Constraints**: *Maximum Length*: `15` |
| `created_by` | [`VendorApiGetUser`](/doc/models/vendor-api-get-user.md) | Required | - |
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
  "changed_by": {
    "active": null,
    "changed_on": null,
    "created_on": null,
    "email": "email8",
    "fail_login_count": null,
    "first_name": "first_name8",
    "id": null,
    "last_login": null,
    "last_name": "last_name6",
    "login_count": null,
    "password": null,
    "username": "username8"
  },
  "changed_on": null,
  "contacts": {
    "contact_for_new_orders": null,
    "email": "email8",
    "id": null,
    "name": "name8",
    "phone": "phone2"
  },
  "corporate_phone": null,
  "created_by": {
    "active": null,
    "changed_on": null,
    "created_on": null,
    "email": "email4",
    "fail_login_count": null,
    "first_name": "first_name2",
    "id": null,
    "last_login": null,
    "last_name": "last_name0",
    "login_count": null,
    "password": null,
    "username": "username8"
  },
  "created_on": null,
  "markup": null,
  "name": "name0",
  "support_email": null,
  "support_phone": null,
  "url": null,
  "vendor_is_manufacturer": null
}
```

