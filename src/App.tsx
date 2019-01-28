// <reference path='./index.d.ts'/>

import React from "react";
import { HashRouter, Link } from "react-router-dom";

import Routes from "./Routes";
import NavBar from "./NavBar";
import Footer from "./Footer";
import {encode, decode} from "messagepack";
import msg from '../pyt/indicators-ETH-BTC.mpk';
var enc = new TextEncoder();
console.log(msg);
console.log(typeof(msg));
const decodedData = decode(msg);
console.log(decodedData); 
// tslint:disable-next-line:no-var-requires
const reactLogo = require("./assets/React-icon.png");

const App = () => (
  <HashRouter>
    <span > <NavBar />
    
      {decodedData}
      
      
      <Routes />
    
    <Footer />
    </span>
  </HashRouter>
);

export default App;
