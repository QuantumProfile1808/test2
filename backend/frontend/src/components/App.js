import React, { Component } from "react";
import { createRoot } from "react-dom/client";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Welcome to the React App</h1>
        <p>This is a simple React application.</p>
      </div>
    );
  }
}

const appdiv = document.getElementById("app");
if (appdiv) {
  const root = createRoot(appdiv);
  root.render(<App />);
}