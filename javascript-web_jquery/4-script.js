#!/usr/bin/node
const $ = window.$;
$('div#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
