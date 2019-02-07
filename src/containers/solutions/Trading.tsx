import React from "react";
import * as tf from '@tensorflow/tfjs';
const axios = require('axios');
import * as Papa from 'papaparse';
import { RandomForestClassifier } from 'machinelearn/ensemble';
import { SGDClassifier } from 'machinelearn/linear_model';
import { KNeighborsClassifier } from 'machinelearn/neighbors';

axios.get('indicators-ETH-BTC.csv')
  .then(function (response) {
    // handle success
    console.log(response);
    console.log(typeof(response.data));
    var data = Papa.parse(response.data,{
                                       	dynamicTyping: true
                                       });
    var x=[];
    var yLong=[];
    var yShort=[];
    var i;
    console.log(data.data.length);
    for (i = 0; i < data.data.length; i++) {
      var col=data.data[i];
      if(col[0]!=null){
      yLong.push(col[0]);
      yShort.push(col[1]);
      var j;
      var dataLine=[];
          for (j = 2; j < col.length; j++) {
               dataLine.push(col[j]);
          }

      x.push(dataLine);
      }
    }
    console.log(x.length);
    console.log(yShort);
    console.log(yLong);
    console.log(x);
    const randomForest = new RandomForestClassifier();
    randomForest.fit(x, yLong);
    console.log(randomForest.toJSON());
    const clf = new SGDClassifier();
    clf.fit(x, yLong);
    console.log(clf.toJSON());
    const knn = new KNeighborsClassifier();
    knn.fit(x, yLong);
    console.log(knn.toJSON());
    const model = tf.sequential();
    model.add(tf.layers.dense({units: 1, inputShape: [151]}));
    model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});
    const xs = tf.tensor2d(x, [29,151]);
    const ys = tf.tensor2d(yLong, [29,1]);
    model.fit(xs, ys, {epochs: 10}).then(() => {
        console.log(JSON.stringify(model.outputs[0].shape));
    });

  })



const Development = () => (
  <div>
    <h2>About Page</h2>

  </div>
);

export default Development;
