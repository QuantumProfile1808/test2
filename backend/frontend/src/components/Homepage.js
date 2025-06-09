import React, { Component } from "react";
import { Routes, Route, Link, Navigate } from "react-router-dom";
import Page2Wrapper from "./Page2Wrapper";
import Page3Wrapper from "./Page3Wrapper";
import RoomWrapper from "./RoomWrapper";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";

export default class Homepage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      roomCode: null,
    };
    this.clearRoomCode = this.clearRoomCode.bind(this);
  }

  async componentDidMount() {
    fetch("/api/user-in-room")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          roomCode: data.code,
        });
      });
  }

  renderHomePage() {
    return (
      <Grid container spacing={3}>
        <Grid item xs={12} align="center">
          <Typography variant="h3" component="h3">
            House Party
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <ButtonGroup disableElevation variant="contained" color="primary">
            <Button color="primary" to="/Page2" component={Link}>
              Join a Room
            </Button>
            <Button color="secondary" to="/Page3" component={Link}>
              Create a Room
            </Button>
          </ButtonGroup>
        </Grid>
      </Grid>
    );
  }

  clearRoomCode() {
    this.setState({
      roomCode: null,
    });
  }

  render() {
    return (
      <Routes>
        <Route
          path="/"
          element={
            this.state.roomCode ? (
              <Navigate to={`/room/${this.state.roomCode}`} />
            ) : (
              this.renderHomePage()
            )
          }
        />
        <Route path="/Page2" element={<Page2Wrapper />} />
        <Route path="/Page3" element={<Page3Wrapper />} />
        <Route
          path="/room/:roomCode/*"
          element={<RoomWrapper leaveRoomCallback={this.clearRoomCode} />}
        />
      </Routes>
    );
  }
}