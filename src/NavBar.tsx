
// <reference path='./index.d.ts'/>

import React from "react";

import Routes from "./Routes";
import {IntlProvider, FormattedMessage} from 'react-intl';
// tslint:disable-next-line:no-var-requires

const NavBar = () => (
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand  mb-0 h1" href="#">Buisson Diaz Conseil</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div className="collapse navbar-collapse" id="navbarSupportedContent">
    <ul className="navbar-nav mr-auto">
      <li className="nav-item">
        <a className="nav-link" href="/"><FormattedMessage
                    id="home"
                    defaultMessage="Home"
                    
                /> <span className="sr-only">(current)</span></a>
      </li>
      
      <li className="nav-item dropdown">
        <a className="nav-link dropdown-toggle" href="#/software" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <FormattedMessage
                    id="software"
                    defaultMessage="Software"
                    
                />
        </a>
        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
         
          <a className="dropdown-item" href="#/software/development"><FormattedMessage
                    id="development"
                    defaultMessage="Development"
                    
                /></a>
          <a className="dropdown-item" href="#/software/management"><FormattedMessage
                    id="management"
                    defaultMessage="Management"
                    
                /></a>
          
        </div>
      </li>

      <li className="nav-item dropdown">
        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <FormattedMessage
                    id="data"
                    defaultMessage="Data"
                    
                />
        </a>
        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
          <a className="dropdown-item" href="#/data/research"><FormattedMessage
                    id="research"
                    defaultMessage="Research"
                    
                /></a>
          <a className="dropdown-item" href="#/data/analytics"><FormattedMessage
                    id="analytics"
                    defaultMessage="Analytics"
                    
                /></a>
          <a className="dropdown-item" href="#/data/modelling"><FormattedMessage
                    id="modelling"
                    defaultMessage="Modelling"
                    
                /></a>
          
          
        </div>
      </li>

      <li className="nav-item dropdown">
        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <FormattedMessage
                    id="solutions"
                    defaultMessage="Solutions"
                    
                />
        </a>
        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
          <a className="dropdown-item" href="#/solution/trading"><FormattedMessage
                    id="trading"
                    defaultMessage="Trading"
                    
                /></a>
          <a className="dropdown-item" href="#/solutions/sports"><FormattedMessage
                    id="sport"
                    defaultMessage="Sport"
                    
                /></a>
          
          
        </div>
      </li>

      <li className="nav-item dropdown">
        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <FormattedMessage
                    id="company"
                    defaultMessage="Company"
                    
                />
        </a>
        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
        <a className="dropdown-item" href="#/company/history"><FormattedMessage
                    id="history"
                    defaultMessage="History"
                    
                /></a>
        <a className="dropdown-item" href="#/company/customers"><FormattedMessage
                    id="customers"
                    defaultMessage="Customers"
                    
                /></a>
          <a className="dropdown-item" href="#/company/team"><FormattedMessage
                    id="team"
                    defaultMessage="Team"
                    
                /></a>
          <a className="dropdown-item" href="#/company/contact"><FormattedMessage
                    id="contact"
                    defaultMessage="Contact"
                    
                /></a>
          
          
        </div>
      </li>
      
    </ul>

  </div>
</nav>);

export default NavBar;