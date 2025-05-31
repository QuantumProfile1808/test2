import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import Homepage from "./Homepage";
// This is the main App component that renders the Homepage component
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Page2 from "./Page2";
import Page3 from "./page3";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Homepage />;
      </div>
    );
  };
}

const appdiv = document.getElementById("app");
if (appdiv) {
  const root = createRoot(appdiv);
  root.render(<App />);
}