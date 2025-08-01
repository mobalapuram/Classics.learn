import { Routes, Route, Link } from 'react-router-dom';
import Index from './pages/index';
import React from 'react';
// import About from './pages/about';
import Generator from './pages/generator';
import Projects from './pages/projects';

function App () {
  return <div>
    <nav className="navbar">
        <Link to="/">Home</Link> 
        <Link to="/projects">Projects</Link>
        <Link to="/generator">Generator</Link>
        <Link to="/about">About</Link>
    </nav>

    <Routes>
      <Route path="/" element={<Index />} />
      {/* <Route path="/about" element={<About />} /> */}
      <Route path="/generator" element={<Generator />} /> 
      <Route path="/projects" element={<Projects />} />
    </Routes>
  </div>;
}

export default App;