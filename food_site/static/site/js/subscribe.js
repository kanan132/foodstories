let url = 'http://127.0.0.1:8000/api/v1/subscribe/';

let form = document.querySelector('.subscribe-form');


form.addEventListener('submit', function(event){
    event.preventDefault();
    let email = document.getElementById('email').value;
    let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let data = {
        'email': email,
    }


    let settings = {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(data)
    }
    fetch(url, settings)
    .then(response => response.json())
    .then(data => {
        if (data.email == email) {
            document.querySelector('#message p').innerText = 'Thank u 4 subscribing!';
        }
        else{
            document.querySelector('#message p').innerText = data.email;
        }
    })
})