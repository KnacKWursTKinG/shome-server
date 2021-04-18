/*jshint esversion: 6*/
/*global $*/
/*global panel, SetupPopup*/
/*global document, console, window*/
'use strict';


const screen = {
  route: {
    pi: {
      on: function (id, success, error) {
        // <<- ajax call on '/pi/on'
        $.ajax({
          type: 'POST',
          url: 'pi/on',
          data: JSON.stringify({
            id: id
          }),
          contentType: 'application/json',
          success: success,
          error: error
        });
        // ->>
      },
      off: function (id, success, error) {
        // <<- ajax call on '/pi/off'
        $.ajax({
          type: 'POST',
          url: 'pi/off',
          data: JSON.stringify({
            id: id
          }),
          contentType: 'application/json',
          success: success,
          error: error
        });
        // ->>
      },
      get: function (id, success, error) {
        // <<- ajax call on '/pi/get'
        $.ajax({
          type: 'POST',
          url: 'pi/get',
          data: JSON.stringify({
            id: id
          }),
          contentType: 'application/json',
          success: success,
          error: error
        });
        // ->>
      },
    },

    html: {
      category: function (category, success, error) {
        // <<- ajax call on '/html/category/<category>'
        category = category.toLowerCase();

        $.ajax({
          type: 'GET',
          url: '/html/category/' + category,
          success: success,
          error: error
        });
        // ->>
      }
    },

    cache: {
      get: function (id, success, error) {
        // <<- ajax call on 'GET /cache'
        $.ajax({
          type: 'GET',
          url: '/cache',
          data: {id: id},
          success: success,
          error: error
        });
        // ->>
      },
      post: function (id, data, success, error) {
        // <<- ajax call on 'POST /cache'
        data.id = id;
        $.ajax({
          type: 'POST',
          url: '/cache',
          data: JSON.stringify(data),
          contentType: 'application/json',
          success: success,
          error: error
        });
        // ->>
      },
    }
  },

  power: {
    click: function () {
      // <<- Enable on & off buttons
      // run check power
      // '.control-element .toggle' onclick event
      this.check();

      // event for turn on/off lights
      $('.screen .control-element .toggle').click(function () {
        var id = $(this).parent().parent().attr('id');

        var powerOff = $(`#${id} .off`);
        var powerOn = $(`#${id} .on`);

        // disable buttons
        powerOn.prop('disabled', true);
        powerOff.prop('disabled', true);

        if (powerOff.hasClass('check') && $(this).hasClass('on')) {
          /* ON button clicked while OFF is checked*/
          screen.route.pi.on(
            id,
            function () {
              // uncheck OFF
              powerOff.removeClass('check');
              powerOff.addClass('uncheck');

              // check ON
              powerOn.removeClass('uncheck');
              powerOn.addClass('check');

              // enable buttons
              powerOn.prop('disabled', false);
              powerOff.prop('disabled', false);
            },
            function () {
              // enable buttons
              powerOn.prop('disabled', false);
              powerOff.prop('disabled', false);
            }
          );
        } else if (powerOn.hasClass('check') && $(this).hasClass('off')) {
          /* OFF button clicked while ON is checked*/
          screen.route.pi.off(
            id,
            function () {
              // uncheck ON
              powerOn.removeClass('check');
              powerOn.addClass('uncheck');

              // check OFF
              powerOff.removeClass('uncheck');
              powerOff.addClass('check');

              // enable buttons
              powerOn.prop('disabled', false);
              powerOff.prop('disabled', false);
            },
            function () {
              // enable buttons
              powerOn.prop('disabled', false);
              powerOff.prop('disabled', false);
            }
          );
        }
      });
      // ->>
    },

    check: function () {
      // <<- check if power is ON or OFF and set css classes '.check' && '.uncheck'
      // NOTE: iter '.control-element' in '.screen .main', get 'id', get '/api/pi_rgb/get' data
      $('.screen .main').children().each(function (idx, child) {
        let id = $(child).attr('id');

        let host = id.split('--', 1)[0];
        let section = id.split('--', 2)[1];

        var powerOn = $(`#${id} .on`);
        var powerOff = $(`#${id} .off`);

        screen.route.pi.get(
          id,
          function (rgbw) {
            if (rgbw.length > 1) {
              // groups
              let isOff = 0;
              let isOn = 0;

              rgbw.forEach(function (rgbw, idx) {
                if ( `${rgbw}` == `0,0,0,0` || `${rgbw}` == `0,0,0` ) {
                  isOff++;
                } else {
                  isOn++;
                }
              });

              if (isOn > 0 && isOff == 0) {
                // power is on
                rgbw = rgbw[0];
              } else {
                // power is off
                rgbw = [0, 0, 0, 0];
              }
            }

            if ( rgbw ) {
              if ( `${rgbw}` == `0,0,0,0` || `${rgbw}` == `0,0,0` ) {
                // is off
                powerOn.addClass('uncheck');
                powerOn.removeClass('check');
                powerOff.addClass('check');
                powerOff.removeClass('uncheck');

              } else {
                // is on
                powerOn.addClass('check');
                powerOn.removeClass('uncheck');
                powerOff.addClass('uncheck');
                powerOff.removeClass('check');
              }

              powerOn.removeClass('offline');
              powerOff.removeClass('offline');
            }
          },
          function (err) {
            console.error(err.responseText);
            throw err;
          }
        );
      });
      // ->>
    },
  },

  setup: {
    click: function () {
      // <<- onclick event on `#${id} .setup` for open a popup
      // NOTE: change name, rgbw, warmWhite [default: 'auto']
      $('.screen .control-element .setup').click(function () {
        const el = $(this);
        let id = el.parent().attr('id');  // NOTE: '<host>--<section>' || '<group>--group'
        let name = el.text(); // NOTE: '<host>:<section>' || '<group>'

        if (screen.popup[id]) {
          screen.popup[id].open();
        } else {
          let popup = new SetupPopup({
            id: id,
            name: name
          });

          popup.open();
        }
      });
      // ->>
    }
  },

  // NOTE: storage for created popup objects
  popup: {}
};


$(document).ready(function () {
  requestCategory(panel.active);
  panel.close();
});


function requestCategory(category) {
  screen.route.html.category(
    category,
    function (data) {
      $('.screen .main').html(data);
      screen.power.click();
      screen.setup.click();
    }
  );
}
