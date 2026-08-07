/* Google reviews marquee — renders from data/reviews.json.
   The JSON is refreshed by .github/workflows/update-reviews.yml so the
   section stays current without anyone editing markup. */
(function () {
  'use strict';

  var track = document.querySelector('[data-reviews-track]');
  if (!track) return;

  var STAR = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.5 2.9 5.9 6.6.9-4.8 4.6 1.2 6.5-5.9-3.1-5.9 3.1 1.2-6.5L2.5 9.3l6.6-.9z"/></svg>';
  var GOOGLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.4a5.5 5.5 0 0 1-2.4 3.6v3h3.9c2.3-2.1 3.6-5.2 3.6-8.8z"/><path fill="#34A853" d="M12 24c3.2 0 6-1.1 8-2.9l-3.9-3a7.2 7.2 0 0 1-10.7-3.8h-4v3.1A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.3 14.3a7.1 7.1 0 0 1 0-4.6v-3.1h-4a12 12 0 0 0 0 10.8l4-3.1z"/><path fill="#EA4335" d="M12 4.8c1.8 0 3.4.6 4.6 1.8l3.5-3.5A12 12 0 0 0 1.3 6.6l4 3.1A7.2 7.2 0 0 1 12 4.8z"/></svg>';
  var QUOTE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.5 5C6.5 6.6 4.8 9.3 4.8 12.6V19h6.4v-6.4H8.1c0-2.2.9-3.8 2.8-4.9L9.5 5zm9.4 0c-3 1.6-4.7 4.3-4.7 7.6V19h6.4v-6.4h-3.1c0-2.2.9-3.8 2.8-4.9L18.9 5z"/></svg>';

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function stars(n) {
    var out = '';
    for (var i = 0; i < Math.max(0, Math.min(5, Math.round(n || 0))); i++) out += STAR;
    return out;
  }

  function initials(name) {
    var parts = String(name || '').trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return '?';
    var a = parts[0].charAt(0);
    var b = parts.length > 1 ? parts[parts.length - 1].charAt(0) : '';
    return (a + b).toUpperCase();
  }

  function card(r) {
    return '<figure class="review-card">' +
        '<div class="review-card__top">' +
          '<span class="review-card__g">' + GOOGLE + '</span>' +
          '<span class="review-card__stars" role="img" aria-label="' + esc(r.rating) + ' out of 5">' + stars(r.rating) + '</span>' +
          '<span class="review-card__when">' + esc(r.when || '') + '</span>' +
        '</div>' +
        '<blockquote class="review-card__text">' + esc(r.text) + '</blockquote>' +
        '<figcaption class="review-card__foot">' +
          '<span class="review-card__avatar" aria-hidden="true">' + esc(initials(r.author)) + '</span>' +
          '<span><span class="review-card__name">' + esc(r.author) + '</span>' +
            (r.local_guide ? '<span class="review-card__guide">Local Guide</span>' : '') +
          '</span>' +
          '<span class="review-card__quote">' + QUOTE + '</span>' +
        '</figcaption>' +
      '</figure>';
  }

  function fmtDate(iso) {
    if (!iso) return '\u2014';
    var d = new Date(iso);
    if (isNaN(d.getTime())) return esc(iso);
    return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function render(data) {
    var list = (data.reviews || []).filter(function (r) { return r && r.text; });
    if (!list.length) {
      var section = document.getElementById('reviews');
      if (section) section.hidden = true;
      return;
    }

    // Duplicate the set so the -50% keyframe loops seamlessly.
    var html = list.map(card).join('');
    track.innerHTML = html + html;
    track.setAttribute('aria-label', list.length + ' patient reviews from Google');

    // Slow the scroll proportionally to how much content there is.
    track.style.animationDuration = Math.max(40, list.length * 7) + 's';

    var summary = document.querySelector('[data-reviews-summary]');
    if (summary && data.rating) {
      summary.hidden = false;
      var rating = summary.querySelector('[data-reviews-rating]');
      var st = summary.querySelector('[data-reviews-stars]');
      var ct = summary.querySelector('[data-reviews-count]');
      if (rating) rating.textContent = Number(data.rating).toFixed(1);
      if (st) st.innerHTML = stars(data.rating);
      if (ct) ct.textContent = data.total ? data.total + ' Google reviews' : '';
    }

    var upd = document.querySelector('[data-reviews-updated]');
    if (upd) upd.textContent = fmtDate(data.updated);
  }

  fetch('data/reviews.json', { cache: 'no-cache' })
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(render)
    .catch(function () {
      var section = document.getElementById('reviews');
      if (section) section.hidden = true;
    });
})();
