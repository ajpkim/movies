/**
   This script enables adding nominations to the movie selection room
   nomination list using WebSockets.
**/

const roomName = JSON.parse(document.getElementById('room-name').textContent);

// Establish WebSocket connection
const selectionSocket = new WebSocket(
    'ws://'
        + window.location.host
        + '/ws/movie_selection/'
        + roomName
        + '/'
);
document.querySelector('#nomination-input').focus();
document.querySelector('#nomination-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#nomination-submit').click();
    }
};
// Send nomination on input submit
document.querySelector('#nomination-submit').onclick = function(e) {
    const nominationInput = document.querySelector('#nomination-input');
    const nomination = nominationInput.value;

    selectionSocket.send(JSON.stringify({
        'nomination': nomination,
    }));
    nominationInput.value = '';
};

// Add nominee to nomination list
selectionSocket.onmessage = function(e) {
    const nomination = JSON.parse(e.data).nomination;
    const nominationList = document.querySelector('#nominations-list');
    const nominationLi = document.createElement('li');
    nominationLi.appendChild(document.createTextNode(nomination));
    nominationList.appendChild(nominationLi);
};

selectionSocket.onclose = function(e) {
    console.error('Selection socket closed unexpectedly');
}
