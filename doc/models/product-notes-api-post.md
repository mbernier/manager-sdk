
# Product Notes Api Post

## Structure

`ProductNotesApiPost`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_type` | `string` | Optional | **Constraints**: *Maximum Length*: `100` |
| `changed_by` | `object` | Optional | - |
| `changed_on` | `datetime` | Optional | - |
| `created_by` | `object` | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `products` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "action_type": null,
  "changed_by": null,
  "changed_on": null,
  "created_by": null,
  "created_on": null,
  "note": "note4",
  "products": null
}
```

