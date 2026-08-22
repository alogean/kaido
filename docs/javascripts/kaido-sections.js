/* KaiDO , coloration et iconographie par section.
   Détecte la section courante (outils / psycho / methode) depuis l'URL,
   pose data-kaido-section sur <html>, et décore les onglets, la navigation
   latérale et le titre de page avec l'icône de la section.
   Icônes : Material Design Icons (Pictogrammers, Apache 2.0), les mêmes que
   celles embarquées dans MkDocs Material (console, brain, compass-outline). */
(function () {
  "use strict";

  var ICON_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="';
  var ICON_CLOSE = '"/></svg>';

  var SECTIONS = {
    outils: {
      label: "Installation et outils",
      path: "M20 19V7H4v12zm0-16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm-7 14v-2h5v2zm-3.42-4L5.57 9H8.4l3.3 3.3c.39.39.39 1.03 0 1.42L8.42 17H5.59z"
    },
    psycho: {
      label: "Bachelor en psychologie",
      path: "M21.33 12.91c.09 1.55-.62 3.04-1.89 3.95l.77 1.49c.23.45.26.98.06 1.45-.19.47-.58.84-1.06 1l-.79.25a1.687 1.687 0 0 1-1.86-.55L14.44 18c-.89-.15-1.73-.53-2.44-1.1-.5.15-1 .23-1.5.23-.88 0-1.76-.27-2.5-.79-.53.16-1.07.23-1.62.22-.79.01-1.57-.15-2.3-.45a4.1 4.1 0 0 1-2.43-3.61c-.08-.72.04-1.45.35-2.11-.29-.75-.32-1.57-.07-2.33C2.3 7.11 3 6.32 3.87 5.82c.58-1.69 2.21-2.82 4-2.7 1.6-1.5 4.05-1.66 5.83-.37.42-.11.86-.17 1.3-.17 1.36-.03 2.65.57 3.5 1.64 2.04.53 3.5 2.35 3.58 4.47.05 1.11-.25 2.2-.86 3.13.07.36.11.72.11 1.09m-5-1.41c.57.07 1.02.5 1.02 1.07a1 1 0 0 1-1 1h-.63c-.32.9-.88 1.69-1.62 2.29.25.09.51.14.77.21 5.13-.07 4.53-3.2 4.53-3.25a2.59 2.59 0 0 0-2.69-2.49 1 1 0 0 1-1-1 1 1 0 0 1 1-1c1.23.03 2.41.49 3.33 1.3.05-.29.08-.59.08-.89-.06-1.24-.62-2.32-2.87-2.53-1.25-2.96-4.4-1.32-4.4-.4-.03.23.21.72.25.75a1 1 0 0 1 1 1c0 .55-.45 1-1 1-.53-.02-1.03-.22-1.43-.56-.48.31-1.03.5-1.6.56-.57.05-1.04-.35-1.07-.9a.97.97 0 0 1 .88-1.1c.16-.02.94-.14.94-.77 0-.66.25-1.29.68-1.79-.92-.25-1.91.08-2.91 1.29C6.75 5 6 5.25 5.45 7.2 4.5 7.67 4 8 3.78 9c1.08-.22 2.19-.13 3.22.25.5.19.78.75.59 1.29-.19.52-.77.78-1.29.59-.73-.32-1.55-.34-2.3-.06-.32.27-.32.83-.32 1.27 0 .74.37 1.43 1 1.83.53.27 1.12.41 1.71.4q-.225-.39-.39-.81a1.038 1.038 0 0 1 1.96-.68c.4 1.14 1.42 1.92 2.62 2.05 1.37-.07 2.59-.88 3.19-2.13.23-1.38 1.34-1.5 2.56-1.5m2 7.47-.62-1.3-.71.16 1 1.25zm-4.65-8.61a1 1 0 0 0-.91-1.03c-.71-.04-1.4.2-1.93.67-.57.58-.87 1.38-.84 2.19a1 1 0 0 0 1 1c.57 0 1-.45 1-1 0-.27.07-.54.23-.76.12-.1.27-.15.43-.15.55.03 1.02-.38 1.02-.92"
    },
    methode: {
      label: "Méthodologie d'apprentissage",
      path: "m7 17 3.2-6.8L17 7l-3.2 6.8zm5-5.9a.9.9 0 0 0-.9.9.9.9 0 0 0 .9.9.9.9 0 0 0 .9-.9.9.9 0 0 0-.9-.9M12 2a10 10 0 0 1 10 10 10 10 0 0 1-10 10A10 10 0 0 1 2 12 10 10 0 0 1 12 2m0 2a8 8 0 0 0-8 8 8 8 0 0 0 8 8 8 8 0 0 0 8-8 8 8 0 0 0-8-8"
    }
  };

  function iconSvg(key) {
    return ICON_OPEN + SECTIONS[key].path + ICON_CLOSE;
  }

  function sectionOfPath(pathname) {
    var m = /\/(outils|psycho|methode)(\/|$)/.exec(pathname || "");
    return m ? m[1] : null;
  }

  function sectionOfLink(a) {
    try {
      return sectionOfPath(new URL(a.href, location.href).pathname);
    } catch (e) {
      return null;
    }
  }

  function addIcon(el, key, cls) {
    if (!el || el.querySelector(":scope > .kaido-icon")) return;
    var span = document.createElement("span");
    span.className = "kaido-icon " + (cls || "");
    span.innerHTML = iconSvg(key);
    el.insertBefore(span, el.firstChild);
  }

  function decorateTabs() {
    document.querySelectorAll(".md-tabs__item").forEach(function (li) {
      var a = li.querySelector(".md-tabs__link");
      if (!a) return;
      var key = sectionOfLink(a);
      if (!key) return;
      li.setAttribute("data-kaido-section", key);
      addIcon(a, key, "kaido-icon--tab");
    });
  }

  function decorateSidebar() {
    var nav = document.querySelector(".md-sidebar--primary .md-nav--primary");
    if (!nav) return;
    // Avec navigation.tabs + navigation.sections, la barre latérale ne montre
    // que la section courante ; on marque tout item dont le lien mène à une
    // section, ce qui couvre aussi le tiroir mobile où tout est listé.
    nav.querySelectorAll(".md-nav__item").forEach(function (li) {
      var a = li.querySelector(":scope > a.md-nav__link, :scope > label.md-nav__link a, :scope > .md-nav__container a, :scope > label.md-nav__link");
      if (!a) return;
      var key = a.tagName === "A" ? sectionOfLink(a) : null;
      if (!key && a.tagName === "LABEL") {
        var inner = a.querySelector("a");
        if (inner) key = sectionOfLink(inner);
      }
      if (!key) return;
      li.setAttribute("data-kaido-section", key);
      var isSectionHead = li.classList.contains("md-nav__item--section") || li.classList.contains("md-nav__item--nested");
      if (isSectionHead) {
        var label = li.querySelector(":scope > label.md-nav__link, :scope > .md-nav__container > label.md-nav__link, :scope > .md-nav__container > a.md-nav__link, :scope > a.md-nav__link");
        addIcon(label, key, "kaido-icon--nav");
      }
    });
  }

  function decorateContent(key) {
    var inner = document.querySelector(".md-content__inner");
    if (!inner || inner.querySelector(".kaido-chip")) return;
    var h1 = inner.querySelector("h1");
    if (!h1) return;
    if (!key) return;
    var chip = document.createElement("p");
    chip.className = "kaido-chip";
    chip.innerHTML = '<span class="kaido-icon">' + iconSvg(key) + "</span>" + SECTIONS[key].label;
    h1.parentNode.insertBefore(chip, h1);
  }

  function apply() {
    var key = sectionOfPath(location.pathname);
    document.documentElement.setAttribute("data-kaido-section", key || "accueil");
    decorateTabs();
    decorateSidebar();
    decorateContent(key);
  }

  if (typeof document$ !== "undefined" && document$ && typeof document$.subscribe === "function") {
    document$.subscribe(apply);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", apply);
  } else {
    apply();
  }
})();
