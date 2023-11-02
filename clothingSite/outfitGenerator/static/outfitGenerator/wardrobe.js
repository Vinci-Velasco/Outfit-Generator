/**
 * Adds tint or shade to hex colour string
 * @param {string} colour The hex colour
 * @param {integer} value The tint/shade value (from 0 - 200 inclusive)
 * @returns tinted/shaded hex colour (as string)
 */
function getTintedOrShadedColour(colour, value) {
    if (value === 100) {
        return colour;
    }

    // convert hex to decimal RGB
    const redHex = colour.slice(1, 3);
    const blueHex = colour.slice(3, 5);
    const greenHex = colour.slice(5);
    const redDecimal = parseInt(redHex, 16);
    const blueDecimal = parseInt(blueHex, 16);
    const greenDecimal = parseInt(greenHex, 16);

    let newRedDecimal;
    let newBlueDecimal;
    let newGreenDecimal;
    let newColour;

    // get new decimal RGB by applying tint
    if (value > 100) {
        const tint_value = (value - 100) / 100;
        newRedDecimal = applyTint(redDecimal, tint_value);
        newBlueDecimal = applyTint(blueDecimal, tint_value);
        newGreenDecimal = applyTint(greenDecimal, tint_value);
        console.log(newRedDecimal);
    }

    // get new decimal RGB by applying shade
    else {
        const shade_value = value / 100;
        newRedDecimal = applyShade(redDecimal, shade_value);
        newBlueDecimal = applyShade(blueDecimal, shade_value);
        newGreenDecimal = applyShade(greenDecimal, shade_value);
    }

    // convert back to hex
    let newRedHex = newRedDecimal.toString(16);
    let newBlueHex = newBlueDecimal.toString(16);
    let newGreenHex = newGreenDecimal.toString(16);

    // each hex value should have 2 digits, so prepend a 0 if needed
    if (newRedHex.length == 1) {
        newRedHex = "0" + newRedHex;
    }

    if (newBlueHex.length == 1) {
        newBlueHex = "0" + newBlueHex;
    }

    if (newGreenHex.length == 1) {
        newGreenHex = "0" + newGreenHex;
    }

    newColour = `#${newRedHex}${newBlueHex}${newGreenHex}`;
    return newColour;
}

function applyTint(colourValue, tintValue) {
    return Math.round(colourValue + ((255 - colourValue) * tintValue));
}

function applyShade(colourValue, shadeValue) {
    return Math.round(colourValue * shadeValue)
}

function changeColourBox(formID, colourBoxID) {
    const colourMenu = document.getElementById(`${formID}-colour`);
    const colour = colourMenu.value;

    const tintOrShadeMenu = document.getElementById(`${formID}-tint_or_shade`);
    const tintOrShade = tintOrShadeMenu.value;

    const saturationMenu = document.getElementById(`${formID}-saturation`);
    const saturation = saturationMenu.value;

    const colourBox = document.getElementById(colourBoxID);
    colourBox.style.backgroundColor = getTintedOrShadedColour(colour, tintOrShade);
    colourBox.style.filter = `saturate(${saturation}%)`
}

window.onload = function() {
    const pathElements = document.getElementsByClassName("svg-fill");

    // change colour of all svgs to the colour specified in the dataset
    for (let path of pathElements) {
        const colour = path.dataset.colour;
        const saturation = path.dataset.saturation;
        const value = path.dataset.tintshade;
        path.style.fill = getTintedOrShadedColour(colour, value);
        path.style.filter = `saturate(${saturation}%)`
    }

    // change colour box for top clothing form everytime colour/tint/shade/saturation is chosen
    const topColourMenu = document.getElementById("id_top-form-colour");
    topColourMenu.addEventListener("change", () => {
        changeColourBox("id_top-form", "top-colour");
    });

    const topTintOrShadeMenu = document.getElementById("id_top-form-tint_or_shade");
    topTintOrShadeMenu.addEventListener("change", () => {
        changeColourBox("id_top-form", "top-colour");
    });
    const topSaturationMenu = document.getElementById("id_top-form-saturation");
    topSaturationMenu.addEventListener("change", () => {
        changeColourBox("id_top-form", "top-colour");
    });

    // change colour box for top clothing form everytime colour/tint/shade/saturation is chosen
    const bottomColourMenu = document.getElementById("id_bottom-form-colour");
    bottomColourMenu.addEventListener("change", () => {
        changeColourBox("id_bottom-form", "bottom-colour");
    });

    const bottomTintOrShadeMenu = document.getElementById("id_bottom-form-tint_or_shade");
    bottomTintOrShadeMenu.addEventListener("change", () => {
        changeColourBox("id_bottom-form", "bottom-colour");
    });

    const bottomSaturationMenu = document.getElementById("id_bottom-form-saturation");
    bottomSaturationMenu.addEventListener("change", () => {
        changeColourBox("id_bottom-form", "bottom-colour");
    });

    // // change colour box for top clothing form everytime colour/tint/shade/saturation is chosen
    const shoesColourMenu = document.getElementById("id_shoes-form-colour");
    shoesColourMenu.addEventListener("change", () => {
        changeColourBox("id_shoes-form", "shoes-colour");
    });
    const shoesTintOrShadeMenu = document.getElementById("id_shoes-form-tint_or_shade");
    shoesTintOrShadeMenu.addEventListener("change", () => {
        changeColourBox("id_shoes-form", "shoes-colour");
    });
    const shoesSaturationMenu = document.getElementById("id_shoes-form-saturation");
    shoesSaturationMenu.addEventListener("change", () => {
        changeColourBox("id_shoes-form", "shoes-colour");
    });
};
