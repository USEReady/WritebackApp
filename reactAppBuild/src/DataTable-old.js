import React, {useState, useEffect} from "react";
import './DataTable.css';
// import SelectGroup from './Selectgroup';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from "@material-ui/lab/Alert";
const {Config} = require('./Config.js');

//Needed
const useStyles = makeStyles({
    container: {
        paddingTop: "6%",
        borderTopStyle: "solid",
        marginTop: "3%",
    },
    userInfo: {
        padding: "5%",
        marginTop: "3%",
        backgroundColor: "white",
    },
    row: {
        padding: "4% 4% 4%",
        display: "grid",
        gridTemplateColumns: "28% 18%",
        gridGap: "6%",
    },
    label: {
        fontWeight: 900,
        fontSize: 11,
        fontFamily: "Trebuchet MS",
    },
    buttons: {
        float: "right",
        marginTop: "2%",
    },
    button: {
        marginRight: "10%",
        fontSize: 11,
        fontFamily: "Trebuchet MS",
        fontWeight: 600,
        paddingLeft:"4%",
        marginTop: "6%",
    },
    value: {
        fontSize: 11,
        fontFamily: "Trebuchet MS",
        fontWeight: 600,
    },
    savebtndiv: {
      width: "65px"
    },
    pl10: {
      paddingLeft:"10px"
    },
    input: {
        fontSize: 11,
        fontFamily: "Trebuchet MS",
        fontWeight: 600,
        width: "110px",
    },
    

  });
  const ColorButton = withStyles((theme) => ({
    root: {
      color: 'fff',
      backgroundColor: '#29ba74',
      "&:hover": {
        backgroundColor: '#239a4a'
      }
    }
  }))(Button);

/*This is the functional component */
let prevvalue = '';
let currentkey = '';
function DataTable(props) {
    const [editAdjustedForecast, setAdjustedForecast] = React.useState({});
    const [field, setField] = React.useState({});
    const [open, setOpen] = React.useState(false);
    const [erropen, setErrorOpen] = React.useState(false)
    const [userRole, setRole] = React.useState('');
    const [message, setMessage] = React.useState('');
    let writebackDataCopy = [];
    let writebackAuditCopy = [];
    const [username, setUsername] = React.useState();
    const [errorMsg, setErrormsg] = React.useState('Something Went Wrong!');
    const [inputvalue, setinputvalue] = React.useState('');


    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
          return;
        }
        setOpen(false);
        setErrorOpen(false);
      };

      /*Used to refresh worksheet data on success*/
    function CheckError(response) {
      if (response.status >= 200 && response.status <= 299) {
        refreshWorksheetData();
        return response.json();
      }
      else {
        console.log(response.statusText);
      }
    }
    
    /* This is the function that will use to save functinality*/
     const handleSave = () => {
       console.log("writbackcopy",JSON.stringify(writebackDataCopy))
       console.log("auditcopy",JSON.stringify(writebackAuditCopy))
      Promise.all([
        fetch(Config.rest_server_url+'updatedata', 
        { method: 'POST', 
        headers: { 'Content-Type': 'application/json', }, 
        body: JSON.stringify(writebackDataCopy), }),
        fetch(Config.rest_server_url+'audittable', 
        { method: 'POST', 
        headers: { 'Content-Type': 'application/json', }, 
        body: JSON.stringify(writebackAuditCopy), })
      ])
      .then(function (responses) {
        // Get a JSON object from each of the responses
        return Promise.all(responses.map(function (response,index) {
          if (response.status >= 200 && response.status <= 299) {
                if(index == 0){
                  setOpen(true);
                  CheckError(response)
                }
                else {
                  return response.json()
                }
        }
        else {
          if(response.statusText == "") {
            setErrorOpen(true);
            setErrormsg('Error While Saving');
            if(index == 1){
             setErrormsg('Error in Audit Table')  
            }
          }
          else {
            setErrorOpen(true);
            setErrormsg(response.statusText);
          }  
        }
        
        }));
      }).then(function (data) {
        
      }).catch(function (error) {
        // if there's an error, log it
       // console.log("error",error)
        setErrorOpen(true);
      })

  }
  /* This is the function that will use to refresh Tableau Sheet Data*/
  function refreshWorksheetData(){
          const worksheet = props.selectedSheet;
          worksheet.getDataSourcesAsync().then(sources => {
            for (var src in sources){
              sources[src].refreshAsync().then(function () {
                console.log(sources[src].name + ': Refreshed Successfully');
              });
            }
        })
    }
/* This is the function that will get Tableau Data*/
    const getTableContent = headers => {
      console.log("rows",props.rows)
      if(currentkey != props.rows[0][0] && props.rows.length > 0 && headers.length > 0){
      
        let content = [];
        let column_name = '';
        let headersName = '';
       
        console.log("headers",headers);
         
        
           currentkey =  props.rows[0][0];
           console.log("key==>",currentkey);
          for( let j =0;j< props.rows.length;j++) {
            console.log("inside for j");
            debugger;
              let writebackData = new Object();
              let writeBackAuditdata = new Object();
                for(let i=0;i<headers.length;i++) {
                  let keys = headers[i];
                  let values = props.rows[j][i]
                      if(keys == "Measure Names") {
                        const measureKeyvalue = values.split('].[').join(',').split(':');
                          writebackData['Measure Names'] = measureKeyvalue[1];
                           if(props.rows[j][headers.indexOf("WB_SourceValue")] == measureKeyvalue[1]) {
                            column_name = 'WBValue';
                          }
                      }
                      else if( keys == "Measure Values") {
                        writebackData['WBValue'] = values.toString();
                        writeBackAuditdata['WB_Value'] = values.toString();
                      }
                      else if (keys =="WB_PrimaryKey") {
                        writebackData['WBPrimaryKey'] = values;
                        headersName = values;
                        writeBackAuditdata['WB_PrimaryKey_Value'] = values;
                      }
                      else if(keys == "AsUser") {
                      
                        writeBackAuditdata['WB_User'] = values;
                      }
                      else if(keys == "WB_DashboardName") {
                        writebackData['WBDashboardName'] = values;
                        writeBackAuditdata['WB_Dashboard_name'] = values;
                      }
                      
                      else {
                        writebackData[keys] = values;
                      }
                      
                      if(j == 0){
                      if(keys == 'AsUser' || keys == 'Role' || keys == 'ContractDate'){
                            if(keys == 'ContractDate') {
                                let monthNum  = values%100;
                                const months = [ "January", "February", "March", "April", "May", "June", 
                                "July", "August", "September", "October", "November", "December" ];
                                values = months[monthNum-1] + ' ' + values.toString().substring(0,4);
                            }
                            content.push(
                              <div className={classes.row} id="form">
                              <label className={classes.label} >{keys}</label>
                              <span className={classes.value}>{values}</span>
                              </div>
                            );
                      }
                    }
                      if(keys == 'Measure Values') {
                        //setinputvalue(values);
                        console.log("values==>",values)
                        console.log("prevvlaue==>",prevvalue)
                        if(prevvalue != values){
                          console.log("if")
                          setinputvalue(values)
                          prevvalue = values;
                        }
                        console.log("values==>", values)
                        if(props.rows[j][headers.indexOf("Role")].includes('Interactor') &&  column_name == "WBValue") {   // 
                          content.push(
                            <React.Fragment>
                                  <div className={classes.row}>
                                   <label className={classes.label} >WBValue</label>   {/* placeholder={values.toFixed(Config.WB_Decimal)}  key={Math.random()} onBlur={setonblur}*/}  
                                  <input type="number" step="0.01" className={classes.input} key={Math.random()} defaultValue={inputvalue}  name={keys} headerRow={headersName} onChange={handleInputChange}></input>
                                  </div>
                          </React.Fragment>
                          );
                          if(props.rows.length - j == 1){
                            content.push(<div className={classes.row + ' ' + classes.savebtndiv}>
                            <ColorButton className={classes.button+ ' '+ classes.pl10} variant="contained" color="primary" onClick={handleSave}>Save</ColorButton></div>)
                          }
                      }
                      else {
                        content.push(
                          <React.Fragment>
                          <div className={classes.row} id="form">
                          <label className={classes.label} >WBValue</label>
                          <span className={classes.value}>{values.toFixed(Config.WB_Decimal)}</span>
                          </div>
                          </React.Fragment>
                          );
                          if(props.rows.length - j == 1){
                           content.push(<div className={classes.row + ' ' + classes.savebtndiv}>
                           <ColorButton className={classes.button+ ' '+ classes.pl10} disabled variant="contained" color="secondary">Save</ColorButton>
                           </div>)
                          }
                      }
                      }
                }

              writebackDataCopy = [...writebackDataCopy,writebackData];
              writebackAuditCopy = [...writebackAuditCopy,writeBackAuditdata];
           }
         
           console.log("writebackdata==>",writebackDataCopy);
           console.log("writebAudit==>",writebackAuditCopy)
          
        return content;
      }
      };

      const setonblur = event => {
        const getval = event.target.value;
        console.log("onblurval==>", getval)
      }
/* This is the function that uses for Input type operation*/
    const handleInputChange = event => {
        const target = event.target;
        const value = target.value;
        const keyName = target.name;
        const rowHeader = event.currentTarget.attributes['headerRow'].value;
     
       // writebackData[keyName] = value;
       console.log("rowheader",rowHeader);
       for(let i=0; i<writebackDataCopy.length;i++){
         console.log("wb==>", writebackDataCopy[i]['WBValue'])
         if(writebackDataCopy[i]['WBPrimaryKey'] == rowHeader){
          writebackDataCopy[i]['WBValue'] = value;
          writebackAuditCopy[i]['WB_Value'] = value;
          setinputvalue(value)
        }
      
       }
        
    }
    function Alert(props) {
      return <MuiAlert elevation={6} variant="filled" {...props} />;
    }
    const classes = useStyles();
    return (
        <div className={classes.container}>
          {/* <SelectGroup></SelectGroup> */}
        <div>
          
            {getTableContent(props.headers)}
        </div>
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose} >
        <Alert onClose={handleClose} >
        Saved Successfully !!
        </Alert>
      </Snackbar>
       <Snackbar open={erropen} autoHideDuration={6000} onClose={handleClose} >
        <Alert onClose={handleClose} severity="error">
        {errorMsg}
        </Alert>
      </Snackbar> 

    </div>
        )
}

export default DataTable;
