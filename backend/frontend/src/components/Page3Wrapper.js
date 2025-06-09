import React from "react";
import { useNavigate } from "react-router-dom";
import Page3 from "./Page3";

export default function Page3Wrapper(props) {
  const navigate = useNavigate();
  return <Page3 {...props} navigate={navigate} />;
}
