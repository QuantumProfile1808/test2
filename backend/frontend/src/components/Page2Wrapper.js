import React from "react";
import { useNavigate } from "react-router-dom";
import Page2 from "./Page2";

export default function Page2Wrapper(props) {
  const navigate = useNavigate();
  return <Page2 {...props} navigate={navigate} />;
}