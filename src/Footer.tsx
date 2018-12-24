// <reference path='./index.d.ts'/>

import React from "react";

import Routes from "./Routes";
import {IntlProvider, FormattedMessage} from 'react-intl';
// tslint:disable-next-line:no-var-requires

const Footer = () => (
<footer class="container">
          <p class="float-right"></p>
          <hr/>
          <p>&copy; 2019 Buisson Diaz Conseil, Inc. &middot; <a href="#/company/privacy">Privacy</a> &middot; <a href="#/company/terms">Terms</a> &middot; <a href="#/company/legal">Legal Information</a> &middot; <a href="http://www.buissondiaz.com/cgv_service.pdf">CGV</a>  </p>
        </footer>
    
    
  );

export default Footer;