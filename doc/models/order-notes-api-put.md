
# Order Notes Api Put

## Structure

`OrderNotesApiPut`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | `object` | Optional | - |
| `changed_by` | `object` | Optional | - |
| `changed_on` | `datetime` | Optional | - |
| `created_by` | `object` | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `note` | `string` | Required | **Constraints**: *Maximum Length*: `100` |
| `mtype` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "Order": null,
  "changed_by": null,
  "changed_on": null,
  "created_by": null,
  "created_on": null,
  "note": "note4",
  "type": null
}
```

