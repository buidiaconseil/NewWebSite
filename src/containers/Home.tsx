import React from "react";

interface Homeprops {
  user: string;
}

const Home = (props: Homeprops) => (
  <div id="carouselExampleControls" className="carousel slide" data-ride="carousel">
  <div className="carousel-inner">
    <div className="carousel-item active">
      <img src="https://sebadiaz.github.io/ricito/siteweb/img/background.png" className="d-block w-100" alt="..."/>
      <div className="container">
                <div className="carousel-caption text-left">
                  <h1 >Data Analytics and Modeling.</h1>
                  <p >We are a full-service technology, data, and innovation partner who creates innovatives solutions for resolving problems around the globe. </p>
                  <p><a className="btn btn-lg btn-primary" href="data.html" role="button">Learn more</a></p>
                </div>
              </div>
    </div>
    <div className="carousel-item">
      <img src="https://sebadiaz.github.io/ricito/siteweb/img/back3.jpg" className="d-block w-100" alt="..."/>
      <div className="container">
                <div className="carousel-caption text-right">
                  <h1 >The Sport Analitycs Prospective.</h1>
                  <p >We offer some Software Solutions, all your Sport Analytics managed on a performent platform.</p>
                  <p><a className="btn btn-lg btn-primary" href="sport.html" role="button">Learn more</a></p>
                </div>
              </div>
    </div>
    <div className="carousel-item">
      <img src="https://sebadiaz.github.io/ricito/siteweb/img/back2.jpg" className="d-block w-100" alt="..."/>
      <div className="container">
                <div className="carousel-caption">
                  <h1 >Software and Data Intelligence.</h1>
                  <p >We are an Innovative Technology Leader.
                    Expert in Development, Data Science and Cloud solutions, we focus our energy to build your solution in the respect of delay and budget.</p>
                  <p><a className="btn btn-lg btn-primary" href="software.html" role="button">Learn more</a></p>
                </div>
              </div>
    </div>
    <div className="carousel-item">
      <img src="https://sebadiaz.github.io/ricito/siteweb/img/back4.jpg" className="d-block w-100" alt="..."/>
      <div className="container">
                <div className="carousel-caption">
                  <h1 >Streaming Solutions.</h1>
                  
                  <p><a className="btn btn-lg btn-primary" href="software.html" role="button">Learn more</a></p>
                </div>
              </div>
    </div>
  </div>

  <a className="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span className="carousel-control-prev-icon" aria-hidden="true"/>
    <span className="sr-only">Previous</span>
  </a>
  <a className="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span className="carousel-control-next-icon" aria-hidden="true"/>
    <span className="sr-only">Next</span>
  </a>
</div>
);

export default Home;
