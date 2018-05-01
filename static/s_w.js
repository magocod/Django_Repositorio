importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.1.0/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}

workbox.precaching.precacheAndRoute([
  {
    url: '/static/icon/gif/unefalogo-min.gif',
    revision: 'abcde1'
  },
  {
    url: '/static/images/carousel/moodle-min.png',
    revision: 'abcde2'
  },
  {
    url: '/static/images/404-min.png',
    revision: 'abcde3'
  },
  {
    url: '/static/materialize/css/materialize.min.css',
    revision: 'abcde4'
  },
  {
    url: '/static/materialize/css/ghpages.min.css',
    revision: 'abcde5'
  },
  {
    url: '/static/plugin/datatables/datatables.min.css',
    revision: 'abcde6'
  },
  {
    url: '/static/materialize/icon/icon-googleapi.min.css',
    revision: 'abcde7'
  },
  {
    url: '/static/plugin/jquery/jquery-3.2.1.min.js',
    revision: 'abcde8'
  },
  {
    url: '/static/materialize/js/materialize.min.js',
    revision: 'abcde9'
  },
  {
    url: '/static/plugin/datatables/datatables.min.js',
    revision: 'abcde10'
  },
  {
    url: '/static/favicon.png',
    revision: 'abcde11'
  },
  {
    url: 'index.html',
    revision: 'abcde12'
  }

]);



