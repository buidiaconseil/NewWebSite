import React from "react";

const Research = () => (
  <div className="container marketing">
    <hr className="featurette-divider" />

    <div className="row featurette">
      <div className="col-md-7">
        <h2 className="featurette-heading">Contact</h2>
        <h3>Buisson Diaz Conseil.</h3>
        <p className="lead">
          <b>Paris Head Office.</b>
        </p>

        <p className="lead">8 Allée Joseph Récamier</p>

        <p className="lead">75015 Paris - France</p>

        <p className="lead" />

        <p className="lead">Phone: +33 6 15 53 07 20</p>

        <p className="lead">Email : sebastien.diaz[at]buissondiaz.com</p>
      </div>
      <div className="col-md-5">
        <iframe
          width="400"
          height="350"
          frameBorder="0"
          scrolling="no"
          marginHeight="0"
          marginWidth="0"
          src="http://cartosm.eu/map?lon=2.2970654902108&lat=48.835200330486&zoom=18&width=400&height=350&mark=true&nav=false&pan=true&zb=inout&style=default&icon=down"
        />
        <br />
        <div id="cartosmlink">
          <a href="http://www.openstreetmap.org/?mlat=48.835200330486&mlon=2.2970654902108&zoom=18&layers=M">
            See a better Map
          </a>
        </div>
      </div>
    </div>

    <hr className="featurette-divider" />
  </div>
);

export default Research;
