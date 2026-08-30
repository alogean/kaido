/* Capture le contenu textuel principal de la page Moodle actuellement chargée dans un onglet.
   Utilisé pour les ressources de type mod/page, mod/book, et pour la page de cours elle-même.
   À exécuter via moodle.py page sur l’URL cible (l'onglet doit déjà être sur cette page).
   Retourne le texte visible du bloc de contenu principal. */
(function () {
  var main = document.querySelector('[role="main"], #region-main, .course-content, #page-content') || document.body;
  var title = document.title;
  var text = (main.innerText || main.textContent || '').replace(/\n{3,}/g, '\n\n').trim();
  return JSON.stringify({ title: title, url: location.href, text: text });
})();
