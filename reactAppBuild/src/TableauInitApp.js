import React, { Component } from 'react'
import Extension from "./Extension";
import {fetchUserRole} from './restUtil';
const {Config} = require('./Config.js'); 
const { tableau } = window;

class TableauInitApp extends Component {
    constructor(props) {
        super(props)

        this.state = {
            'username':'',
            'role':''
        }
    }
    componentDidMount() {
        console.log("under comp did mount")
        if(this.state.username === ''){
            tableau.extensions.initializeAsync().then(() => {
                const sheet = tableau.extensions.dashboardContent.dashboard.worksheets.find(worksheet => worksheet.name === Config.sheet1);
                console.log(sheet)
                sheet.getSummaryDataAsync().then(info => {
                const username = info.data[0][1].value;
                console.log(username)
                this.setUserRole(username,fetchUserRole(username))
                });
            });
        }
    }

    setUserRole(username,data){
        this.setState({'username':username,'role':data})
    }

    render() {
        return (
            <Extension username={this.state.username} role={this.state.role}/> 
        )
    }
}

export default TableauInitApp