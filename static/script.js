function visibilityClicked(idVisible, idInvisible) {
    // console.log(idVisible);
    // console.log(idInvisible);
    visibleElement = document.getElementById(idVisible);
    invisibleElement = document.getElementById(idInvisible);


    // console.log(visibleElement.offsetParent === null);
    // console.log(invisibleElement.offsetParent === null);
    if (visibleElement.offsetParent === null) {
        visibleElement.style.display = 'block';
        invisibleElement.style.display = 'none';
    } else {
        visibleElement.style.display = 'none';
        invisibleElement.style.display = 'block';
    }


}

// waves-effect waves-light green btn
//waves-effect waves-light blue-grey darken-2 btn