# Menu

```python
menu_controller = client.menu
```

## Class Name

`MenuController`


# Menu GET

Get the menu data structure. Returns a forest like structure with the menu the user has access to

```python
def menu_get(self)
```

## Response Type

[`MenuResponse`](/doc/models/menu-response.md)

## Example Usage

```python
result = menu_controller.menu_get()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`M400Exception`](/doc/models/m400-exception.md) |

