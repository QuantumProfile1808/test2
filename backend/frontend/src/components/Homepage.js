import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Page2 from "./Page2";
import Page3 from "./page3";

export default class Homepage extends Component {
  render() {
    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<p>Welcome to the Homepage</p>} />
          <Route path="/Page2" element={<Page2 />} />
          <Route path="/Page3" element={<Page3 />} />
        </Routes>
      </Router>
    );
  }
}