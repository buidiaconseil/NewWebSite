// <reference path='./index.d.ts'/>

import React from "react";

import Routes from "./Routes";
import { IntlProvider, FormattedMessage } from "react-intl";
// tslint:disable-next-line:no-var-requires

const NavBar = () => (
  <header>
    <div class="container">
      <div class="row">
        <div class="col">
          <a href="index.html" class="probootstrap-logo">
            Buisson Diaz Conseil
          </a>

          <div class="mobile-menu-overlay" />

          <nav role="navigation" class="probootstrap-nav hidden-xs">
            <ul class="probootstrap-main-nav">
              <li class="active">
                <a href="index.html">Home</a>
              </li>
              <li>
                <a href="#/software">Software</a>
              </li>
              <li>
                <a href="#/data">Data</a>
              </li>
              <li>
                <a href="#/solutions">Solutions</a>
              </li>
              <li>
                <a href="#/company">About</a>
              </li>
              <li>
                <a href="#/company/contact">Contact</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </header>
);

export default NavBar;
