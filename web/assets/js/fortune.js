$(document).ready(function() {
    $('.fortune').text(window.fortuneCookies[Math.floor(Math.random()*window.fortuneCookies.length)]);
});