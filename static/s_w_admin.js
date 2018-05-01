importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.1.0/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}

workbox.precaching.precacheAndRoute([
  {
    url: '/static/bootstrap4/css/bootstrap.min.css',
    revision: 'abcde11'
  },
  {
    url: '/static/sbadmin/font-awesome/css/font-awesome.min.css',
    revision: 'abcde22'
  },
  {
    url: '/static/sbadmin/css/sb-admin.min.css',
    revision: 'abcde33'
  },
  {
    url: '/static/plugin/chosen/chosen.min.css',
    revision: 'abcde44'
  },
  {
    url: '/static/plugin/chosen/chosen-bootstrap.css',
    revision: 'abcde55'
  },
  {
    url: '/static/plugin/datatables/datatables.bootstrap4.min.css',
    revision: 'abcde66'
  },
  {
    url: '/static/icon/jpg/py-m3-min.jpg',
    revision: 'abcde77'
  },
  {
    url: '/static/plugin/jquery/jquery-3.2.1.min.js',
    revision: 'abcde88'
  },
  {
    url: '/static/plugin/popper/popper.min.js',
    revision: 'abcde99'
  },
  {
    url: '/static/bootstrap4/js/bootstrap.min.js',
    revision: 'abcde100'
  },
  {
    url: '/static/bootstrap4/js/bootstrap.bundle.min.js',
    revision: 'abcde111'
  },
  {
    url: '/static/plugin/jquery-easing/jquery.easing.min.js',
    revision: 'abcde122'
  },
  {
    url: '/static/sbadmin/js/sb-admin.min.js',
    revision: 'abcde133'
  },
  {
    url: '/static/plugin/chosen/chosen.jquery.min.js',
    revision: 'abcde100'
  },
  {
    url: '/static/plugin/datatables/datatables.min.js',
    revision: 'abcde111'
  },
  {
    url: '/static/plugin/functions/f-bootstrap.js',
    revision: 'abcde122'
  },
  {
    url: '/static/favicon.png',
    revision: 'abcde123'
  }
  
]);



