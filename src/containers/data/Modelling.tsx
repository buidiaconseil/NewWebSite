import React from "react";
import GeoModelling from "./GeoModelling";
import Chester from "./PredictChester";
import Introduction from "./IntroductionModel";
import { Switch, Route } from 'react-router';

const Development = () => (
  <div>
     <hr/>
     <h1>Modelling</h1>
    <div className="container">

    <div className="btn-group btn-group-sm">
    <a href="#/data/modelling" type="button" className="btn btn-secondary">Introduction</a>
    <a href="#/data/modelling/krigeage" type="button" className="btn btn-secondary">Example: Spatial Modelling</a>
    </div>
    <div className="btn-group btn-group-sm">
    <a href="#/data/modelling/chester" type="button" className="btn btn-secondary">Example: Crime at Chester </a>
    

</div>
     <div className="row">
      
      <div className="col">
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
