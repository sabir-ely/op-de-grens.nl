import * as SimpleMDE from "simplemde";
import "simplemde/dist/simplemde.min.css";

const markdownEditor : Element = document.getElementById("markdown_editor");

new SimpleMDE({
    autoDownloadFontAwesome : undefined,
    element      : markdownEditor,
    spellChecker : false,
    forceSync    : true,
    showIcons    : ["strikethrough", "horizontal-rule"],
    promptURLs   : true,
    blockStyles : {
        italic : "_",
    },
    autosave     :  {
        enabled : true,
        uniqueId : window.location.pathname,
    },
});
