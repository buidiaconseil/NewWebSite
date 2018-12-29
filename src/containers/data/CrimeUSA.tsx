
import * as React from "react";

export default class Hello extends React.Component<HelloProps, {}> {
    render() {
        return (
        
<div>
 <h2 >
 Images of violent crimes by state in USA</h2>
 <p className="lead text-left">
 
The first image propose the max county value of the state

The second image is the mean value of the violent crime of the counties
 
<p>

    <img src="https://4.bp.blogspot.com/-FNzIoI43ymE/UOCGMARERSI/AAAAAAAAA6w/181AUHDd9fM/s640/maxviolent.png" />
    <img src="https://1.bp.blogspot.com/-4aMytD41GQY/UOCGNIMjhCI/AAAAAAAAA64/F5ggaVYWwKY/s640/meanviolent.png" />
  </p>

  </p>
 </div>

);
}
}