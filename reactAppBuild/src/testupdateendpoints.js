import React  from "react";
import Button from '@material-ui/core/Button';
const {tableau} = window;
const {Config} = require('./Config.js'); 

class TestUpdateEndPoints extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'username':''
        }
        this._textForecast='1001'
        this._textForecastPeriod='1001'
        this._textAccountId='1001'

        this.handleUpdate=this.handleUpdate.bind(this);
        this.handleForecastChange=this.handleForecastChange.bind(this);
        this.handleForecastPeriodChange=this.handleForecastPeriodChange.bind(this);
        this.handleAccountIdChange=this.handleAccountIdChange.bind(this);
    }
    
    // componentDidUpdate(){
    //     tableau.extensions.initializeAsync().then(() => {
    //         const sheet = tableau.extensions.dashboardContent.dashboard.worksheets.find(worksheet => worksheet.name === 'Extension Input');
    //         console.log(sheet)
    //         sheet.getSummaryDataAsync().then(info => {
    //         const username = info.data[0][1].value;
    //         console.log(username)
    //         this.setState({'username':username})
    //         });
    //     });
    // }

    componentDidMount(){
        console.log("under comp did mount")
        if(this.state.username === ''){
            tableau.extensions.initializeAsync().then(() => {
                const sheet = tableau.extensions.dashboardContent.dashboard.worksheets.find(worksheet => worksheet.name === Config.sheet1);
                console.log(sheet)
                sheet.getSummaryDataAsync().then(info => {
                const username = info.data[0][1].value;
                console.log(username)
                this.setState({'username':username})
                });
            });
        }
    }

    handleUpdate(e){
        try{
            let update_payload={
                forecast:this._textForecast,
                forecast_period:this._textForecastPeriod,
                account_id:this._textAccountId
            }
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(update_payload)
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
    handleForecastChange(e){
        this._textForecast=e.target.value
    }
    handleForecastPeriodChange(e){
        this._textForecastPeriod=e.target.value
    }
    handleAccountIdChange(e){
        this._textAccountId=e.target.value
    }
    render() { 
        console.log(this)
        return ( 
            <React.Fragment>
                <b>{this.props.username}</b>
                <b>{this.props.role}</b>
                <input title="Type forecast value" type="text" onChange={this.handleForecastChange}></input>
                <input title="Type forecast period value" type="text" onChange={this.handleForecastPeriodChange}></input>
                <input title="Type account id value" type="text" onChange={this.handleAccountIdChange}></input>
                <Button variant="contained"  onClick={this.handleUpdate}>
                    UpdateDb
                </Button>
            </React.Fragment>
         );
    }
}
 
export default TestUpdateEndPoints;