#!/usr/bin/node
const $ = window.$;
$(document).ready(() => {
  $('#update_header').on('click', () => {
    $('header').html('New Header!!!');
  });
});
