
import * as React from "react";
import { Route, RouteProps, Switch, Redirect } from "react-router-dom";

import HistoryComp from './History'
import Customers from './Customers'
import Team from './Team'
import Contact from './Contact'
import Privacy from './Privacy'
import Legal from './Legal'
import Terms from './Terms'




export default class Hello extends React.Component<HelloProps, {}> {
    render() {
        return (
        

<div class="container-fluid ">
<hr></hr>
  <div class="row">
    <div class="col-2"><div class="btn-group-vertical btn-group-sm">

    
    <a href="#/company/history" type="button" class="btn btn-secondary">History</a>
    <a href="#/company/team" type="button" class="btn btn-secondary">Team</a>
    <a href="#/company/customers" type="button" class="btn btn-secondary">Customers</a>
    
    
    <a href="#/company/privacy" type="button" class="btn btn-secondary">Privacy</a>
    <a href="#/company/legal" type="button" class="btn btn-secondary">Legal</a>
    <a href="#/company/terms" type="button" class="btn btn-secondary">Terms</a>
    <a href="#/company/contact" type="button" class="btn btn-secondary">Contact</a>

</div></div>
    <div class="col-8"><Switch>
    
    <Route path="/company/history" component={HistoryComp} />
    <Route path="/company/customers" component={Customers} />
    <Route path="/company/team" component={Team} />
    <Route path="/company/contact" component={Contact} />
    <Route path="/company/privacy" component={Privacy} />
    <Route path="/company/legal" component={Legal} />
    <Route path="/company/terms" component={Terms} />
    <Redirect from="/company" exact to="/company/history" />
        </Switch></div>
    <div class="col-2"></div>
  </div>


 </div>

);
}
}