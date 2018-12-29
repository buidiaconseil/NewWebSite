
import * as React from "react";

export default class Hello extends React.Component<HelloProps, {}> {
    render() {
        return (
        
<div>
 <h2 >Capacitor Mounting Surface</h2>
 <p className="lead text-left">
 <h3>
 Introduction
 </h3>
 <p>
   
Choose the type of capacitor that has the longest life.

· Estimate the average service life of the mounting surface capacitor under normal operating conditions:
<ul>
<li>Tension : 50 Volts</li>

<li>Température : 50° Celsus</li>
</ul>
 </p>

 <h3>
 Evaluation method of the average life of the capacitor mounting surface.
 </h3>
<p>
Reliability is expensive. But the cost of poor quality and reliability is even more expensive. Reliability must be supported throughout the life cycle of the product. Predicting reliability is very important for electronic components such as capacitors, diodes and resistors.
</p><p>
To estimate this average lifetime of the surface-mount capacitor, a specific method of acceleration of lifetime is set up. Indeed the capacitors have a life of several years, making their tests very long. Generally the acceleration of the life tests are done by accelerating the failure of the product by the addition of sustained stress.
</p><p>
As part of this study, two non-controllable parameters are used: temperature and voltage. By stressing these two parameters, the life of the capacitor will be much less with reasonable failure times, and will allow an estimate of the service life under average conditions of use.
</p><p>
The value measured in these tests is the MTTF (Mean Time To Failure) which represents the average time of failure.

</p>
<h3>

Description of the model and the parameters of the study

</h3>

<p>
  
The parameters of the study are:
<ul>
  <li>
    
Y : Average operating time to failure (in h)
  </li>
<li>
2 Production factors (controllable factors):
  <ul>
    <li>A: The type of dielectric (composition of the dielectric). 2 levels A1 and A2.</li>
    <li>B: 
Operating temperature of the production process. 2 levels B1 and B2.</li>
  </ul>
</li>
<li>

2 Environmental factors (non-controllable factors):
  <ul>
    <li>
    C: Voltage (operating factors). 4 levels C1 = 200V, C2 = 250V, C3 = 300V and C4 = 350V.</li>
    <li>D: 

    Ambient temperature (environmental factor): 2 levels D1 = 175 ° C and D2 = 190 ° C.</li>
  </ul>
</li>
</ul>
</p>
<p>
  
The mathematical model for the factors of production is the following one taking into account only the links of the second order for the factors A and B:


We use the Taguchi method where we minimize the dispersion of product performance in response to noise factors while maximizing dispersion in response to signal factors.

S / B ratios can be calculated using Taguchi's robust plan options.

There are three ratios:
<ul>
    <li>
"Larger is better" to maximize the answer: S / N = -10 * log (Σ (1 / Y2) / n)
      </li>
      <li>
        
"Smaller is better" to minimize the response: S / N = -10 * log (Σ (Y2) / n)
      </li>
      <li>
        
"Nominal is best" based on mean and standard deviation
      </li>
      </ul>
</p>


  <h2>
    
Choice of factorial plans
  </h2>
  <h3>
    
Production factors plan
  </h3>
  <p>

  L4 full factorial design plan for production factors:
  <table border={1}>
<thead><tr><td>Dielectric</td><td>
Production temperature</td><td>Durée de vie</td></tr></thead>
<tbody>
  <tr><td>1</td><td>1</td><td></td></tr>
  <tr><td>1</td><td>2</td><td></td></tr>
  <tr><td>2</td><td>1</td><td></td></tr>
  <tr><td>2</td><td>2</td><td></td></tr>
</tbody>

  </table>
  
The model on the factors of production is the following


The model has 4 levels of freedom. With AB factor, the LCP is 4.

For orthogonality, the number of tests of the plane must be multiple of k (4).

And to respect the number of degrees of freedom, the number of tests must be at least 4.
  </p>
  <h3>
Experience Plan for Environmental Factors</h3>
<p>
  
Full L8 Factorial Experiment Plan for Environmental Factors:

We begin by changing the Tension factor to 4 levels by two factors at two levels:

<table><tbody><tr><td>
<table border={1}>
<thead><tr><td>Tension (V)</td></tr></thead>
<tbody>
  <tr><td>200</td></tr>
  <tr><td>250</td></tr>
  <tr><td>300</td></tr>
  <tr><td>350</td></tr>
  </tbody>
</table>
  </td><td>
  <table border={1}>
<thead><tr><td>Tension 1</td><td>Tension 2</td></tr></thead>
<tbody>
  <tr><td>1</td><td>1</td></tr>
  <tr><td>1</td><td>2</td></tr>
  <tr><td>2</td><td>1</td></tr>
  <tr><td>2</td><td>1</td></tr>
  </tbody>
</table>
    
    </td></tr></tbody></table>
</p>
<p>
  
The final experience plan is:
<table border={1}>
<thead><tr><td>Tension 1</td><td>Tension 2</td><td>Température</td><td>Lifetime</td></tr></thead>
<tbody>
  <tr><td>1</td><td>1</td><td>175</td><td></td></tr>
  <tr><td>1</td><td>1</td><td>190</td><td></td></tr>
  <tr><td>1</td><td>2</td><td>175</td><td></td></tr>
  <tr><td>1</td><td>2</td><td>190</td><td></td></tr>
  <tr><td>2</td><td>1</td><td>175</td><td></td></tr>
  <tr><td>2</td><td>1</td><td>190</td><td></td></tr>
  <tr><td>2</td><td>2</td><td>175</td><td></td></tr>
  <tr><td>2</td><td>2</td><td>190</td><td></td></tr>
  </tbody>
</table>

Postulated Model:


For orthogonality, the number of tests of the plane must be multiple of k (8).

And to respect the number of degrees of freedom, the number of tests must be at least 8.
</p>
<h3>
Complete Factorial Plan with results</h3>
<p>

L4 + L8 Full Experience Plan Data
<table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" >
 <tbody>
<tr >
  <td rowspan="2"  valign="top"></td>
  <td ><div align="center" class="MsoNormal" >
<span>Tension</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>3</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>3</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>4</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>4</span></div>
</td>
  <td colspan="2" rowspan="2"  valign="top"></td>
  <td colspan="2" rowspan="2" ><div align="center" class="MsoNormal" >
<span>Signal / Bruit</span><span></span></div>
</td>
 </tr>
<tr >
  <td ><div align="center" class="MsoNormal" >
<span>Température&nbsp; de fonction</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
 </tr>
<tr >
  <td ><div align="center" class="MsoNormal" >
<span>Diélectrique</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>Température de production</span></div>
</td>
  <td colspan="8" ></td>
  <td ><div align="center" class="MsoNormal" >
<span>Moyenne</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>Ecart type</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>Maximisation</span></div>
</td>
  <td ><div align="center" class="MsoNormal" >
<span>Valeur cible</span></div>
</td>
 </tr>
<tr >
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>430</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>950</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>560</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>210</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>310</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>230</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>250</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>230</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>396,25</span></div>
</td>
  <td  valign="top"><div >
<span >2545</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>49,2</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>3,85</span></div>
</td>
 </tr>
<tr >
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1080</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1060</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>890</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>450</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>430</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>320</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>340</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>430</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>625</span></div>
</td>
  <td  valign="top"><div class="MsoNormal" >
<span >326,8</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>53,3</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>5,63</span></div>
</td>
 </tr>
<tr >
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>1</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>890</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1060</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>680</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>310</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>310</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>310</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>250</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>230</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>505</span></div>
</td>
  <td  valign="top"><div class="MsoNormal" >
<span >325,5</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>50,5</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>3,8</span></div>
</td>
 </tr>
<tr >
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td  valign="top"><div align="center" class="MsoNormal" >
<span>2</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1100</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1080</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>1080</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>460</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>620</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>370</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>580</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>430</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>715</span></div>
</td>
  <td  valign="top"><div>
<span >317,8</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>54,96</span></div>
</td>
  <td  valign="top"><div align="right" class="MsoNormal" >
<span>7,04</span></div>
</td>
 </tr>
</tbody></table>


</p>
<h2>
Analysis of the reliability of the factors of production</h2>
<h3>Model</h3>
<p>

Experience results for factors of production
We take into account the average life span per group of factors, without considering the environmental factors directly.
<table border={1}>
<thead><tr><td>Dielectric</td><td>
Production temperature</td><td>Durée de vie</td></tr></thead>
<tbody>
  <tr><td>1</td><td>1</td><td>396,25</td></tr>
  <tr><td>1</td><td>2</td><td>625</td></tr>
  <tr><td>2</td><td>1</td><td>505</td></tr>
  <tr><td>2</td><td>2</td><td>715</td></tr>
</tbody>

  </table>
</p>
<h3>Analysis of the variance</h3>
<p>
  
To verify the conditions necessary for an analysis of variance, we must check the independence of the samples, the normality of the distribution and the homogeneity of the variances.
</p>
<h4>
  
Normality of distribution
</h4>
<p>
  
To test the normality of the distribution, we use a Shapiro-Wilk test.
Statistic : 0.984044, Probability: 	0,900591  .

The probability of the test performed is greater than 5%, we can not reject the idea that the service life follows a normal distribution at the 95% level of confidence.





The normality graph confirms the Gaussian distribution.
<img src="https://1.bp.blogspot.com/-MtjLFnyRKUU/VTJXSC5hpiI/AAAAAAAAJZA/eNI3H5qMcw4/s1600/1.png"></img>
</p>
<h4>
Independence of samples</h4>
<p>
  
The plot of residuals by number of observations makes it possible to highlight the independence of the samples.
<img src="https://2.bp.blogspot.com/-VowcIZNLqYI/VTJXc1FoGjI/AAAAAAAAJZI/zCu-OZJgFJc/s1600/2.png"></img>
</p>
<h4>
Homogeneity of Variances</h4>
<p>
  
The plot of Residues by Production Temperature and Dielectric allows to conclude a homogeneous variance. The two graphs show residual variances of the same level.
<img src="https://2.bp.blogspot.com/-NPOSobo79ow/VTJXtLEs1JI/AAAAAAAAJZU/aFBW_JuN66A/s1600/3.png"></img>
<img src="https://4.bp.blogspot.com/-SxWIvYagDtE/VTJXtBIr-AI/AAAAAAAAJZQ/qF7Z7LXEHVo/s1600/4.png"/>
</p>
<h4>
Analysis of the ANOVA</h4>
<p>
  
Analysis with second order interactions.
</p>
<p>
<img src="https://3.bp.blogspot.com/-s2nRjPEYkFk/VTJX5GJkvSI/AAAAAAAAJZg/YMkI7Mw-os4/s1600/5.png"></img>
</p>
<p>
The Pareto graph shows that the AB interaction is negligible.

As part of the study, we will not consider this interaction.

Analysis without AB interaction
</p>
<p>
<img src="https://2.bp.blogspot.com/-ro0rRbVOcAc/VTJYDrIdbfI/AAAAAAAAJZo/Occ2bGkYuHY/s1600/6.png" />


</p>
<p>
  
By eliminating the AB interaction, we can evaluate the quality of each factor in the model.

The results are as follows:
<table border={1}>
<thead><tr><td>Source</td><td>
Production 
Sum of squares</td>
<td>DDL</td>
<td>
Mean quadratic</td>
<td>Report F</td>
<td>Proba.</td>
</tr></thead>
<tbody>
  <tr><td>A:Dielectrique</td><td>9875,39</td><td>1</td><td>9875,39</td><td>112,36</td><td>0,0599</td></tr>
  <tr><td>B:Température Production</td><td>48125,4</td><td>1</td><td>48125,4</td><td>547,56</td><td>0,0272</td></tr>
  <tr><td>Total Error</td><td>87,8906</td><td>1</td><td>87,8906</td><td></td><td></td></tr>
  <tr><td>Total (corr.)</td><td>58088,7</td><td>3</td><td></td><td></td><td></td></tr>
  
</tbody>

  </table>
  
The effect of the production temperature has a probability of less than 5% which indicates that it is significantly different from zero and has a decisive effect at the 95% confidence level.
<img src="https://3.bp.blogspot.com/-P_NChiP70SU/VTJYNtGuIFI/AAAAAAAAJZw/I76DhUEQFIs/s1600/7.png"></img>
</p>
<p>
The effects graph highlights the effect of each of the factors. It highlights and corroborates the analysis of the variance on the strong effect of the production temperature in the model. The effect of the dielectric is less important and can be neglected.

The model adjusted with the dielectric factor is as follows:
CONSTANT:560,313 , Diélectrique:49,6875 , Température Production:109,688.
The equation of the adjusted model is:
Durée de vie = 560,313 + 49,6875*Diélectrique + 109,688*Température de Production .

The best combination that achieves the longest life is a dielectric factor of type 2 and a production temperature factor of level 2. This brings us to an estimated lifetime of 879.064 hours.

The adjusted model without the dielectric factor is as follows: Durée de vie = 231,25 + 219,375*Température de Production.


The best combination that achieves the longest life is a production temperature factor of 2. This brings us to an estimated life of 670 hours.

</p>
<h2>
Environmental factors analysis</h2>
<h3>
Signal / Noise Analysis</h3>
<h4>
Results of experimentation</h4>
<p>
<table border={1}>
<thead><tr><td>Dielectric</td><td>
Production temperature</td><td>
S / B The biggest of the best</td>
<td>
S / B Target value</td>
</tr></thead>
<tbody>
  <tr><td>1</td><td>1</td><td>49,2</td><td>3,85</td></tr>
  <tr><td>1</td><td>2</td><td>53,3</td><td>5,63</td></tr>
  <tr><td>2</td><td>1</td><td>50,5</td><td>3,8</td></tr>
  <tr><td>2</td><td>2</td><td>54,96</td><td>7,04</td></tr>
</tbody>

  </table>
  We choose "the greatest the best" and the target value:

· For one hand to know the best combination acting on the service life.

· And on the other hand, identify combinations that offer greater resistance to environmental factors.
<img src="https://2.bp.blogspot.com/-fa8CMOw17iY/VTJYksAuGGI/AAAAAAAAJZ8/iG7aVhuPRbE/s1600/8.png"></img>
<img src="https://3.bp.blogspot.com/-rnLpEjdctzU/VTJYkoymHWI/AAAAAAAAJZ4/yw8gLxsk5tY/s1600/9.png" />
</p>
<p>
The analysis of the values ​​and graphs of the effects makes it possible to choose the best combination respecting the instructions of robustness. Thus, the choice of the type 2 production temperature and the type 2 dielectric appears again as the best compromise.
</p>
<h3>Study of noise factors</h3>
<p>
  <img src="https://2.bp.blogspot.com/-jcBdyuQhjKU/VTJYyicW-qI/AAAAAAAAJaI/548pHVfKAXI/s1600/10.png"/>
  <img src="https://4.bp.blogspot.com/-kSk6IbaTS_s/VTJYy3UXHyI/AAAAAAAAJaM/_Vm3k3e6CMk/s1600/11.png" />
  </p>
<p> Voltage has a preponderant effect on the effect of noise in our model.

The temperature factor of the environment is negligible in view of the Pareto graph. This is confirmed by the effects graph. The following variance analysis can also be checked:
<table border={1}>
<thead><tr><td>Source</td><td>
Sum of squares</td>
<td>DDL</td>
<td>
Mean quadratic</td>
<td>Report F</td>
<td>Proba.</td>
</tr></thead>
<tbody>
  <tr><td>A:Tension 1</td><td>1,38195E6</td><td>1</td><td>1,38195E6</td><td>29,07</td><td>0,0000</td></tr>
  <tr><td>B:Tension 2</td><td>314028</td><td>1</td><td>314028</td><td>6,61</td><td>0,0158</td></tr>
  <tr><td>C:Temperature Environnement</td><td>87153,1</td><td>1</td><td>87153,1</td><td>1,83</td><td>0,1866</td></tr>
  <tr><td>Total Error</td><td>1,33116E6</td><td>28</td><td>47541,5</td><td></td><td></td></tr>
  <tr><td>Total (corr.)</td><td>3,1143E6</td><td>31</td><td></td><td></td><td></td></tr>
  
</tbody>

  </table>
</p>
<h2>
Estimated life expectancy under normal conditions</h2>
<p>
  
The data used is taken from the previous choice which is the Dielectric factor at Level 2 and the Production temperature factor at level 2.
<table border={1}>
<thead><tr><td>Tension</td><td>
Temperature</td><td>Lifetime</td></tr></thead>
<tbody>
  <tr><td>200</td><td>175</td><td>1100</td></tr>
  <tr><td>200</td><td>190</td><td>1080</td></tr>
  <tr><td>250</td><td>175</td><td>1080</td></tr>
  <tr><td>250</td><td>190</td><td>460</td></tr>
  <tr><td>300</td><td>175</td><td>620</td></tr>
  <tr><td>300</td><td>190</td><td>370</td></tr>
  <tr><td>350</td><td>175</td><td>580</td></tr>
  <tr><td>350</td><td>190</td><td>430</td></tr>
</tbody>

  </table>
  
We use a survival data regression model with a normal log distribution.

The result of the model estimation is as follows:

Estimated Regression Model - Log-Normal


The model is as follows: Duree Modele = exp(13,1167 - 0,00545509*Tension Env - 0,0281227*Temperature Env)

 .

 For a temperature of 50 ° and a voltage of 50 V, the estimate gives us: 92763 hours

Which corresponds to 10 years of life.

Model graph adjusted to 50V and 50 °
<img src="https://4.bp.blogspot.com/-YXFs3gdMqBY/VTJZBfiWdvI/AAAAAAAAJaY/4_eVr8EL698/s1600/12.png" />

<h2>Conclusion</h2>
<p>
  
The analysis of the results allowed us to highlight the best compromise between the robustness and the longer life of surface response capacitors.

Thus, it emerges from the foregoing elements, the surface capacitor having a type A2 dielectric and a type B2 production temperature.

Based on this choice, we have determined, through a survival data regression model, that the surface response capacitor of this type has an estimated lifetime value of 92763 hours (10.6 years).



Combined with the adjusted model graph, we found that the most robust of this type of surface response capacitor exceeded 130,000 hours (14.8 years).
</p>
</p>
  </p>
 </div>

);
}
}