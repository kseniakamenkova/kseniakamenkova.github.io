// Open every page at the top, except when returning with the browser's Back/Forward buttons.
(() => {
  const nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
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
