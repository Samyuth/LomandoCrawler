import './App.css';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [tree, setTree] = useState([])
  
  useEffect(() => {
    const getData = async() => {
      try {
        const response = await axios.get('/');
        setTree(response.data)
      } catch(err) {
        console.log(err)
      }
    }
    getData();
  }, [])

  return (
    <div className="App">
      Welcome to the Lomando Crawler Application!
      { tree.map((level, i) => <p key={i}>
        { level.map(node => <button key={node}>{node}</button>)}
      </p>)}
    </div>
  );
}

export default App;
