import React, { Component } from "react";
import ReactDOM from "react-dom";
import Homepage from "./Homepage";
import { BrowserRouter as Router } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <div className="center">
        <Router>
          <Homepage />
        </Router>
      </div>
    );
  }
}

const appdiv = document.getElementById("app");
if (appdiv) {
  ReactDOM.render(<App />, appdiv);
}