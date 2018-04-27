importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.1.0/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}

workbox.precaching.precache([
  {
    url: '/static/icon/gif/unefalogo-min.gif',
    revision: 'abcde',
  },
  {
    url: '/static/images/carousel/moodle-min.png',
    revision: 'abcde',
  },
  {
    url: '/static/images/404-min.png',
    revision: 'abcde',
  },
  {
    url: '/static/materialize/css/materialize.min.css',
    revision: 'abcde',
  },
  {
    url: '/static/materialize/css/ghpages.min.css',
    revision: 'abcde',
  },
  {
    url: '/static/plugin/datatables/datatables.min.css',
    revision: 'abcde',
  },
  {
    url: '/static/materialize/icon/icon-googleapi.min.css',
    revision: 'abcde',
  },
  {
    url: '/static/plugin/jquery/jquery-3.2.1.min.js',
    revision: 'abcde',
  },
  {
    url: '/static/materialize/js/materialize.min.js',
    revision: 'abcde',
  },
  {
    url: '/static/plugin/datatables/datatables.min.js',
    revision: 'abcde',
  },
]);