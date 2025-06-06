import React, { Component } from 'react';
import { TextField, Button, Typography, Grid } from '@material-ui/core';
import { Link } from 'react-router-dom';

export default class Page3 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      RoomCode: '',
      error: ''

    };
    this.handleTextFieldChange = this.handleTextFieldChange.bind(this);
    this.roombuttonPressed = this.roombuttonPressed.bind(this);
  }

  render() {
    return (
      <Grid container spacing={1} direction="column" alignItems="center" justifyContent="center" style={{ minHeight: "100vh" }}>
        <Grid item xs={12}>
          <Typography variant="h4" gutterBottom>
            Join a Room
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <TextField
            error={!!this.state.error}
            label="Code"
            placeholder="Enter room code"
            value={this.state.RoomCode}
            helperText={this.state.error}
            variant="outlined"
            onChange={this.handleTextFieldChange}
          />
        </Grid>
        <Grid container spacing={1} alignItems="center" justifyContent="center" item xs={12}>
          <Grid item>
            <Button variant="contained" color="primary" onClick={this.roombuttonPressed} component={Link} to={this.roombuttonPressed}>
              Enter Room
            </Button>
          </Grid>
          <Grid item>
            <Button variant="contained" color="secondary" to="/" component={Link}>
              Back
            </Button>
          </Grid>
        </Grid>
      </Grid>
    );
  }

  handleTextFieldChange(e){
    this.setState({RoomCode: e.target.value});
  }

  roombuttonPressed() {
    console.log(this.state.RoomCode);
  };
}