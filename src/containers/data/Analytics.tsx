import React from "react";
import Introduction from "./Introduction";
import Condensateur from "./Condensateur";
import CrimeUSA from "./CrimeUSA";
import AirBnbTrans from "./AirBnbTrans";
import { Switch, Route } from "react-router";

const Development = () => (
  <div>
    <hr />
    <h1>Analytics</h1>
    <div className="container">
      <div class="btn-group btn-group-sm">
        <a href="#/data/analytics" type="button" class="btn btn-secondary">
          Introduction
        </a>
        <a
          href="#/data/analytics/condensateur"
          type="button"
          class="btn btn-secondary"
        >
          Example: Capacitor
        </a>
      </div>
      <div class="btn-group btn-group-sm">
        <a
          href="#/data/analytics/crimeusa"
          type="button"
          class="btn btn-secondary"
        >
          Example: USA Crime{" "}
        </a>
        <a
          href="#/data/analytics/airbnb"
          type="button"
          class="btn btn-secondary"
        >
          Example: Air Bnb
        </a>
      </div>
      <div className="row">
        <div className="col">
          <Switch>
            <Route exact path="/data/analytics" component={Introduction} />
            <Route
              path="/data/analytics/condensateur"
              component={Condensateur}
            />
            <Route path="/data/analytics/crimeusa" component={CrimeUSA} />
            <Route path="/data/analytics/airbnb" component={AirBnbTrans} />

            <Introduction />
          </Switch>
        </div>
      </div>
    </div>
  </div>
);

export default Development;
