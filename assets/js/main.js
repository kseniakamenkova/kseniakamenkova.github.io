// Blocks that exist in the same order on the English and Russian page. Switching language remembers
// which of them was at the top of the screen (and how far into it), so the other language opens there.
const LANG_ANCHORS = '.hello, .projects__title, .project, .contact, .back, .case-head, .case-intro > *, .case-flow > *';
const LANG_KEY = 'lang-switch-place';

function anchors() {
  return [...document.querySelectorAll(LANG_ANCHORS)].filter((el) => el.offsetHeight > 0);
}

function readPlace() {
  try {
    const raw = sessionStorage.getItem(LANG_KEY);
    if (!raw) return null;
    sessionStorage.removeItem(LANG_KEY);
    const place = JSON.parse(raw);
    // only for the page the switcher pointed to, and only right after the click
    return place.to === location.pathname && Date.now() - place.at < 15000 ? place : null;
  } catch (_) { return null; }
}

// Open every page at the top, except when returning with Back/Forward or right after switching language.
(() => {
  const nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  const place = readPlace();
  if (place) {
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    const restore = () => {
      const list = anchors();
      const el = list[Math.min(place.i, list.length - 1)];
      if (!el) return;
      const top = el.getBoundingClientRect().top + window.scrollY;
      window.scrollTo(0, Math.max(0, top + place.f * el.offsetHeight - place.v));
    };
    restore();
    // text and fonts can still shift the layout a little while the page loads
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(restore);
    window.addEventListener('load', restore);
    return;
  }
  if (!location.hash && (!nav || nav.type !== 'back_forward')) {
    window.scrollTo(0, 0);
    window.addEventListener('load', () => window.scrollTo(0, 0));
  }
})();

// Image rails: drag with the mouse, scroll with the arrow keys. Touch and trackpads scroll natively.
document.querySelectorAll('.rail--scroll .rail__track').forEach((track) => {
  let startX = 0;
  let startLeft = 0;
  let dragging = false;

  track.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    dragging = true;
    startX = e.clientX;
    startLeft = track.scrollLeft;
    track.setPointerCapture(e.pointerId);
    track.classList.add('is-dragging');
  });
  track.addEventListener('pointermove', (e) => {
    if (dragging) track.scrollLeft = startLeft - (e.clientX - startX);
  });
  const stop = () => {
    dragging = false;
    track.classList.remove('is-dragging');
  };
  track.addEventListener('pointerup', stop);
  track.addEventListener('pointercancel', stop);

  track.addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    e.preventDefault();
    const step = track.clientWidth * 0.6 * (e.key === 'ArrowRight' ? 1 : -1);
    const smooth = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    track.scrollBy({ left: step, behavior: smooth ? 'smooth' : 'auto' });
  });
});

// Sticky header: a hairline appears once the page is scrolled.
(() => {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const update = () => header.classList.toggle('is-scrolled', window.scrollY > 4);
  update();
  window.addEventListener('scroll', update, { passive: true });
})();

// The dog in the contact block wags its tail when it scrolls into view, and again on hover or tap.
(() => {
  const dog = document.querySelector('.contact__dog');
  if (!dog) return;
  const wag = () => {
    dog.classList.remove('is-wagging');
    void dog.offsetWidth; // restart the animation
    dog.classList.add('is-wagging');
  };
  dog.addEventListener('animationend', () => dog.classList.remove('is-wagging'));
  dog.addEventListener('pointerenter', wag);
  dog.addEventListener('click', wag);
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) { wag(); io.disconnect(); }
    }, { threshold: 0.6 });
    io.observe(dog);
  }
})();

// Language switcher: the button opens a small menu with both languages; Escape or a click outside closes it.
(() => {
  const root = document.querySelector('.lang');
  if (!root) return;
  const btn = root.querySelector('.lang__btn');
  const menu = root.querySelector('.lang__menu');
  const opts = [...menu.querySelectorAll('.lang__opt')];
  const open = (focusFirst) => {
    menu.hidden = false;
    btn.setAttribute('aria-expanded', 'true');
    if (focusFirst) (menu.querySelector('[aria-current]') || opts[0]).focus();
  };
  const close = (focusBtn) => {
    menu.hidden = true;
    btn.setAttribute('aria-expanded', 'false');
    if (focusBtn) btn.focus();
  };
  btn.addEventListener('click', () => (menu.hidden ? open(false) : close(false)));
  btn.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); open(true); }
  });
  menu.addEventListener('keydown', (e) => {
    const i = opts.indexOf(document.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); opts[(i + 1) % opts.length].focus(); }
    if (e.key === 'ArrowUp') { e.preventDefault(); opts[(i - 1 + opts.length) % opts.length].focus(); }
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) close(true); });
  document.addEventListener('click', (e) => { if (!menu.hidden && !root.contains(e.target)) close(false); });
  // Remember the place on the page so the other language opens at the same block, not at the top.
  opts.forEach((a) => a.addEventListener('click', () => {
    if (a.hasAttribute('aria-current')) return;
    const list = anchors();
    const line = 96; // just under the sticky header
    let i = list.findIndex((el) => el.getBoundingClientRect().bottom > line);
    if (i < 0) i = list.length - 1;
    const r = list[i].getBoundingClientRect();
    const f = Math.min(1, Math.max(0, (line - r.top) / Math.max(1, r.height)));
    try {
      sessionStorage.setItem(LANG_KEY, JSON.stringify({ to: new URL(a.href, location.href).pathname, i, f, v: line, at: Date.now() }));
    } catch (_) {}
  }));
})();
