import { useState, useEffect } from "react";
import axios from "axios";
function App() {
  const fetch = async () => {
    const response = await axios.post("http://localhost:5000", {
      item_name: "laptop",
    });

    console.log(response.data);
  };
  useEffect(() => {
    fetch();
  }, []);
  return <div>Hello World</div>;
}

export default App;
