import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Page2 from "./Page2";
import Page3 from "./Page3";

export default class Homepage extends Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<div>Welcome to the Homepage</div>} />
          <Route path="/Page2" element={<Page2/>} />
          <Route path="/Page3" element={<Page3 />} />
        </Routes>
      </Router>
    );
  }
}