// Mobile nav toggle + footer year. Kept intentionally minimal.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var close = function () { toggle.setAttribute('aria-expanded', 'false'); document.body.classList.remove('nav-open'); };
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      document.body.classList.toggle('nav-open', !open);
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { close(); toggle.focus(); } });
  }
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
