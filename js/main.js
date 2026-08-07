/* Dr. Adarsh Patil's Orthopaedic Clinic — site interactions */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Mobile nav ---- */
  var toggle = document.querySelector('.nav-toggle');
  var navLinks = document.getElementById('primary-nav');
  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      var open = navLinks.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    navLinks.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && window.innerWidth <= 820) {
        navLinks.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- Hero carousel ---- */
  var slides = Array.prototype.slice.call(document.querySelectorAll('.hero-slide'));
  var dots = Array.prototype.slice.call(document.querySelectorAll('.hero__dots button'));
  if (slides.length > 1) {
    var idx = 0;
    var timer = null;
    var show = function (n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('is-active', i === idx); });
      dots.forEach(function (d, i) { d.setAttribute('aria-selected', String(i === idx)); });
    };
    var start = function () {
      if (reduceMotion) return;
      stop();
      timer = setInterval(function () { show(idx + 1); }, 7000);
    };
    var stop = function () { if (timer) { clearInterval(timer); timer = null; } };
    dots.forEach(function (d, i) {
      d.addEventListener('click', function () { show(i); start(); });
    });
    var heroEl = document.querySelector('.hero');
    if (heroEl) {
      heroEl.addEventListener('mouseenter', stop);
      heroEl.addEventListener('mouseleave', start);
    }
    show(0);
    start();
  }

  /* ---- Count-up stats ---- */
  var nums = Array.prototype.slice.call(document.querySelectorAll('[data-count]'));
  if (nums.length) {
    var run = function (el) {
      if (el.dataset.done === '1') return;
      el.dataset.done = '1';
      var target = parseFloat(el.dataset.count);
      var suffix = el.dataset.suffix || '';
      if (reduceMotion) { el.textContent = target + suffix; return; }
      var dur = 1500;
      var t0 = null;
      var step = function (ts) {
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + (p === 1 ? suffix : '');
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      };
      requestAnimationFrame(step);
    };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { run(en.target); io.unobserve(en.target); } });
      }, { threshold: 0.35 });
      nums.forEach(function (n) { io.observe(n); });
    } else {
      nums.forEach(run);
    }
  }

  /* ---- Reveal on scroll ---- */
  var reveals = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  if (reveals.length) {
    if ('IntersectionObserver' in window && !reduceMotion) {
      var ro = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-visible'); ro.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px' });
      reveals.forEach(function (r) { ro.observe(r); });
    } else {
      reveals.forEach(function (r) { r.classList.add('is-visible'); });
    }
  }

  /* ---- FAQ accordion ---- */
  Array.prototype.forEach.call(document.querySelectorAll('.faq__q'), function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq__item');
      var open = item.getAttribute('data-open') === 'true';
      var group = item.parentElement;
      if (group && group.dataset.exclusive !== 'false') {
        Array.prototype.forEach.call(group.querySelectorAll('.faq__item'), function (i) {
          i.setAttribute('data-open', 'false');
          i.querySelector('.faq__q').setAttribute('aria-expanded', 'false');
        });
      }
      item.setAttribute('data-open', String(!open));
      btn.setAttribute('aria-expanded', String(!open));
    });
  });

  /* ---- Lightbox gallery ---- */
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery__item'));
  var box = document.getElementById('lightbox');
  if (items.length && box) {
    var boxImg = box.querySelector('img');
    var boxCap = box.querySelector('.lightbox__cap');
    var current = 0;
    var lastFocus = null;

    var render = function (n) {
      current = (n + items.length) % items.length;
      var src = items[current].dataset.full || items[current].querySelector('img').src;
      boxImg.src = src;
      boxImg.alt = items[current].querySelector('img').alt;
      boxCap.textContent = items[current].dataset.caption || '';
    };
    var open = function (n) {
      lastFocus = document.activeElement;
      render(n);
      box.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      box.querySelector('.lightbox__close').focus();
    };
    var close = function () {
      box.classList.remove('is-open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };
    items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
    box.querySelector('.lightbox__close').addEventListener('click', close);
    var prev = box.querySelector('.lightbox__nav--prev');
    var next = box.querySelector('.lightbox__nav--next');
    if (prev) prev.addEventListener('click', function () { render(current - 1); });
    if (next) next.addEventListener('click', function () { render(current + 1); });
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) {
      if (!box.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') render(current - 1);
      if (e.key === 'ArrowRight') render(current + 1);
    });
  }

  /* ---- Contact form: front-end only, opens the visitor's email client ---- */
  var form = document.getElementById('enquiry-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var body = [
        'Name: ' + (d.get('name') || ''),
        'Phone: ' + (d.get('phone') || ''),
        'Concern: ' + (d.get('concern') || ''),
        '',
        (d.get('message') || '')
      ].join('\n');
      window.location.href = 'mailto:adarshpatilortho@gmail.com'
        + '?subject=' + encodeURIComponent('Appointment enquiry — ' + (d.get('name') || 'Website visitor'))
        + '&body=' + encodeURIComponent(body);
      var status = document.getElementById('form-status');
      if (status) {
        status.textContent = 'Your email application should now open with the message pre-filled. If it does not, please call or WhatsApp +91 70205 25460.';
      }
    });
  }

  /* ---- Footer year ---- */
  Array.prototype.forEach.call(document.querySelectorAll('[data-year]'), function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
