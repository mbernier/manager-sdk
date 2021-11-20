
# Vendor Api Get User

## Structure

`VendorApiGetUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | - |
| `changed_on` | `datetime` | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `email` | `string` | Required | **Constraints**: *Maximum Length*: `64` |
| `fail_login_count` | `int` | Optional | - |
| `first_name` | `string` | Required | **Constraints**: *Maximum Length*: `64` |
| `id` | `int` | Optional | - |
| `last_login` | `datetime` | Optional | - |
| `last_name` | `string` | Required | **Constraints**: *Maximum Length*: `64` |
| `login_count` | `int` | Optional | - |
| `password` | `string` | Optional | **Constraints**: *Maximum Length*: `256` |
| `username` | `string` | Required | **Constraints**: *Maximum Length*: `64` |

## Example (as JSON)

```json
{
  "active": null,
  "changed_on": null,
  "created_on": null,
  "email": "email6",
  "fail_login_count": null,
  "first_name": "first_name0",
  "id": null,
  "last_login": null,
  "last_name": "last_name8",
  "login_count": null,
  "password": null,
  "username": "username0"
}
```

