
import * as React from "react";

export default class Hello extends React.Component<HelloProps, {}> {
    render() {
        return (
        
<div>
 <h2 >
Spatial modeling</h2>
 <p className="lead text-left">
 <h3>
 
Variogram
 </h3>
 <h4>
Experimental variogram</h4>
 <p>
 
We begin the analysis with variogram analysis.
</p>
<p>
<img src="https://3.bp.blogspot.com/-J9y95Y02Uis/VCSAx2aVulI/AAAAAAAAHBY/mbttet--E7k/s1600/typo6.png"></img>
Plus on s’éloigne du point plus la semi variance est importante. Il y a donc de forte disparité géographique.
</p>
<h4>

Variogram at 0 °, 45 °, 90 ° and 135 °</h4>
 <p>
<img src="https://1.bp.blogspot.com/-1ajcNytqra8/VCSA5KS78tI/AAAAAAAAHBg/QSYEJ-RsOAA/s1600/typo7.png"/>

The variogram at 0 ° is little variant and resembles a nugget effect, compared to the other angles which have a greater tendency to increase the variance over the distant distances.
</p>
<h3>
Using a variogram model</h3>
<p>
  
To use kriging linear modeling, we need a variogram model representative of our data. We use a spherical model to represent our variograms.
<img src="https://1.bp.blogspot.com/-mwJyem27etw/VCSBAu9ak0I/AAAAAAAAHBo/Kc-70fdRgEc/s1600/typo8.png"/>

The model used is quite close to the four angles and seems a good compromise, strongly attenuating some angles and increasing others.
</p>

<h3>
Kriging on a spatial grid</h3>
<p>
  
The result of kriging is as follows:
<img src="https://2.bp.blogspot.com/-70iA6t_te0s/VCSBIMYSZII/AAAAAAAAHBw/jV-2XllIx_0/s1600/typo9.png" />

As seen in the exploratory analysis, we have a vertical axis that breaks down into two distinct parts. The lowest values ​​in this axis and the larger values ​​on the left and right sides. The representation on a grid, shows us clearly the distribution of the variable Y which has two weakly polluted zones in the middle of other very polluted zones.
</p>
<h3>
Prediction error</h3>
<p>
  <img src="https://3.bp.blogspot.com/-ypi7LgbODW8/VCSBPpaHmDI/AAAAAAAAHB4/t8XfDkL-YYc/s1600/typo10.png" />
  
It can be seen that prediction errors are very important to the right and to the left of a vertical axis. The errors are due to the compromise made with our variogram model. On the left and right are strong values ​​close to low values. The linear model, smoothing the values, releases these errors.
</p>
  </p>
 </div>

);
}
}