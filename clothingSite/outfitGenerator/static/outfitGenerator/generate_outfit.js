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
}