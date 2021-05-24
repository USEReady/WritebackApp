import React, { useState, useEffect } from "react";
import Extension from "./Extension";
require("./App.css");
const {Config} = require('./Config.js'); 

//Needed
const { tableau } = window;

function App() {
  const [selectedSheet, setSelectedSheet] = useState(undefined);
  const [username, setUsername] = useState();

  useEffect(() => {
    tableau.extensions.initializeAsync().then(() => {
        const sheet = tableau.extensions.dashboardContent.dashboard.worksheets.find(worksheet => worksheet.name === Config.SheetName[Config.SheetName.indexOf(worksheet.name)]);
         console.log("appshhet", sheet)
        sheet.getSummaryDataAsync().then(info => {
          const username = info.data[0][1].value;
         console.log("app-username=>", username)
          setUsername(username);
      })
    })
   // sendUsername();
  },[]);
return (
    <Extension/> 
  );
}

export default App;