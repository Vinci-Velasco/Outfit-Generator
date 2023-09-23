window.onload = function() {
    const pathElements = document.getElementsByClassName("svg-fill");

    // change colour of all svgs to the colour specified in the dataset
    for (let path of pathElements) {
        const colour = path.dataset.colour;
        const saturation = path.dataset.saturation;
        path.style.fill=colour;
        path.style.filter = `saturate(${saturation}%)`
    }
};

// change colour box for top clothing form everytime colour is chosen
const topDropDownMenu = document.getElementById("id_top-form-colour");
topDropDownMenu.addEventListener("change", () => {
    const colour = topDropDownMenu.value;
    const topColourBox = document.getElementById("top-colour");
    topColourBox.style.backgroundColor = colour;
});

// change colour box for bottom clothing form everytime colour is chosen
const bottomDropDownMenu = document.getElementById("id_bottom-form-colour");
bottomDropDownMenu.addEventListener("change", () => {
    const colour = bottomDropDownMenu.value;
    const bottomColourBox = document.getElementById("bottom-colour");
    bottomColourBox.style.backgroundColor = colour;
});

// change colour box for shoes clothing form everytime colour is chosen
const shoesDropDownMenu = document.getElementById("id_shoes-form-colour");
shoesDropDownMenu.addEventListener("change", () => {
    const colour = shoesDropDownMenu.value;
    const shoesColourBox = document.getElementById("shoes-colour");
    shoesColourBox.style.backgroundColor = colour;
});
