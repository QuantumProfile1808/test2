import React, { Component } from "react";
import ReactDOM from "react-dom";
import Homepage from "./Homepage";

export default class App extends Component {
  render() {
    return (
      <div className="center">
        <Homepage />
      </div>
    );
  }
}

const appdiv = document.getElementById("app");
if (appdiv) {
  ReactDOM.render(<App />, appdiv);
}