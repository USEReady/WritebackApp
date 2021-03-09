import React from 'react'
const {Config} = require('./Config.js');

/*Used to Fetch Userrole */
export function fetchUserRole(username='appadmin') {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({'username' : username})
    };
    return fetch(Config.rest_server_url+'getuserrole', requestOptions)
            .then(response => {
               return response.json()
            });
            // .then(data => this.setRole(data));
}


