
import './App.css';
import React from "react";
import Home from './components/home'
  

function App() {
  fetch('http://127.0.0.1:5000/start');

 

  return (
    <div className="App">
      <Home/>
    </div>
  );
};

export default App;

