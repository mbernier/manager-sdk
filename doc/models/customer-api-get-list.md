
# Customer Api Get List

## Structure

`CustomerApiGetList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `email` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `id` | `int` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `phone` | `string` | Required | **Constraints**: *Maximum Length*: `12` |
| `shipping_address` | `string` | Required | **Constraints**: *Maximum Length*: `250` |

## Example (as JSON)

```json
{
  "billing_address": "billing_address8",
  "email": "email6",
  "id": null,
  "name": "name0",
  "phone": "phone0",
  "shipping_address": "shipping_address0"
}
```

