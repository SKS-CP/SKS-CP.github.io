/* ------------------------------------------------------------------
   1. Swap in a placeholder for any figure image not yet added.
   ------------------------------------------------------------------ */
document.addEventListener(
  'error',
  function (e) {
    var el = e.target;
    if (el.tagName === 'IMG' && el.dataset.fallback !== 'done') {
      el.dataset.fallback = 'done';
      el.classList.add('is-missing');
      el.src = 'assets/placeholder.svg';
    }
  },
  true
);

/* ------------------------------------------------------------------
   2. Site search. Reads window.SEARCH_INDEX from assets/search-index.js,
      which the build script regenerates from the page text.
   ------------------------------------------------------------------ */
(function () {
  var toggle = document.querySelector('.search-toggle');
  var panel = document.querySelector('.search-panel');
  if (!toggle || !panel) return;

  var input = panel.querySelector('input');
  var list = panel.querySelector('.search-results');

  function open() {
    panel.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    input.focus();
  }

  function close() {
    panel.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    panel.classList.contains('is-open') ? close() : open();
  });

  document.addEventListener('click', function (e) {
    if (!panel.contains(e.target) && e.target !== toggle) close();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  function snippet(text, term) {
    var i = text.toLowerCase().indexOf(term);
    if (i < 0) return text.slice(0, 110) + '…';
    var start = Math.max(0, i - 40);
    return (start > 0 ? '…' : '') + text.slice(start, start + 130).trim() + '…';
  }

  input.addEventListener('input', function () {
    var term = input.value.trim().toLowerCase();
    list.innerHTML = '';

    if (term.length < 2) return;

    var index = window.SEARCH_INDEX || [];
    var hits = index.filter(function (p) {
      return (p.title + ' ' + p.text).toLowerCase().indexOf(term) > -1;
    });

    if (!hits.length) {
      list.innerHTML = '<li class="search-empty">No pages match that.</li>';
      return;
    }

    hits.slice(0, 8).forEach(function (p) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = p.url;
      a.innerHTML =
        '<span class="r-title"></span><span class="r-snip"></span>';
      a.querySelector('.r-title').textContent = p.title;
      a.querySelector('.r-snip').textContent = snippet(p.text, term);
      li.appendChild(a);
      list.appendChild(li);
    });
  });
})();
