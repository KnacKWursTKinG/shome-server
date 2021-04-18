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


## MRAV: *'~/.config/plugins/mpv'*

> MPV-Player Network Control plugin<br/>
> '*https://github.com/jaseg/python-mpv*'


* Client -> Server:
  * **Type**: pickle/bytes
  * __*mpv_data*__: `tuple["mpv.MPV attribute name", Optional["args"], Optional["kwargs"]]`


* Server -> Client:
  * **Type**: pickle/bytes
  * __*return*__: `Any`


 Type | Route | Description | Client | Server
:----:|:------|:-----------:|:-------|:------
POST  | /api/mrav/ | python-mpv control | __*mpv_data*__ | __*return*__


### Examples

__*@TODO* ...__
