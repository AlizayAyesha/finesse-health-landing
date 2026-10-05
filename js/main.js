// Mobile nav toggle, footer year, and front-end enquiry form (demo only).
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var close = function () {
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-open');
    };
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      document.body.classList.toggle('nav-open', !open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        close();
        toggle.focus();
      }
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());

  var form = document.getElementById('enquiry-form');
  if (!form) return;

  var success = document.getElementById('form-success');

  function clearInvalid() {
    form.querySelectorAll('.is-invalid').forEach(function (el) {
      el.classList.remove('is-invalid');
    });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    clearInvalid();

    var fullName = form.querySelector('#full-name');
    var phone = form.querySelector('#phone');
    var email = form.querySelector('#email');
    var treatment = form.querySelector('#treatment');
    var terms = form.querySelector('#terms-agree');
    var invalid = false;

    function requireField(el) {
      if (!el) return;
      var ok = el.type === 'checkbox' ? el.checked : Boolean(String(el.value || '').trim());
      if (!ok) {
        el.classList.add('is-invalid');
        invalid = true;
      }
    }

    requireField(fullName);
    requireField(phone);
    requireField(email);
    requireField(treatment);
    requireField(terms);

    if (email && email.value && !email.checkValidity()) {
      email.classList.add('is-invalid');
      invalid = true;
    }

    if (invalid) {
      var first = form.querySelector('.is-invalid');
      if (first) first.focus();
      return;
    }

    // Front-end only: no network request. Backend wiring required (see README).
    form.classList.add('is-submitted');
    if (success) {
      success.hidden = false;
      success.focus && success.setAttribute('tabindex', '-1');
      success.focus();
    }
  });
})();
