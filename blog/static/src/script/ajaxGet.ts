/*Adapted from https://stackoverflow.com/a/30008115*/

export default function ajaxGet (url : string) : Promise<string> {
    /*A simple XMLHttpRequest GET wrapped in a Promise */

    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.onload = <any>function () {
            if (this.status >= 200 && this.status < 300) {
                resolve(xhr.response);
            } else {
                reject({
                    status: this.status,
                    statusText: xhr.statusText
                });
            }
        };

        xhr.onerror = <any>function () {
            reject({
                status: this.status,
                statusText: xhr.statusText
            });
        }
        xhr.send(null);
    });
}

