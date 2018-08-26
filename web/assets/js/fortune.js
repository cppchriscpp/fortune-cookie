$(document).ready(function() {
    regularFortune();

    setInterval(function() {
        // Reload the cookie js file, so any new requests get new ones
        $.getScript('assets/data/cookie.js');
    }, 300000);

    $('.newFortune').click(regularFortune);
    $('.newConstitution').click(constLine);
    $('.newPolitic').click(constFortune);
    $('.bed').click(inBed);
});

function regularFortune() {
    $('.fortune').html(window.fortuneCookies[Math.floor(Math.random()*window.fortuneCookies.length)]);
}

function constFortune() {
    $('.fortune').html(window.constCookies[Math.floor(Math.random()*window.constCookies.length)]);
}

function constLine() {
    $('.fortune').html(window.constLines[Math.floor(Math.random()*window.constLines.length)]);
}

function inBed() {
    if (!$('.fortune').text().endsWith('In Bed.')) {
        $('.fortune').html($('.fortune').html() + ' In Bed.');
    }
}