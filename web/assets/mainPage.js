document.addEventListener('DOMContentLoaded', () => {
    let joinGameForm = document.querySelector("#join-game-room");
    // console.log(joinGameForm)

    joinGameForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const roomCode = document.getElementById('roomcode').value;

        if (validateRoomID(roomCode)) {
            const url = `/room/${encodeURIComponent(roomCode)}?username=${encodeURIComponent(username)}`;
            window.location.href = url;
        } else {
            alert('Invalid room code. Please try again.');
        }
    })

    function validateRoomID(roomCode) {
        const isValid = /^[A-Za-z0-9]{8}$/.test(roomCode);
        return isValid;
    }
});