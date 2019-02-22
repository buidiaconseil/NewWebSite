import React from "react";
import * as tf from '@tensorflow/tfjs';
const axios = require('axios');
import * as Papa from 'papaparse';
import { RandomForestClassifier } from 'machinelearn/ensemble';
import { SGDClassifier } from 'machinelearn/linear_model';
import { KNeighborsClassifier } from 'machinelearn/neighbors';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';
import {
  AreaChart, Area
} from 'recharts';


export default class Trading extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      datasup: []
    };
    this.componentDidMount=this.componentDidMount.bind(this);
    this.load=this.load.bind(this);
  }
  componentDidMount(){
        this.load();
  }
  load() {

    let currentComponent = this;
    axios.get('indicators-ETH-BTC.csv',{
                                                                                                               headers: {
                                                                                                                    responseType: 'arraybuffer'
                                                                                                               }
                                                                                                           }).then(function (response) {
        console.log(response);
            console.log(typeof(response.data));
            var data = Papa.parse(response.data,{
                                               	dynamicTyping: true
                                               });
             console.log(data);
            console.log(data.data.length);
            var datasup=[]
             for (var i=0;i<data.data.length;i++){

                var line=data.data[i];

                datasup.push({short:line[0],long:line[1]});
             }
            currentComponent.setState({datasup})
            console.log(datasup);
      });
  }

  render() {

    return (
<div>
    <h2>About Page</h2>
<AreaChart width={730} height={250} data={this.state.datasup}
  margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
  <defs>
    <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
      <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8}/>
      <stop offset="95%" stopColor="#8884d8" stopOpacity={0}/>
    </linearGradient>
    <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
      <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8}/>
      <stop offset="95%" stopColor="#82ca9d" stopOpacity={0}/>
    </linearGradient>
  </defs>
  <XAxis dataKey="name" />
  <YAxis />
  <CartesianGrid strokeDasharray="3 3" />
  <Tooltip />
  <Area type="monotone" dataKey="short" stroke="#ffffff" fillOpacity={1} fill="url(#colorUv)" />
  <Area type="monotone" dataKey="long" stroke="#82ca9d" fillOpacity={1} fill="url(#colorPv)" />
</AreaChart>
  </div>
    );
  }
}




