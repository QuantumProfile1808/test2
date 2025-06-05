import React from "react";
import { useParams } from "react-router-dom";
import Room from "./Room";

export default function RoomWrapper(props) {
  const params = useParams();
  return <Room {...props} roomCode={params.roomCode} />;
}