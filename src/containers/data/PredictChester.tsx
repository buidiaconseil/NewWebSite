import * as React from "react";

export default class Hello extends React.Component<HelloProps, {}> {
  render() {
    return (
      <div>
        <h2>Predict violent crime for 2013 at chester city , PA</h2>
        <p className="lead text-left">
          This is a study of crime prediction at chester city, PA. Prediction is
          an hard task. With a low data content the must is to use an
          exponential method to predict the violent crimes rate. For 2013 , the
          violent crimes should decrease lowly . It is a tendency.
          <p>
            Predicted crimes value by 100k hab are
            <table border="1">
              <thead>
                <tr>
                  <td />
                  <td>Real value </td>
                  <td>Predict for 2013</td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Violent crime</td>
                  <td>3174</td>
                  <td>3165.4</td>
                </tr>
                <tr>
                  <td>Murder and nonnegligent manslaughter</td>
                  <td>64</td>
                  <td>64.2</td>
                </tr>
                <tr>
                  <td>Forcible rape</td>
                  <td>50</td>
                  <td>51.7</td>
                </tr>
                <tr>
                  <td>Robbery</td>
                  <td>637</td>
                  <td>635</td>
                </tr>
                <tr>
                  <td>Aggravated assault</td>
                  <td>2423</td>
                  <td>2414</td>
                </tr>
              </tbody>
            </table>
          </p>
          <p>
            <img src="https://2.bp.blogspot.com/-_8Tugq0vrc8/UO1BXiiQR0I/AAAAAAAAA9M/yVKnjf1hgWA/s640/a167r001_html_3c3a8c65.png" />
          </p>
        </p>
      </div>
    );
  }
}
