const socket = io({autoConnect: false});
let uuid;

document.addEventListener('DOMContentLoaded', () => {
    //Getting QRcode
    fetch(window.location.href+'/set/')
    .then((response) =>  {

        uuid = response.headers.get('uuid');

        if (uuid) {
            console.log('ID recebido:', uuid);
        } else {
            console.error('Cabeçalho uuid não encontrado na resposta');
        }

        if (!response.ok) {
            throw new Error('QRcode was not ok');
        }

        return response.blob();
    })
    .then(blob => {

        const imageObjectURL = URL.createObjectURL(blob);
        const imgElement = document.createElement('img');
        imgElement.src = imageObjectURL;
        imgElement.style.width = '300px';

        const container = document.getElementById('imageContainer');
        container.innerHTML = '';
        container.appendChild(imgElement);
        
    })
    .catch(error => {
        console.error('Error getting QRcode:', error);
    });


    setTimeout(() => {

        socket.connect();

        socket.on("connect", function() {

            data = {'uuid':uuid, 'user':'mainPage'}

            socket.emit("join_session", data);
        })

        socket.on("new_message", function(data) {
            console.log('Controller: ', data.message)
        })
        
    }, 500); 


})