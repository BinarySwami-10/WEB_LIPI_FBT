var destinations = [
    "Enter Destination Here",
    "Goa...                ",
    "Ooty..                ",
    "Srinagar, Kashmir     ",
    "Rishikesh             ",
    "Ladakh                ",
    "Jim Corbett Wildlife Safari",
];
resetTravelDestinationInput= () => {
    $('#holidayDestinationInput').attr( 'placeholder',"");
}


resetTravelDestinationInput()
destindex=0
finished=0
function writePiece(word, iteration) {
    if (destindex>=destinations.length-1) {
        console.log('destindex')
        destindex=0
    }

    if (iteration == word.length ) {
        finished=1;
        resetTravelDestinationInput()
        writePiece(destinations[++destindex], 0);
        return finished
    };

    setTimeout(function() {
        $('#holidayDestinationInput').attr( 'placeholder',$('#holidayDestinationInput').attr('placeholder') + word[iteration++] );
        writePiece(word, iteration);
    },100);

}


writePiece(destinations[destindex],0)



// for (var i = 0; i < destinations.length; i++) {
//     writePiece(destinations[i],0);
//     console.log(destinations[i])
// }
// Call the function to begin the typing process

