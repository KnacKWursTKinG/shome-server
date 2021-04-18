# Flask Routes Overview


## Pi RGB API: *'~/.config/plugins/py_rgb'*

* Server Returns:
  * Status Code [200]: `json.dumps(dict(...)) or None`
  * Else: `str(error_message)`
<br/><br/>
* Json Data:
  * __*sections*__: `list[str or int]`
  * __*rgbw*__: `list[int]`


 Type | Route | Description | Client | Server
:----:|:------|:-----------:|:-------|:------
POST  | /api/pi\_rgb/set | set __*rgbw*__ for __*sections*__  | __*rgbw*__<br/>__*sections*__ | -
POST  | /api/pi\_rgb/get | get __*rgbw*__ from __*sections*__ | __*sections*__              | `list[rgbw, ...]`<br/>Note: sections[0] = list[0]
POST  | /api/pi\_rgb/on  | turn on __*sections*__             | __*sections*__              | -
POST  | /api/pi\_rgb/off | turn off __*sections*__            | __*sections*__              | -


## MRAV: *'~/.config/plugins/mpv'*

> MPV-Player Network Control plugin<br/>
> '*https://github.com/jaseg/python-mpv*'


# TODO: some examples

# NOTE: just some thoughts here
* Client to Server: [ data-type: *pickle/bytes* ]
  * __*func*__: python function
    * Example:
    ```Python
    def play(self):
      player = self.MPV(ytdl=True)
      player.play('https://youtu.be/DOmdB7D-pUU')
      player.wait_for_playback()
    ```
  * __*log-level*__: mpv-player log level for __*output*__


* Server to Client: [ data-type: *pickle/bytes* ]
  * __*return*__: *func* return
  * __*output*__: mpv-player *output* if available


 Type | Route | Description | Client | Server
:----:|:------|:-----------:|:-------|:------
POST  | /api/mrav/ | python-mpv control | __*func*__ | __*return*__<br/>__*output*__
