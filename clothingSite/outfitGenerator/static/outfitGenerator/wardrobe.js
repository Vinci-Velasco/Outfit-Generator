window.onload = function() {
    let pathElements = document.getElementsByClassName("svg-fill");

    // change colour of all svgs to the colour specified in the dataset
    for (let path of pathElements) {
        let colour = path.dataset.colour;
        path.style.fill=colour; // change to HEX decimal value instead cause stuff like mauve is not recognized
    }
};