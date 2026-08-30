/* Énumère toutes les ressources téléchargeables et pages d'une page de cours Moodle FernUni.
   À exécuter dans l’onglet du cours via moodle.py.
   Retourne une chaîne JSON: { title, files:[...], pages:[...], links:[...], subcourses:[...] }.
   - files : liens vers des fichiers (mod/resource, pluginfile, mod/folder, extensions directes)
   - pages : mod/page, mod/book, mod/lesson (contenu HTML à capturer séparément)
   - links : mod/url et liens vidéo directs. C'est là que vivent les vidéos SWITCHtube.
             Un cours peut n'avoir aucun `pages` et quarante vidéos, toutes derrière des
             mod/url : les résoudre avec moodle.py resolve, les aspirer avec
             moodle.py video. `kind` vaut "video" si la cible est manifestement une
             vidéo, "lien" sinon (un lien Zoom de regroupement n'est pas téléchargeable).
*/
(function () {
  var out = { title: document.title, files: [], pages: [], links: [], subcourses: [] };
  var seen = {};
  var videoHost = /tube\.switch\.ch|switchtube|vimeo\.com|youtube\.com|youtu\.be|kaltura/i;
  var videoName = /vid[ée]o|video|enregistrement|regroupement|recording/i;
  var fileExt = /\.(pdf|docx?|pptx?|xlsx?|odt|ods|odp|zip|rtf|csv|txt|mp3|mp4|m4a|jpg|jpeg|png)(\?|$)/i;
  var anchors = Array.prototype.slice.call(document.querySelectorAll('a[href]'));
  anchors.forEach(function (a) {
    var href = a.href;
    if (!href || seen[href]) return;
    var txt = (a.innerText || a.textContent || '').replace(/\s+/g, ' ').trim();
    // nom depuis l'attribut ou le texte de l'activité
    var inst = a.closest('.activityinstance, .activity-item, li.activity');
    var name = txt;
    if (inst) {
      var n = inst.querySelector('.instancename, .activityname, .activitytitle');
      if (n) name = (n.innerText || n.textContent).replace(/\s+/g, ' ').trim();
    }
    name = name.replace(/\s*(Fichier|File|Dossier|Folder|Page|URL|Lien)\s*$/i, '').trim();

    if (/\/mod\/resource\/view\.php/.test(href) || /\/pluginfile\.php/.test(href) ||
        /\/mod\/folder\/view\.php/.test(href) || fileExt.test(href)) {
      seen[href] = 1;
      out.files.push({ url: href, name: name || 'ressource', type: 'file' });
    } else if (/\/mod\/(page|book|lesson)\/view\.php/.test(href)) {
      seen[href] = 1;
      out.pages.push({ url: href, name: name || 'page' });
    } else if (/\/mod\/url\/view\.php/.test(href)) {
      // Cible externe inconnue à ce stade : moodle.py resolve la résoudra.
      seen[href] = 1;
      out.links.push({ url: href, name: name || 'lien',
                       kind: videoName.test(name) ? 'video' : 'lien', resolved: null });
    } else if (videoHost.test(href)) {
      // Lien vidéo posé directement dans le cours, sans passer par un mod/url.
      seen[href] = 1;
      out.links.push({ url: href, name: name || 'video', kind: 'video', resolved: href });
    } else if (/\/course\/view\.php/.test(href) && href.indexOf(location.href) !== 0) {
      // sous-cours / catégories liés (rare) , informatif
      seen[href] = 1;
      out.subcourses.push({ url: href, name: name });
    }
  });
  return JSON.stringify(out);
})();
