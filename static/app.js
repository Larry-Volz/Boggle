let mouseDown = false;
let letter = "";
let word = "";
let seen = [];
let lastX;
let lastY;
let x;
let y;

// alert(seen.every(notEq))

//TODO: set up a timer functionality
//TODO: SET UP A point counter and game restart option subroutines
//TODO: clean up issue of making sure it doesn't count the same letter 2x using x & y id's

$('#board').on("mousedown touchstart", ".game-cells", (evt) => {
    evt.preventDefault(); //eliminate default highlighting of text
    mouseDown = true;

    //TODO: clear board for another round

    console.log(`MOUSEDOWN`)
    letter = $(evt.target).closest(".game-cells").text().toString().trim();
    x = $(evt.target).closest(".game-cells").data('x')
    y = $(evt.target).closest(".game-cells").data('y')

    // console.table(seen)
    // console.log(`x:${x}, y:${y} `)

    if (seen.some(xyInArray)) {
        console.log(`------`)
    } else {
        seen.push({ 'x': x, 'y': y })
        word += letter;
        console.log(`${letter} ADDED TO ARRAY`)
    }

    $(evt.target).removeClass("bg-white");
    $(evt.target).addClass("bg-primary");

    // console.log(`MOUSEDOWN x: ${x} y: ${y} letter: ${letter}`)
});

$('#board').on("mouseover", ".game-cells", (evt) => {
    evt.preventDefault();
    if (mouseDown) {
        
        $(evt.target).removeClass("bg-white");
        $(evt.target).addClass("bg-primary");
        
        letter = $(evt.target).text().toString().trim();
        x = $(evt.target).closest(".game-cells").data('x')
        y = $(evt.target).closest(".game-cells").data('y')
        
        console.log(`MOUSE-OVER`)
        if (seen.some(xyInArray)) {
            console.log(`------`)
        } else {
            seen.push({ 'x': x, 'y': y })
            word += letter;
            console.log(`${letter} ADDED TO ARRAY`)
        }

    }
});

$('.game-cells').on("mouseout", (evt) => {
    evt.preventDefault();
    if (mouseDown) {

        console.log(`MOUSEOUT`)
        if (seen.some(xyInArray)) {
            console.log(`------`)
        } else {
            seen.push({ 'x': x, 'y': y })
            word += letter;
            console.log(`${letter} ADDED TO ARRAY`)
        }
    }
});

// on mouseup - make them into a word
$(window.document).on('mouseup touchend', (event) => {
    // Capture this event anywhere in the document, since the mouse may leave our element while mouse is down and then the 'up' event will not fire within the element.
    mouseDown = false;
    
    if (word.length > 0) {
        console.log(`MOUSEUP - word is ${word}`);

        //TODO: put word into session[]
        //TODO POST a form to the backend to check if it's in the list
        //TODO: back-end to do testing against db
        //TODO: award points if appropriate
        //TODO: check timer - do ending routine if time is overwith
    };

});




function xyInArray(val, idx) {
    //to be used in every
    //xy format [{'x':x,'y':y}, {},{}]
    //xy2 format {'x':x,'y':y} <-- passed from outside as global var
    // console.log(val['x'] == x && val['y'] == y);
    return (val['x'] == x && val['y'] == y);
};
