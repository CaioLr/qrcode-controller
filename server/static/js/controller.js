const socket = io({autoConnect: false});

const uuid = window.location.pathname.split('/')[2]
console.log('ID recebido:'+uuid)

const keys = ["a", "s", "d", "f","ArrowUp","ArrowLeft","ArrowRight","ArrowDown"];

function sendMessage(value) {
    let key;
    typeof(value) == 'object' ? key = value.key : key = value;
    if (keys.includes(key)) {
        let message = key;
        let data = {
            'session_id':uuid,
            'message':message
        }
        socket.emit("handle_message", data);
    }
}

document.addEventListener('DOMContentLoaded', () => {

    socket.connect();

    socket.on("connect", function() {


        data = {'uuid':uuid, 'user':'controllerPage'}

        socket.emit("join_session", data);
    })

    document.addEventListener('keydown', (event) => {
        sendMessage(event);
    });
})




