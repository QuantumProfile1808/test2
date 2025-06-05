import React, { Component } from "react";
import RoomWrapper from "./RoomWrapper";


export default class Room extends Component {
    constructor(props) {
      super(props);
      this.state = {
        VotesToSkip: 2,
        GuestCanPause: false,
        isHost: false,
    };
    this.roomCode = this.props.roomCode;;
  }

      componentDidMount() {
        this.getRoomDetails();
    }

    getRoomDetails() {
      fetch('/api/get-room?code=' + this.roomCode)
        .then((response) => response.json())
        .then((data) => {
          this.setState({
            VotesToSkip: data.votes_to_skip,
            GuestCanPause: data.guest_can_pause,
            isHost: data.is_host,
          });
        });
    }

    render() {
        return( <div>
            <h3>Room Code: {this.roomCode}</h3>
            <p>Votes {this.state.VotesToSkip} </p>
            <p>Guest Can Pause: {this.state.GuestCanPause.toString()}</p>
            <p>Host: {this.state.isHost.toString()}</p>
        </div>
        );
    }
}