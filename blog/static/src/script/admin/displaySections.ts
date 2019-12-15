class Section {

    private button : HTMLElement;
    private body   : HTMLElement;

    constructor(button: HTMLElement, body: HTMLElement){
        this.button = button;
        this.body   = body;
    }

    public hide() : void {
        this.body.classList.add("hidden");
        this.button.classList.remove("underlined");
    }

    public display() : void {
        this.body.classList.remove("hidden");
        this.button.classList.add("underlined");
    }

    public setClickEvent(otherSection : Section) : void {
        this.button.addEventListener("click", () => {
            this.display();
            otherSection.hide();
            sessionStorage.setItem("currentSection", this.button.id);
        })
    }
}

const articleBody       = <HTMLElement>document.getElementById("edit_articles");
const articleButton     = <HTMLElement>document.getElementById("article_menu_button")
const descriptionBody   = <HTMLElement>document.getElementById("edit_description");
const descriptionButton = <HTMLElement>document.getElementById("description_menu_button")

const articleSection     : Section = new Section(articleButton, articleBody)
const descriptionSection : Section = new Section(descriptionButton, descriptionBody)

articleSection.setClickEvent(descriptionSection);
descriptionSection.setClickEvent(articleSection);

const currentSection : string = sessionStorage.getItem("currentSection");

if (currentSection){
    document.getElementById(currentSection).click();
}

