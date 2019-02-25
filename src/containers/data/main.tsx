import * as React from "react";
import { Route, RouteProps, Switch, Redirect } from "react-router-dom";
import Research from "./Research";
import Analytics from "./Analytics";
import Modelling from "./Modelling";
import ManagementData from "./Management";
import Sport from "./Sport";

export default class Hello extends React.Component<HelloProps, {}> {
  render() {
    return (
      <div class="container">
        <hr />
        <div class="row">
          <div class="col-2">
            <div class="btn-group-vertical btn-group-sm">
              <a href="#/data/research" type="button" class="btn btn-secondary">
                Research
              </a>
              <a
                href="#/data/analytics"
                type="button"
                class="btn btn-secondary"
              >
                Analytics
              </a>
              <a
                href="#/data/modelling"
                type="button"
                class="btn btn-secondary"
              >
                Modelling
              </a>
              <a href="#/data/sport" type="button" class="btn btn-secondary">
                Sports
              </a>
            </div>
          </div>
          <div class="col-8">
            <Switch>
              <Route path="/data/research" component={Research} />
              <Route path="/data/modelling" component={Modelling} />
              <Route path="/data/analytics" component={Analytics} />
              <Route path="/data/sport" component={Sport} />
              <Redirect from="/data" exact to="/data/research" />
            </Switch>
          </div>
          <div class="col-2">
            <a
              class="twitter-timeline"
              data-width="220"
              data-theme="dark"
              href="https://twitter.com/ML_NLP?ref_src=twsrc%5Etfw"
            >
              Tweets by ML_NLP
            </a>
            <script
              async
              src="https://platform.twitter.com/widgets.js"
              charset="utf-8"
            />
            <hr />
            <a
              href="https://twitter.com/intent/tweet?button_hashtag=MachineLearning&ref_src=twsrc%5Etfw"
              class="twitter-hashtag-button"
              data-show-count="false"
            >
              Tweet #MachineLearning
            </a>
            <script
              async
              src="https://platform.twitter.com/widgets.js"
              charset="utf-8"
            />
          </div>
        </div>
      </div>
    );
  }
}
