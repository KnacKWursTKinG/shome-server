/*jshint esversion: 6*/
/*global $, console, screen, requestCategory, panel*/
'use strict';


function SetupPopup(obj) {
  this.id = obj.id;
  this.name = obj.name;

  this.html = `
    <div onclick="event.cancelBubble=true;" class="main element">
      <input class="label" type="text" value="${this.name}">
      <div class="rgbw">
        <input class="required rgbw-input" type="number" placeholder="R" size="3" min="0" max="255" required>
        <input class="required rgbw-input" type="number" placeholder="G" size="3" min="0" max="255" required>
        <input class="required rgbw-input" type="number" placeholder="B" size="3" min="0" max="255" required>
      </div>
      <div onclick="screen.popup['${this.id}'].save();" class="button">Save</div>
    </div>
  `;

  this.display = 'flex';

  if (screen.popup[this.id]) {
    $(`#popup--${this.id}`).remove();
  }

  $('.screen').after(`
    <div onclick="screen.popup['${this.id}'].close();" id="popup--${this.id}" class="popup-container">
      <div class="popup">
        ${this.html}
      </div>
    </div>
  `);

  $(`.popup .main .required.rgbw-input`).on('input', function () {
    let el = $(this);

    if (el.val() <= Number(el.attr('max')) && el.val() >= Number(el.attr('min'))) {
      el.css('background-color', 'var(--popup-rgbw-bg-color-accept)');
    } else {
      el.css('background-color', 'var(--popup-rgbw-bg-color-wrong)');
    }
  });

  screen.popup[this.id] = this;
}


SetupPopup.prototype.css = function (key, value) {
  return $(`#popup--${this.id}`).css(key, value);
};


SetupPopup.prototype.open = function () {
  this.load();
  this.css('display', this.display);
};


SetupPopup.prototype.close = function () {
  this.css('display', 'none');
};


SetupPopup.prototype.save = function (append=true) {
  // <<-  save `#popup--${this.id} .main .rgbw` to cache
  const rgbw = $(`#popup--${this.id} .main .rgbw`);
  const id = this.id;

  let name = $(`#popup--${this.id} .main .label`).val();
  let rgb = [];
  let err = 0;

  rgbw.children().each(function (idx, child) {
    let val = $(child).val();

    if (!val) {
      val = 0;
      err++;
    } else {
      val = Number(val);

      if (val < 0 || val > 255) {
        throw `rgb value: ${val} not in range [range: 0-255]`;
      }
    }

    rgb.push(Number(val));
  });

  if (err >= 3 || rgb == '0,0,0') {
    rgb = undefined;
  }

  let data = {
    name: name
  };

  if (rgb) {
    data.append = append;
    data.rgb = rgb;
  }

  screen.route.cache.post(
    id,
    data,
    function () {
      requestCategory(panel.active);
      // add rgb to '#popup-${id} .cache'
      if (rgb) {
        screen.popup[id].load();
      }
    },
    function (err) {
      console.error(err.responseText);
      throw err;
    }
  );
  // ->>
};


SetupPopup.prototype.load = function () {  // NOTE: '<host>--<section>'
  // <<- load rgb cache to `#popup--${id} .popup .cache`
  const id = this.id;

  screen.route.cache.get(
    id,

    // success callback
    function (data) {
      // <<- '#popup--${id} .popup .cache' create rgbw cache popup
      // clear '.cache' popup content and create new
      $(`#popup--${id} .popup .cache`).remove();

      if (data.rgbw.length > 0) {
        let html = `
          <div onclick="event.cancelBubble=true;" class="cache element">
        `;

        for (let idx = 0; idx < data.rgbw.length; idx++) {
          let r = data.rgbw[idx][0];
          let g = data.rgbw[idx][1];
          let b = data.rgbw[idx][2];

          if (idx > 0) {
            if (r == data.rgbw[idx - 1][0] &&
                g == data.rgbw[idx - 1][1] &&
                b == data.rgbw[idx - 1][2]) {
              continue;
            }
          }

          html += `
            <div onclick="screen.popup['${id}'].set(${r}, ${g}, ${b})"
            style="background-color:rgba(${r},${g},${b});" class="element">
              <div class="rgb">${r}, ${g}, ${b}</div>
            </div>
          `;
        }

        html += `</div>`;

        $(`#popup--${id} .popup .main`).before(html);
      }
      // ->>

      // <<- '#popup--${id} .popup .groups' create groups popup
      // clear '.groups' popup content and create new
      $(`#popup--${id} .popup .groups`).remove();

      let html = `
        <div onclick="event.cancelBubble=true;" class="groups element">
          <div class="label">Groups</div>
          <div class="checklist">
      `;

      Array.prototype.forEach.call(data.groups, (name) => {
        // move to checklist items
        html += `
          <div onclick="postGroups('${id}', '${name}')" class="checked item">${name}</div>
        `;
      });

      // Add unchecked elements (groups not in use for this section)
      Array.prototype.forEach.call(data.allGroups, (group) => {
        if (data.groups.indexOf(group) == -1) {
          html += `
            <div onclick="postGroups('${id}', '${group}')" class="item">${group}</div>
          `;
        }
      });

      html += `
          </div>
          <input onchange="createGroup('${id}', this.value)" class="button" type="text" placeholder="Add Group">
        </div>
      `;

      $(`#popup--${id} .popup .${(data.rgbw.length > 0) ? 'cache' : 'main'}`).before(html);
    },
    // ->>

    // error callback
    function (err) {
      console.error(err.responseText);
      throw err;
    }
  );
  // ->>
};


SetupPopup.prototype.set = function (r, g, b) {
  // <<- set rgb to `#popup--${id} .popup .main .rgbw`
  const id = this.id;
  const rgb = [r, g, b];

  $(`#popup--${id} .popup .main .rgbw`).children().each(function (idx, child) {
    $(child).val(rgb[idx]);
  });
  // ->>
};


// <<- Helper Functions

function postGroups(id, group) {
  /**************************************************************
   * Iter children for `#popup--${id} .popup .groups .checklist`
   * and toggle group + post to cache
   **************************************************************/
  const list = $(`#popup--${id} .popup .groups .checklist`);
  let groups = [];

  list.children().each(function (idx, child) {
    child = $(child);

    if (child.hasClass('checked')) {
      if (child.text() == group) {
          child.removeClass('checked');
      }
      else {
        groups.push(child.text());
      }
    }
    else if (child.text() == group) {
      child.addClass('checked');
      groups.push(group);
    }
  });

  screen.route.cache.post(
    id,
    {'groups': groups, 'append': false},
    () => {
      screen.popup[id].load();
    }
  );
}


function createGroup(id, group) {
  if (group) {
    screen.route.cache.post(
      id,
      {'groups': [group], 'append': true},
      () => {
        // reload on success
        screen.popup[id].load();
      }
    );
  }
}

// ->>

