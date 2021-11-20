
# Security Login Request

## Structure

`SecurityLoginRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `string` | Optional | The password for authentication |
| `provider` | [`ProviderEnum`](/doc/models/provider-enum.md) | Optional | Choose an authentication provider |
| `refresh` | `bool` | Optional | If true a refresh token is provided also |
| `username` | `string` | Optional | The username for authentication |

## Example (as JSON)

```json
{
  "password": null,
  "provider": null,
  "refresh": null,
  "username": null
}
```

