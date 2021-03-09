import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

const useStyles = makeStyles((theme) => ({
    button: {
      display: 'block',
      marginTop: theme.spacing(2),
    },
    formControl: {
      margin: theme.spacing(1),
      minWidth: 120,
    },
  }));
function SelectGroup() {
    const classes = useStyles();
  const [table_name, table_namefn] = React.useState('');
  const [col_name, col_namefn] = React.useState('');
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);

  const handleChange = (event) => {
    table_namefn(event.target.value);
  };
  const handleChangecolmn = (event) => {
    col_namefn(event.target.value)
  };

  const handleClose = () => {
    setOpen(false);
  };
  const handleClosecolm = () => {
    setOpen1(false);
  };
  const handleOpen = () => {
    setOpen(true);
  };
  const handleOpencolmn = () => {
    setOpen1(true);
  };
return(
    <div>
        <div class="col-sm-12">
       <FormControl className={classes.formControl}>
        <InputLabel id="demo-controlled-open-select-label">WB table name</InputLabel>
        <Select
          labelId="demo-controlled-open-select-label"
          id="demo-controlled-open-select"
          open={open}
          onClose={handleClose}
          onOpen={handleOpen}
          value={table_name}
          onChange={handleChange}
        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          <MenuItem value={10}>Forecast</MenuItem>
          <MenuItem value={20}>Sales</MenuItem>
        </Select>
      </FormControl>
      </div>
      <div class="col-sm-12">
       <FormControl className={classes.formControl}>
        <InputLabel id="demo-controlled-open-select-label1">WB Column name</InputLabel>
        <Select
          labelId="demo-controlled-open-select-label1"
          id="demo-controlled-open-select1"
          open={open1}
          onClose={handleClosecolm}
          onOpen={handleOpencolmn}
          value={col_name}
          onChange={handleChangecolmn}
        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          <MenuItem value={1}>Category</MenuItem>
          <MenuItem value={2}>Customer_Name</MenuItem>
          <MenuItem value={3}>Sales</MenuItem>
          <MenuItem value={4}>Customer_ID</MenuItem>
          <MenuItem value={5}>Profit</MenuItem>
          <MenuItem value={6}>Ship_Date</MenuItem>
          <MenuItem value={5}>Order_Date</MenuItem>
          <MenuItem value={6}>Forecast_Amount</MenuItem>
        </Select>
      </FormControl>
      </div>
    </div>
)
}

export default SelectGroup