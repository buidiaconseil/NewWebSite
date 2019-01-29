import React from "react";
import { Route, RouteProps, Switch } from "react-router-dom";
import { About, Home, Software } from "./containers";
import { ResearchSoftware, Development, ManagementSoftware,SoftwareMain } from "./containers/software";
import { ResearchData, Modelling, ManagementData, Analytics,MainData } from "./containers/data";
import { Sport, Trading } from "./containers/solutions";
import { HistoryComp,Customers,Team,Contact,Privacy,Legal,Terms,MainCompany } from "./containers/company";


const Routes = () => (
  <section class="probootstrap-section">
  <Switch>
    <Route
      exact
      path="/"
      // tslint:disable-next-line:jsx-no-lambda
      render={(routeProps: RouteProps) => (
        <Home {...routeProps} user="Default User" />
      )}
    />
    <Route path="/about" component={About} />
    <Route path="/software" component={SoftwareMain} />
    <Route path="/software/research" component={ResearchSoftware} />
    <Route path="/software/development" component={Development} />
    <Route path="/software/management" component={ManagementSoftware} />
    <Route path="/data" component={MainData} />
    <Route path="/data/research" component={ResearchData} />
    <Route path="/data/modelling" component={Modelling} />
    <Route path="/data/management" component={ManagementData} />
    <Route path="/data/analytics" component={Analytics} />
    <Route path="/solutions/sports" component={Sport} />
    <Route path="/solution/trading" component={Trading} />
    
    <Route path="/company" component={MainCompany} />
    <Route path="/company/history" component={HistoryComp} />
    <Route path="/company/customers" component={Customers} />
    <Route path="/company/team" component={Team} />
    <Route path="/company/contact" component={Contact} />
    <Route path="/company/privacy" component={Privacy} />
    <Route path="/company/legal" component={Legal} />
    <Route path="/company/terms" component={Terms} />
<Route path="/solutions" component={Trading} />
    
  </Switch>
  </section>
);

export default Routes;
