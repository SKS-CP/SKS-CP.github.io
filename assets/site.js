/* Swap in a placeholder if a figure image hasn't been added yet. */
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
