/* Ouvre toutes les sections repliées d'une page de cours Moodle FernUni pour que
   tous les liens d'activités soient présents dans le DOM avant l'énumération.
   À exécuter dans l’onglet du cours via moodle.py. Retourne un petit rapport.
   NB FernUni : les déclencheurs sont souvent de simples liens/spans dont le TEXTE est
   « Déplier » / « Tout ouvrir » / « Tout déplier » , d'où le clic par libellé ci-dessous. */
(function () {
  var clicked = 0;
  var labels = ['déplier', 'tout ouvrir', 'tout déplier', 'expand all', 'open all'];
  document.querySelectorAll('a, button, span').forEach(function (e) {
    var t = (e.innerText || e.textContent || '').trim().toLowerCase();
    if (labels.indexOf(t) !== -1) { try { e.click(); clicked++; } catch (x) {} }
  });
  // éléments encore marqués repliés (attributs ARIA / classes Boost)
  document.querySelectorAll('[aria-expanded="false"], a.collapsed, [data-toggle="collapse"][aria-expanded="false"]')
    .forEach(function (e) { try { e.click(); clicked++; } catch (x) {} });
  return JSON.stringify({ clicked: clicked });
})();
