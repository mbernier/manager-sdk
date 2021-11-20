
# Order Notes Api Get

## Structure

`OrderNotesApiGet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`OrderNotesApiGetOrder`](/doc/models/order-notes-api-get-order.md) | Required | - |
| `changed_by` | [`OrderNotesApiGetUser`](/doc/models/order-notes-api-get-user.md) | Required | - |
| `changed_on` | `datetime` | Optional | - |
| `created_by` | [`OrderNotesApiGetUser`](/doc/models/order-notes-api-get-user.md) | Required | - |
| `created_on` | `datetime` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `mtype` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "Order": {
    "changed_on": null,
    "created_on": null,
    "customer_order_total": null,
    "customer_shipping_price": null,
    "id": null,
    "product_costs": null,
    "profit": null,
    "shipping_cost": null,
    "status": null,
    "website_order_id": 76
  },
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
  "type": null
}
```

