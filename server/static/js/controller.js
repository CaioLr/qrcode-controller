const socket = io({autoConnect: false});

const uuid = window.location.pathname.split('/')[2]
console.log('ID recebido:'+uuid)

document.addEventListener('DOMContentLoaded', () => {

    socket.connect();

    socket.on("connect", function() {


        data = {'uuid':uuid, 'user':'controllerPage'}

        socket.emit("join_session", data);
    })

    document.getElementById("message").addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
        let message = document.getElementById("message").value;
        let data = {
            'session_id':uuid,
            'message':message
        }
        socket.emit("handle_message", data);
        document.getElementById("message").value = "";
    }
    })


})