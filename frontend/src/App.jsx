import { useEffect, useState } from "react";
import api from "./lib/api";

function App() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    api
      .get("/health")
      .then((response) => {
        setStatus(response.data.status);
      })
      .catch(() => {
        setStatus("Backend unavailable");
      });
  }, []);

  return (
    <div>
      <h1>AP3</h1>
      <p>AI-Powered Placement Preparation Portal</p>
      <p>Backend status: {status}</p>
    </div>
  );
}

export default App;