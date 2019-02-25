import * as React from "react";
import { Route, RouteProps, Switch, Redirect } from "react-router-dom";
import Research from "./Research";
import Analytics from "./Analytics";
import Modelling from "./Modelling";
import ManagementData from "./Management";

import ResearchSoftware from "./Research";

import Development from "./Development";
import ManagementSoftware from "./Management";

export default class Hello extends React.Component<HelloProps, {}> {
  render() {
    return (
      <div>
        <div class="container">
          <hr />
          <div class="row">
            <div class="col-2">
              <div class="btn-group-vertical btn-group-sm">
                <a
                  href="#/software/development"
                  type="button"
                  class="btn btn-secondary"
                >
                  Development
                </a>
                <a
                  href="#/software/management"
                  type="button"
                  class="btn btn-secondary"
                >
                  Management
                </a>
              </div>
            </div>
            <div class="col-8">
              <Switch>
                <Route path="/software/development" component={Development} />
                <Route
                  path="/software/management"
                  component={ManagementSoftware}
                />
                <Redirect from="/software" exact to="/software/development" />
              </Switch>
            </div>
            <div class="col-2">
              <a
                class="twitter-timeline"
                data-width="220"
                data-theme="dark"
                href="https://twitter.com/RedHat?ref_src=twsrc%5Etfw"
              >
                Tweets by RedHat
              </a>{" "}
              <script
                async
                src="https://platform.twitter.com/widgets.js"
                charset="utf-8"
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
