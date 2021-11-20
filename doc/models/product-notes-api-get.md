
# Product Notes Api Get

## Structure

`ProductNotesApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_type` | `string` | Optional | **Constraints**: *Maximum Length*: `100` |
| `changed_by` | [`ProductNotesApiGetUser`](/doc/models/product-notes-api-get-user.md) | Required | - |
| `changed_on` | `datetime` | Optional | - |
| `created_by` | [`ProductNotesApiGetUser`](/doc/models/product-notes-api-get-user.md) | Required | - |
| `created_on` | `datetime` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `products` | [`ProductNotesApiGetProducts`](/doc/models/product-notes-api-get-products.md) | Required | - |

## Example (as JSON)

```json
{
  "action_type": null,
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
  "note": "note4",
  "products": {
    "customer_photos": null,
    "handle": "handle8",
    "id": null,
    "name": "name2",
    "options": null,
    "product_type": null,
    "seo_description": null,
    "seo_name": null,
    "sku": "sku2",
    "tags": null,
    "variations": null,
    "vendor_photos": null,
    "vendor_sku": "vendor_sku6",
    "vendor_url": "vendor_url6"
  }
}
```

