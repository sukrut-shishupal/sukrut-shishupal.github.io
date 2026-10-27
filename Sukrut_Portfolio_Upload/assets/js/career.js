// The site remains fully usable without JavaScript.
const normalizedPath = value => value.replace(/index\.html$/, '').replace(/\/$/, '') || '/';
document.querySelectorAll('nav a').forEach(link => {
  const url = new URL(link.href, location.href);
  if (!url.hash && normalizedPath(url.pathname) === normalizedPath(location.pathname)) {
    link.setAttribute('aria-current', 'page');
  }
});
