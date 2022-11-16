import { useState, useEffect } from "react";
import { FaSearch, FaArrowUp, FaArrowDown } from "react-icons/fa";
import axios from "axios";
function App() {
  const [results, setResults] = useState([]);
  const [input, setInput] = useState("");

  const [direction, setDirection] = useState(false);

  const fetch = async () => {
    try {
      const response = await axios.post("http://localhost:5000", {
        item_name: input,
      });

      setResults(response.data);
    } catch (err) {
      console.error(err);
    }
  };
  const handleSubmit = () => {
    fetch();
  };

  const sortByPrice = () => {
    setDirection(!direction);
    const sorted = [...results].sort((a, b) =>
      direction ? a.Price - b.Price : b.Price - a.Price
    );
    setResults(sorted);
    console.log(sorted);
    console.log("SORTED");
  };

  return (
    <div className="bg-orange-400 min-h-screen flex">
      <div className="flex flex-col h-screen w-[20vw] justify-center items-center">
        <h1 className="text-4xl font-bold pb-5">Pricely - RPA</h1>
        <div className="flex w-full justify-center items-center">
          <input
            placeholder="Enter product name"
            className="px-5 py-3 rounded-xl mx-2"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <div className="bg-slate-600 hover:cursor-pointer flex items-center p-3 rounded-xl">
            <button onClick={handleSubmit}>
              <FaSearch size={24} color="white" />
            </button>
          </div>
        </div>
      </div>
      <div className="px-5 py-5 overflow-hidden  bg-white">
        <div
          onClick={sortByPrice}
          className="bg-slate-600 hover:cursor-pointer inline-flex items-center text-white font-bold px-5 py-3 rounded-md"
        >
          <button className="mr-5">Sort By Price</button>
          {direction ? <FaArrowUp /> : <FaArrowDown />}
        </div>

        <table className="table-auto border-spacing-5">
          <thead className="">
            <tr>
              <th className=" px-5  outline-slate-400 outline-2">Name</th>
              <th className=" outline outline-slate-400 outline-2">Price</th>
            </tr>
          </thead>
          <tbody className="">
            {/* Here goes tables */}
            {results.map((item) => {
              return (
                <tr>
                  <td className="max-w-[60vw] truncate border px-5 py-3">
                    {item.Name}
                  </td>
                  <td className="border px-5 py-3 bg-slate-400">
                    {item.Price} $
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
