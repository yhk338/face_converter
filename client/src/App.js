import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';
import './styles.css';
import Header from './components/Header';
import ImageInput from './components/ImageInput';
import ImageOutput from './components/ImageOutput';


function App() {
  return (
    <div className="App">
      <Header />
      <ImageInput />
      <ImageOutput />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
