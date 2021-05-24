import React, {useState, useEffect} from "react";
import DataTable from "./DataTable";
import {fetchUserRole} from './restUtil';
const {tableau} = window;
const {Config} = require('./Config.js'); 

function Extension(props){
    const [isLoading, setIsLoading] = useState(true);
    const [selectedSheet, setSelectedSheet] = useState(undefined);
    const [sheetNames, setSheetNames] = useState([]);
    const [rows, setRows] = useState([]);
    const [headers, setHeaders] = useState([]);
    const [userRole, setRole] = React.useState('');
    const [userName, setUsername] = React.useState('');
    // console.log(props.role)
    let unregisterEventFn = undefined;
    let unregisterEventFnFilter = undefined;

    useEffect(() => {
        tableau.extensions.initializeAsync().then(() => {
            const sheetNames = tableau.extensions.dashboardContent.dashboard.worksheets.map(worksheet => worksheet.name);
            setSheetNames(sheetNames);

            const selectedSheet =  getSelectedSheet();
            setSelectedSheet(selectedSheet);
            console.log('selectedSheet==>',selectedSheet)           
            
            const sheetSelected = !!selectedSheet;
            // setIsLoading(sheetSelected);

            if(!!sheetSelected){
                loadSelectedMarks(selectedSheet);
            }
        })
    },[]);


    const getSelectedSheet = (sheet) => {
        const sheetName = sheet || selectedSheet;
        return tableau.extensions.dashboardContent.dashboard.worksheets.find(worksheet => worksheet.name === Config.SheetName[Config.SheetName.indexOf(worksheet.name)]);
    };
    const loadSelectedMarks = (sheet) => {
        if(unregisterEventFn){
            unregisterEventFn();
        }
        if(unregisterEventFnFilter){
            unregisterEventFnFilter();
        }
        
        const worksheet = getSelectedSheet(sheet);
        // const field = worksheet.fields;
        // setHeaders(field);
        worksheet.getSummaryDataAsync().then(info => {
            const username = info.data[0][1].value;
             console.log("extensionusername=>",username)
            setUsername(username)
           // setRole(fetchUserRole(username))
            });
        worksheet.getSelectedMarksAsync().then(marks => {
            const worksheetData = marks.data[0];
            // const name = worksheetData;
            // setName(name);
            console.log(worksheetData.data)
            const rows = worksheetData.data.map(row => row.map(cell => cell.value));
            const headers = worksheetData.columns.map(column => column.fieldName);
            setRows(rows);
            setHeaders(headers);
            setIsLoading(false);
        });
        unregisterEventFnFilter = worksheet.addEventListener(tableau.TableauEventType.FilterChanged, () => {
            setIsLoading(true);
            loadSelectedMarks(sheet);
        })
        unregisterEventFn = worksheet.addEventListener(tableau.TableauEventType.MarkSelectionChanged, () => {
            setIsLoading(true);
            loadSelectedMarks(sheet);
        })
    };

    const onSelectSheet = (sheet) => {
        tableau.extensions.settings.set('sheet',sheet);
        setIsLoading(true);
        tableau.extensions.settings.saveAsync().then(() => {
            setSelectedSheet(sheet);
            loadSelectedMarks(sheet);
        });
    };
/*This is part where extensions created*/
    const mainContent = (rows.length > 0)
        ? (<DataTable username={userName} role={userRole} rows={rows} headers={headers} selectedSheet={selectedSheet}/>)
        : (<h4>Please click on the table to update the value.</h4>);

let output = <div>{mainContent}</div>;
    return (
        <div>
        <div>{output}</div>
        </div>
    );

}

export default Extension;