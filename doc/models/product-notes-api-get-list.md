
# Product Notes Api Get List

## Structure

`ProductNotesApiGetList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_type` | `string` | Optional | **Constraints**: *Maximum Length*: `100` |
| `id` | `int` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `products_id` | `int` | Required | - |

## Example (as JSON)

```json
{
  "action_type": null,
  "id": null,
  "note": "note4",
  "products_id": 244
}
```

