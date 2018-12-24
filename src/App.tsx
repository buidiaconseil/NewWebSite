// <reference path='./index.d.ts'/>

import React from "react";
import { HashRouter, Link } from "react-router-dom";

import Routes from "./Routes";
import NavBar from "./NavBar";
import Footer from "./Footer";

// tslint:disable-next-line:no-var-requires
const reactLogo = require("./assets/React-icon.png");

const App = () => (
  <HashRouter>
    <div> <NavBar />
    
    <main className="container">
      
      
      <Routes />
    </main>
    <Footer />
    </div>
  </HashRouter>
);

export default App;
