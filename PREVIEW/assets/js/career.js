// Progressive enhancement: navigation and content also work without JavaScript.
document.querySelectorAll('nav a').forEach(link => {
  const url = new URL(link.href, location.href);
  if (url.pathname === location.pathname && !url.hash) link.setAttribute('aria-current', 'page');
});
