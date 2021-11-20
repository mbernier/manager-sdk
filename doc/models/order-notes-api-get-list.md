
# Order Notes Api Get List

## Structure

`OrderNotesApiGetList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `order_id` | `int` | Required | - |
| `mtype` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "note": "note4",
  "order_id": 46,
  "type": null
}
```

