import React from "react";
import {encode, decode} from "messagepack";
const axios = require('axios');



axios.get('indicators-ETH-BTC.mpk',{
                                                                                                           headers: {
                                                                                                                responseType: 'arraybuffer'
                                                                                                           }
                                                                                                       })
  .then(function (response) {
    // handle success
    console.log(response);
    console.log(typeof(response.data));
    var buf = new ArrayBuffer(response.data.length*2); // 2 bytes for each char
      var bufView = new Uint8Array(buf);
      for (var i=0, strLen=response.data.length; i < strLen; i++) {
        bufView[i] = response.data.charCodeAt(i);
      }
      console.log(buf);
    const decodedData = decode(buf);
    console.log(decodedData);
  })



const Development = () => (
  <div>
    <h2>About Page</h2>

  </div>
);

export default Development;
