import React from "react";
import * as tf from "@tensorflow/tfjs";
const axios = require("axios");
import * as Papa from "papaparse";
import { RandomForestClassifier } from "machinelearn/ensemble";
import { SGDClassifier } from "machinelearn/linear_model";
import { KNeighborsClassifier } from "machinelearn/neighbors";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";
import { AreaChart, Area } from "recharts";

export default class Trading extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      datasup: []
    };
    this.componentDidMount = this.componentDidMount.bind(this);
    this.load = this.load.bind(this);
  }
  componentDidMount() {
    this.load();
  }
  load() {
    let currentComponent = this;
    axios
      .get("indicators-ETH-BTC.csv", {
        headers: {
          responseType: "arraybuffer"
        }
      })
      .then(function(response) {
        console.log(response);
        console.log(typeof response.data);
        var data = Papa.parse(response.data, {
          dynamicTyping: true
        });
        console.log(data);
        console.log(data.data.length);
        var datasup = [];
        for (var i = 0; i < data.data.length; i++) {
          var line = data.data[i];

          datasup.push({ short: line[0], long: line[1], open: line[2], high: line[3], low: line[4] });
        }
        currentComponent.setState({ datasup });
        console.log(datasup);
      });
  }

  render() {
    return (
      <div>
        <h2>About Page</h2>
        <AreaChart
          width={730}
          height={250}
          data={this.state.datasup}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          
          <XAxis dataKey="name" />
          <YAxis />
          <CartesianGrid strokeDasharray="3 3" />
          <Tooltip />
          <Area
            type="monotone"
            dataKey="open"
            stroke="#ffffff"
            fillOpacity={1}
            fill="url(#colorUv)"
          />
         
        </AreaChart>
      </div>
    );
  }
}
