import React from "react";
import Button from '@material-ui/core/Button';
const {Config} = require('./Config.js');

class TestInsertEndPoints extends React.Component {
    constructor(props) {
        super(props);
        this.state = {  }
        this._textInp='1001'
        this._textUp='1001'
        this.handleSave=this.handleSave.bind(this);
        this.handleInputChange=this.handleInputChange.bind(this);
        this.handleUserRole=this.handleUserRole.bind(this);

        this.handleUpdate=this.handleUpdate.bind(this);
        this.handleUpdateChange=this.handleUpdateChange.bind(this);
    }

    handleUpdate(e){
        try{
            let update_key={
                sales:this._textUp
            }
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(update_key)
            };     
            fetch(Config.rest_server_url+'updatedata', requestOptions)
                .then(response => {
                console.log(response.json());
            });
        }
        catch(err)
        {
            console.log(err)
        }
    }
    handleUpdateChange(e){
        this._textUp=e.target.value
    }
    handleUserRole(e){
        try{
            let userobj={
                username:'ashwin_editor'
            }
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userobj)
            };     
            fetch(Config.rest_server_url+'getuserrole', requestOptions)
                .then(response => {
                console.log(response.json());
            });
        }
        catch(err)
        {
            console.log(err)
        }
    }
    handleInputChange(e){
        this._textInp=e.target.value
    }
    handleSave(e){
        try{
            let insert_key={
                rowid:this._textInp
            }
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(insert_key)
            };     
            fetch(Config.rest_server_url+'insertdata', requestOptions)
                .then(response => {
                console.log(response.json());
            });
        }
        catch(err)
        {
            console.log(err)
        }
    }
    render() { 
        return ( 
            <React.Fragment>
                <input type="text" onChange={this.handleInputChange}></input>
                <Button variant="contained"  onClick={this.handleUserRole}>
                    GetUserRole
                </Button>
                <Button variant="contained"  onClick={this.handleSave}>
                    InsertToDb
                </Button> 

                <input type="text" onChange={this.handleUpdateChange}></input>
                
                <Button variant="contained"  onClick={this.handleUpdate}>
                    UpdateDb
                </Button>
            </React.Fragment>
         );
    }
}
 
export default TestInsertEndPoints;