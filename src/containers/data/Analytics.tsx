import React from "react";
import Introduction from "./Introduction";
import Condensateur from "./Condensateur";
import CrimeUSA from "./CrimeUSA";
import AirBnbTrans from "./AirBnbTrans";
import { Switch, Route } from 'react-router';

const Development = () => (
  <div >
    <hr/>
    <div className="container">
     <div className="row">
      <div className="col-sm-2">
      <ul className="nav flex-column">
  <li className="nav-item">
    <a className="nav-link" href="#/data/analytics">Introduction</a>
  </li>
  
  <li className="nav-item">

    <a className="nav-link" href="#/data/analytics/condensateur">Example:Capacitor </a>
  </li>
  <li className="nav-item">

    <a className="nav-link" href="#/data/analytics/crimeusa">Example:USA Crime </a>
  </li>
  <li className="nav-item">

    <a className="nav-link" href="#/data/analytics/airbnb">Example:Air Bnb </a>
  </li>

  
</ul>
      </div>
      <div className="col-md-7">
      <Switch>
      <Route exact path="/data/analytics" component={Introduction}/>
  <Route path="/data/analytics/condensateur"  component={Condensateur}/>
  <Route path="/data/analytics/crimeusa"  component={CrimeUSA}/>
  <Route path="/data/analytics/airbnb"  component={AirBnbTrans}/>
  
      <Introduction />
      </Switch>
      
      </div>
    
    </div>
      </div>
      </div>
    );

export default Development;
