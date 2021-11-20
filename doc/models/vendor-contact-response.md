
# Vendor Contact Response

## Structure

`VendorContactResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `float` | Optional | The total record count on the backend |
| `description_columns` | [`DescriptionColumns`](/doc/models/description-columns.md) | Optional | - |
| `ids` | `List of string` | Optional | A list of item ids, useful when you don't know the column id |
| `label_columns` | [`LabelColumns`](/doc/models/label-columns.md) | Optional | - |
| `list_columns` | `List of string` | Optional | A list of columns |
| `list_title` | `string` | Optional | A title to render. Will be translated by babel |
| `order_columns` | `List of string` | Optional | A list of allowed columns to sort |
| `result` | [`List of VendorContactApiGetList`](/doc/models/vendor-contact-api-get-list.md) | Optional | The result from the get list query |

## Example (as JSON)

```json
{
  "count": null,
  "description_columns": null,
  "ids": null,
  "label_columns": null,
  "list_columns": null,
  "list_title": null,
  "order_columns": null,
  "result": null
}
```

