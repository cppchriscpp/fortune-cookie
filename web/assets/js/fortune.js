$(document).ready(function() {
    var uselessNumber = (new Date()).getTime();
    $.getScript('assets/data/cookie.js?junk='+uselessNumber, function() {
        regularFortune();
    });

    setInterval(function() {
        // Reload the cookie js file, so any new requests get new ones
        // The ? thing is to make sure it actually loads a new copy to replace the old one. (Caching, etc)
        $.getScript('assets/data/cookie.js?junk='+uselessNumber);
    }, 300000);

    $('.newFortune').click(regularFortune);
    $('.newConstitution').click(constLine);
    $('.newPolitic').click(constFortune);
    $('.tweet').click(tweetLine);
    $('.tweetCookie').click(tweetCookieLine)
    $('.everythingCookie').click(everythingLine);
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

function tweetLine() {
    $('.fortune').html(window.tweetLines[Math.floor(Math.random()*window.tweetLines.length)]);
}

function tweetCookieLine() {
    $('.fortune').html(window.tweetCookie[Math.floor(Math.random()*window.tweetCookie.length)]);
}

function everythingLine() {
    $('.fortune').html(window.everythingCookie[Math.floor(Math.random()*window.everythingCookie.length)]);
}

function inBed() {
    if (!$('.fortune').text().endsWith('In Bed.')) {
        $('.fortune').html($('.fortune').html() + ' In Bed.');
    }
}