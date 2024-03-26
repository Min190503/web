


import React from "react";

const today = new Date();

function formatDate(date) {
  return new Intl.DateTimeFormat("en-US", { weekday: "long" }).format(date);
}

export default function TodoList() {
  return <h1>Danh Sách Công Việc Cho Ngày {formatDate(today)}</h1>;
}