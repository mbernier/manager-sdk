# Security

```python
security_controller = client.security
```

## Class Name

`SecurityController`

## Methods

* [Security Login POST](/doc/controllers/security.md#security-login-post)
* [Security Refresh POST](/doc/controllers/security.md#security-refresh-post)


# Security Login POST

Authenticate and get a JWT access and refresh token

```python
def security_login_post(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SecurityLoginRequest`](/doc/models/security-login-request.md) | Body, Required | - |

## Response Type

[`SecurityLoginResponse`](/doc/models/security-login-response.md)

## Example Usage

```python
body = SecurityLoginRequest()
result = security_controller.security_login_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`M400Exception`](/doc/models/m400-exception.md) |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |


# Security Refresh POST

Use the refresh token to get a new JWT access token

```python
def security_refresh_post(self)
```

## Response Type

[`SecurityRefreshResponse`](/doc/models/security-refresh-response.md)

## Example Usage

```python
result = security_controller.security_refresh_post()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |
| 500 | Fatal error | [`M400Exception`](/doc/models/m400-exception.md) |

