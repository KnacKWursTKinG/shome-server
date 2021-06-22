# Flask Routes Overview


## Pi RGB API: *'~/.config/plugins/py_rgb'*

* **Type**: json

* **Data**:
  * __*sections*__: `list[str or int]`
  * __*rgbw*__: `Union[tuple[int, int, int], tuple[int, int, int]]`


 Type | Route | Description | Client | Server
:----:|:------|:-----------:|:-------|:------
POST  | /api/pi\_rgb/set | set __*rgbw*__ for __*sections*__  | __*rgbw*__<br/>__*sections*__ | -
POST  | /api/pi\_rgb/get | get __*rgbw*__ from __*sections*__ | __*sections*__              | `list[`__*rgbw*__`]`
POST  | /api/pi\_rgb/on  | turn on __*sections*__             | __*sections*__              | -
POST  | /api/pi\_rgb/off | turn off __*sections*__            | __*sections*__              | -


## MRAV: *'~/.config/plugins/nmpv'*

> MPV-Player Network Control plugin<br/>
> '*https://github.com/jaseg/python-mpv*'


### Client -> Server:
#### **Type**: application/json
#### __*mpv_data*__: 

> run method

```json
{
  "sync": null,
  "attr": "new",
  "args": [],
  "kwargs": {
    "ytdl": true
  }
}
```

> set property

```json
{
  "sync": null,
  "attr": "new",
  "value": "..."
}
```

> get property

```json
{
  "sync": null,
  "attr": "new"
}
```


### Server -> Client:
#### **Type**: application/json
#### __*return*__: json method/property return or error message


 Type | Route | Description | Client | Server
:----:|:------|:-----------:|:-------|:------
POST  | /api/nmpv/player | python-mpv control | __*mpv_data*__ | __*return*__


### Examples

__*@TODO* ...__
