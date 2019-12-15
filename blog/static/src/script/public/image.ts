/*
    Append "pure-img" class to all <img> tags
 */

Array.from(document.getElementsByTagName("img")).forEach((image) => {
    image.classList.add("pure-img");
    //image.style.maxWidth = "70%";
})
