window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]], 
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['upgreek']}
  },
  loader: {
    load: ['[tex]/upgreek']
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};