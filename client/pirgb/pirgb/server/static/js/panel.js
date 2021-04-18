/*jshint esversion: 6*/
/*global $, console, screen*/
'use strict';

const panel = {
  position: 'bottom',
  active: 'Sections',
  list: [
    'Sections',
    'Groups'
    //'Settings'
  ],
  html: {
    sections: function () {
      // <<- panel closed html code
      return `
        <div onclick="panel.open()" id="category">${panel.active}</div>
        <div onclick="screen.power.check()" class="panel-button">
          <img style="height:75%" class="panel-button-img" src="../static/icon/reload.png" alt="Reload">
        </div>
      `;
      // ->>
    },
    groups: function () {
      // <<- panel closed html code
      // TODO add onclick event to 'Add' Button
      return `
        <!-- NOTE: removed for now
        <div class="panel-button">
          <img style="height:75%" class="panel-button-img" src="../static/icon/add.png" alt="Add">
        </div>
        -->
        ${panel.html[panel.list[0].toLowerCase()]()}
      `;
      // ->>
    }
  },
  close: function () {
    // <<- generate html code for a closed panel for section ...
    const el = $(`.panel-${panel.position}`);

    el.css('height', `var(--panel-bottom-height)`);
    el.removeClass('open');
    el.html(panel.html[panel.active.toLowerCase()]);
    $('.screen .main').off('click');
    // ->>
  },
  open: function () {
    // <<- generate panel open html code for select a category from panel.list
    let html = ``;

    panel.list.forEach(function (category) {
      html += `
      <div onclick="panel.active='${category}';panel.close();requestCategory('${category}')" class="panel-item">
        ${category}
      </div>
      `;
    });

    const el = $(`.panel-${panel.position}`);

    el.css('height', `calc((var(--panel-bottom-height) * ${panel.list.length}) + (${panel.list.length} * 5px))`);
    el.addClass('open');
    el.html(html);

    $('.screen .main').on('click', function (event) {
      panel.close();
    });
    // ->>
  }
};
