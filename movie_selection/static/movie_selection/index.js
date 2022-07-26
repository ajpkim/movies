/***
    This script allows users to create a new room or join an existing room.
***/

document.querySelector('#join-room-input').focus();

// Create room and send User there
document.querySelector('#create-room-btn').onclick = function(e) {
    const roomName = "ABC";
    window.location.pathname = '/movie_selection/' + roomName + '/';
};

// // Send User to existing room
// document.querySelector('#join-room-input').onkeyup = function(e) {
//     if (e.keyCode === 13) {  // enter, return
//         document.querySelector('#join-room-btn').click();
//     }
// };
// document.querySelector('#join-room-btn').onclick = function(e) {
//     var roomName = document.querySelector('#join-room-input').value;
//     window.location.pathname = '/movie_selection/' + roomName + '/';
// };
