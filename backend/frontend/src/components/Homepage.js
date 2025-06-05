import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Page2 from "./Page2";
import Page3 from "./Page3";
import Room from "./Room";
import RoomWrapper from "./RoomWrapper";
import Page2Wrapper from "./Page2Wrapper";


export default class Homepage extends Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<div>Welcome to the Homepage</div>} />
          
          <Route path="/Page3" element={<Page3 />} />
          <Route path="/room/:roomCode" element={<RoomWrapper />} />
          <Route path="/Page2" element={<Page2Wrapper />} />
        </Routes>
      </Router>
    );
  }
}