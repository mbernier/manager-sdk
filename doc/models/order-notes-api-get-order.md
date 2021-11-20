
# Order Notes Api Get Order

## Structure

`OrderNotesApiGetOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `changed_on` | `datetime` | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `customer_order_total` | `float` | Optional | - |
| `customer_shipping_price` | `float` | Optional | - |
| `id` | `int` | Optional | - |
| `product_costs` | `float` | Optional | - |
| `profit` | `float` | Optional | - |
| `shipping_cost` | `float` | Optional | - |
| `status` | [`StatusEnum`](/doc/models/status-enum.md) | Optional | **Constraints**: *Maximum Length*: `19` |
| `website_order_id` | `int` | Required | - |

## Example (as JSON)

```json
{
  "changed_on": null,
  "created_on": null,
  "customer_order_total": null,
  "customer_shipping_price": null,
  "id": null,
  "product_costs": null,
  "profit": null,
  "shipping_cost": null,
  "status": null,
  "website_order_id": 8
}
```

