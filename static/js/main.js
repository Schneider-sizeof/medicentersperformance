'use strict';

document.addEventListener('DOMContentLoaded', function () {

  // Signal that JS is active — CSS scroll animations only engage when this class is present
  document.body.classList.add('js-ready');

  /* ============================================================
     1. PRELOADER — fade out on window load with 3s failsafe
     ============================================================ */
  (function initPreloader() {
    var preloader = document.getElementById('preloader');
    if (!preloader) return;

    function hidePreloader() {
      preloader.classList.add('loaded');
      setTimeout(function () {
        preloader.style.display = 'none';
      }, 600);
    }

    window.addEventListener('load', hidePreloader);

    // 3-second failsafe
    setTimeout(function () {
      if (preloader.style.display !== 'none') {
        hidePreloader();
      }
    }, 3000);
  })();

  /* ============================================================
     2. NAVBAR — scroll-based 'scrolled' class & logo shrink
     ============================================================ */
  (function initNavbar() {
    var navbar = document.querySelector('.navbar');
    var logo = document.querySelector('.navbar-brand img');
    if (!navbar) return;

    function onScroll() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;

      if (scrollY > 50) {
        navbar.classList.add('scrolled');
        if (logo) logo.classList.add('logo-shrink');
      } else {
        navbar.classList.remove('scrolled');
        if (logo) logo.classList.remove('logo-shrink');
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on init
  })();

  /* ============================================================
     3. SCROLL ANIMATIONS — IntersectionObserver with stagger
     ============================================================ */
  (function initScrollAnimations() {
    if (!('IntersectionObserver' in window)) return;

    var animClasses = ['.fade-in-up', '.fade-in-left', '.fade-in-right'];
    var elements = document.querySelectorAll(animClasses.join(','));
    if (!elements.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;

          // Stagger children inside the element
          var children = el.querySelectorAll('.stagger-child');
          if (children.length) {
            children.forEach(function (child, i) {
              child.style.transitionDelay = (i * 100) + 'ms';
              child.classList.add('visible');
            });
          }

          el.classList.add('visible');
          observer.unobserve(el);
        }
      });
    }, {
      threshold: 0.05,
      rootMargin: '50px 0px 0px 0px'
    });

    elements.forEach(function (el) { observer.observe(el); });
  })();

  /* ============================================================
     4. COUNTER ANIMATION — animate 0 → data-target over 2s
     ============================================================ */
  (function initCounters() {
    if (!('IntersectionObserver' in window) || !('requestAnimationFrame' in window)) return;

    var counters = document.querySelectorAll('.counter-number');
    if (!counters.length) return;

    var DURATION = 2000; // ms

    function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }

    function animateCounter(el) {
      var target = parseInt(el.getAttribute('data-target'), 10);
      if (isNaN(target)) return;

      var suffix = el.getAttribute('data-suffix') || '';
      var start = 0;
      var startTime = null;

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var elapsed = timestamp - startTime;
        var progress = Math.min(elapsed / DURATION, 1);
        var value = Math.floor(easeOutQuart(progress) * (target - start) + start);

        el.textContent = value.toLocaleString() + suffix;

        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target.toLocaleString() + suffix;
        }
      }

      requestAnimationFrame(step);
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function (c) { observer.observe(c); });
  })();

  /* ============================================================
     5. SMOOTH SCROLL — anchor links offset by navbar height
     ============================================================ */
  (function initSmoothScroll() {
    var navbar = document.querySelector('.navbar');

    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;

      var id = link.getAttribute('href');
      if (id === '#' || id === '#!') return;

      var targetEl = document.querySelector(id);
      if (!targetEl) return;

      e.preventDefault();

      var navHeight = navbar ? navbar.offsetHeight : 0;
      var targetPos = targetEl.getBoundingClientRect().top + window.pageYOffset - navHeight - 16;

      if ('scrollBehavior' in document.documentElement.style) {
        window.scrollTo({ top: targetPos, behavior: 'smooth' });
      } else {
        window.scrollTo(0, targetPos);
      }
    });
  })();

  /* ============================================================
     6. LAZY LOADING — Matterport iframes with data-src
     ============================================================ */
  (function initLazyIframes() {
    if (!('IntersectionObserver' in window)) {
      // Fallback: load all immediately
      var iframes = document.querySelectorAll('iframe[data-src]');
      iframes.forEach(function (iframe) {
        iframe.src = iframe.getAttribute('data-src');
        iframe.removeAttribute('data-src');
      });
      return;
    }

    var lazyIframes = document.querySelectorAll('iframe[data-src]');
    if (!lazyIframes.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var iframe = entry.target;
          iframe.src = iframe.getAttribute('data-src');
          iframe.removeAttribute('data-src');
          iframe.classList.add('loaded');
          observer.unobserve(iframe);
        }
      });
    }, {
      rootMargin: '200px 0px'
    });

    lazyIframes.forEach(function (iframe) { observer.observe(iframe); });
  })();

  /* ============================================================
     7. BACK TO TOP — show at 300px, smooth scroll to top
     ============================================================ */
  (function initBackToTop() {
    var btn = document.getElementById('backToTop') || document.querySelector('.back-to-top');
    if (!btn) return;

    function toggleVisibility() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollY > 300) {
        btn.classList.add('visible');
      } else {
        btn.classList.remove('visible');
      }
    }

    window.addEventListener('scroll', toggleVisibility, { passive: true });
    toggleVisibility();

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      if ('scrollBehavior' in document.documentElement.style) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        window.scrollTo(0, 0);
      }
    });
  })();

  /* ============================================================
     8. MOBILE NAVBAR — auto-close collapse on link click (<992px)
     ============================================================ */
  (function initMobileNavClose() {
    var navCollapse = document.querySelector('.navbar-collapse');
    if (!navCollapse) return;

    var navLinks = navCollapse.querySelectorAll('.nav-link');

    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth < 992 && navCollapse.classList.contains('show')) {
          // Bootstrap 5
          var bsCollapse = typeof bootstrap !== 'undefined' && bootstrap.Collapse
            ? bootstrap.Collapse.getInstance(navCollapse)
            : null;

          if (bsCollapse) {
            bsCollapse.hide();
          } else {
            // Fallback: manually toggle classes
            navCollapse.classList.remove('show');
            var toggler = document.querySelector('.navbar-toggler');
            if (toggler) toggler.classList.add('collapsed');
          }
        }
      });
    });
  })();

  /* ============================================================
     9. PARALLAX EFFECT — hero translateY at 0.3× scroll speed
     ============================================================ */
  (function initParallax() {
    var hero = document.querySelector('.hero-section, .hero, [data-parallax]');
    if (!hero) return;

    // Skip on touch devices for performance
    var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;

    var ticking = false;

    function updateParallax() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      var heroBottom = hero.offsetTop + hero.offsetHeight;

      // Only apply when hero is in viewport
      if (scrollY <= heroBottom) {
        hero.style.backgroundPositionY = (scrollY * 0.3) + 'px';
      }

      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(updateParallax);
        ticking = true;
      }
    }, { passive: true });
  })();

  /* ============================================================
     10. TYPEWRITER EFFECT — cycle through data-words array
     ============================================================ */
  (function initTypewriter() {
    var el = document.querySelector('.typewriter');
    if (!el) return;

    var wordsAttr = el.getAttribute('data-words');
    if (!wordsAttr) return;

    var words;
    try {
      words = JSON.parse(wordsAttr);
    } catch (e) {
      words = wordsAttr.split(',').map(function (w) { return w.trim(); });
    }

    if (!words.length) return;

    var wordIndex = 0;
    var charIndex = 0;
    var isDeleting = false;
    var TYPING_SPEED = 80;
    var DELETING_SPEED = 50;
    var PAUSE_AFTER_WORD = 1800;
    var PAUSE_BEFORE_TYPE = 400;

    function tick() {
      var currentWord = words[wordIndex];
      var displayText;

      if (isDeleting) {
        charIndex--;
        displayText = currentWord.substring(0, charIndex);
      } else {
        charIndex++;
        displayText = currentWord.substring(0, charIndex);
      }

      el.textContent = displayText;

      var delay = isDeleting ? DELETING_SPEED : TYPING_SPEED;

      if (!isDeleting && charIndex === currentWord.length) {
        delay = PAUSE_AFTER_WORD;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        delay = PAUSE_BEFORE_TYPE;
      }

      setTimeout(tick, delay);
    }

    tick();
  })();

  /* ============================================================
     11. NAVBAR ACTIVE LINK — highlight based on URL path
     ============================================================ */
  (function initActiveLink() {
    var currentPath = window.location.pathname.replace(/\/+$/, '') || '/';
    var navLinks = document.querySelectorAll('.navbar .nav-link');

    navLinks.forEach(function (link) {
      var linkPath = (link.getAttribute('href') || '').replace(/\/+$/, '') || '/';

      // Normalize relative paths
      try {
        var a = document.createElement('a');
        a.href = link.getAttribute('href') || '';
        linkPath = a.pathname.replace(/\/+$/, '') || '/';
      } catch (e) { /* keep parsed path */ }

      link.classList.remove('active');

      if (linkPath === currentPath) {
        link.classList.add('active');

        // Also mark parent dropdown if applicable
        var dropdown = link.closest('.dropdown');
        if (dropdown) {
          var toggle = dropdown.querySelector('.dropdown-toggle');
          if (toggle) toggle.classList.add('active');
        }
      }
    });
  })();

});
