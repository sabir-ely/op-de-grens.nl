const buttonArray : Array<Element> = Array.from(document.getElementsByClassName("remove_message"));

buttonArray.forEach((button : Element) => {
    button.addEventListener("click", () => {
        const messageBox = <Element>button.parentNode.parentNode;
        messageBox.innerHTML = null;
    })
})
