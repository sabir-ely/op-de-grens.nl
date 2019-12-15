// Apply polyfills
import "classlist-polyfill";
import * as promisePolyfill from "promise-polyfill";
declare global { interface Window { Promise; }}
if (!window.Promise){
    window.Promise = promisePolyfill
};


// Load all scripts
// using "require()" because Typescript doesn't allow "import" inside conditionals
if (document.getElementById("admin_main_page")){
    require("./script/admin/loadArticleTable");
    require("./script/admin/displaySections");
    require("./script/admin/removeMessage");
}
else if (document.getElementById("text_editor")){
    require("./script/admin/simplemde");
}

//Import styles
import "./style/admin/index.scss";
