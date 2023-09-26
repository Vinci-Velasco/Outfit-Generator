function getTintedOrShadedColour(colour, value) {
    if (value === 100) {
        return colour;
    }

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

    if (value > 100) {
        const tint_value = (value - 100) / 100;
        newRedDecimal = applyTint(redDecimal, tint_value);
        newBlueDecimal = applyTint(blueDecimal, tint_value);
        newGreenDecimal = applyTint(greenDecimal, tint_value);
    }
    else {
        const shade_value = value / 100;
        newRedDecimal = applyShade(redDecimal, shade_value);
        newBlueDecimal = applyShade(blueDecimal, shade_value);
        newGreenDecimal = applyShade(greenDecimal, shade_value);
    }

    let newRedHex = newRedDecimal.toString(16);
    let newBlueHex = newBlueDecimal.toString(16);
    let newGreenHex = newGreenDecimal.toString(16);

    if (newRedHex === "0") {
        newRedHex += "0";
    }

    if (newBlueHex === "0") {
        newBlueHex += "0";
    }

    if (newGreenHex === "0") {
        newGreenHex += "0";
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