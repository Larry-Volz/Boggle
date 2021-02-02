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

    letter = $(evt.target).closest(".game-cells").text().toString().trim();
    x = $(evt.target).closest(".game-cells").data('x')
    y = $(evt.target).closest(".game-cells").data('y')

    console.table(seen)
    console.log(`x:${x}, y:${y} `)
    if (seen.some(xyInArray)) {
        console.log(`${x},${y} ALREADY IN ARRAY`)
    } else {
        seen.push({ 'x': x, 'y': y })
        console.log(`${x},${y} ADDED TO ARRAY`)
    }

    // lastX=x;
    // lastY=y;

    console.log(`x: ${x} y: ${y}`)
    $(evt.target).css("background-color", "rgb(0,0,128,0.5)");
    console.log("MOUSEDOWN")
    console.log(`letter: ${letter}`)
});

$('.game-cells').on("mouseover", (evt) => {
    evt.preventDefault();
    if (mouseDown) {
        // $(evt.target).toggleClass("bg-primary", "bg-white");
        $(evt.target).css("background-color", "rgb(0,0,128,0.5)");

        letter = $(evt.target).text().toString().trim();

        x = $(evt.target).closest(".game-cells").data('x')
        y = $(evt.target).closest(".game-cells").data('y')

        console.log(`MOUSEOVER x:${x} y:${y} : ${letter}`)
    }
});

$('.game-cells').on("mouseout", (evt) => {
    evt.preventDefault();
    if (mouseDown) {

        word += letter;
        console.log(`MOUSEOUT letter: ${letter} word: ${word}`)
    }
});

// on mouseup - make them into a word
$(window.document).on('mouseup touchend', (event) => {
    // Capture this event anywhere in the document, since the mouse may leave our element while mouse is down and then the 'up' event will not fire within the element.
    mouseDown = false;
    word += letter;
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
    return (val[idx]['x'] == x && val[idx]['y'] == y);
};
