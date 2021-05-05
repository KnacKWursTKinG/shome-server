# nmpvc: Network-MPV-Client

* Module
  * stream (stream local file or online stream to player with flask)

    * Stream
      * file
      * youtube
      * twitch
      * else (takes video/audio download/stream url)

  * player (main class for player control)

    * Player
      * pl/playlist
      * play
      * append
      * remove
      * play_next
      * play_prev
      * play_index
      * ...

  * base (`mpv.MPV` setters and getters)

    * NetMPVControlHelp (list with available methods/attribute)
      * methods
      * attr (with defaults)

    * NetMPVControlBase (checks PlayerHelp before sending to nmpv plugin)
      * set (set attr)
      * get (get attr)
      * run (run method)

* Client (term)
  * ...
