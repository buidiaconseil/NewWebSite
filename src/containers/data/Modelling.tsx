import React from "react";
import GeoModelling from "./GeoModelling";
import Chester from "./PredictChester";
import Introduction from "./IntroductionModel";
import { Switch, Route } from 'react-router';

const Development = () => (
  <div>
     <hr/>
    <div className="container">
     <div className="row">
      <div className="col-sm-2">
      <ul className="nav flex-column">
  <li className="nav-item">
    <a className="nav-link" href="#/data/modelling">Introduction</a>
  </li>
  
  <li className="nav-item">

    <a className="nav-link" href="#/data/modelling/krigeage">Example:Spatial Modelling</a>
  </li>
  <li className="nav-item">

    <a className="nav-link" href="#/data/modelling/chester">Example:Crime at Chester</a>
  </li>

  
</ul>
      </div>
      <div className="col-md-7">
      <Switch>
      <Route exact path="/data/analytics" component={Introduction}/>
  <Route path="/data/modelling/krigeage"  component={GeoModelling}/>
  <Route path="/data/modelling/chester"  component={Chester}/>
  
      <Introduction />
      </Switch>
      
      </div>
    
    </div>
      </div>
    
  </div>
);

export default Development;
