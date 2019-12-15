/*
    I made this a class instead of series of functions, because
    I found it would make more sense if the table would be
    a single unified component with shared properties instead
    of a collection of functions that pass around the same variables.
*/
import ajaxGet from "../ajaxGet";


type Articles = Array<string>;

class ArticleTable {

    private readonly articleURI : string = "/admin/articles/all";
    private articles : Promise<Articles>;
    private table : Element;
    private currentPage = 1;

    constructor(tableElement : Element){
        this.table = tableElement;
        this.articles = this.getArticles();
        this.setSearchEvent();
        this.render();
    }

    private async getArticles() : Promise<Articles>{
        const response : string = await ajaxGet(this.articleURI);
        return JSON.parse(response);
    }

    private async render(articles : Articles = null) : Promise<void>{
        /*Have to check for null explictly because "await"
          can't be used inside a function parameter*/
        const currentArticles = articles ? articles : (await this.articles);
        this.table.querySelector("tbody").innerHTML = currentArticles.join("");
    }


    private async search(key : string) : Promise<void> {
        const results : Articles = (await this.articles).filter((article) => {

            //In order to parse the HTML, a dummy element is created
            const element : HTMLElement = document.createElement("table");
            element.innerHTML = article.toLowerCase();
            const title : HTMLElement = <HTMLElement>element.querySelector(".article_title");

            if (title.innerText.includes(key.toLowerCase())){
                return article;
            }
        });

        this.render(results);
    }

    private setSearchEvent() : void {
        const input : HTMLInputElement = <HTMLInputElement>document.getElementById("article_search");
        input.addEventListener("keyup", () => {
            this.search(input.value);
        })
    }
}

new ArticleTable(document.getElementById("article_table"));
