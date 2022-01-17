# **DESCRIPTION**

## Study of the share price of Vale S.A. using time series and the production of pig iron as an exogenous variable
To predict the price of Vale's shares, using pig iron production as an explanatory variable, it was first necessary to predict the values of the independent variable. These values were entered into the database and thus the value of the dependent variable was predicted.

Results of the pig iron prediction model: https://github.com/juliokozarewicz/pig_iron

## Pig iron
The vast majority of pig iron is produced and consumed within integrated steel mill complexes. In this context the term “pig iron” is something of a misnomer: within integrated steel mills, blast furnace iron is transferred directly to the steel plant in liquid form, better known as "hot metal" or "blast furnace iron."

The term “pig iron” dates back to the time when hot metal was cast into ingots before being charged to the steel plant. The moulds were laid out in sand beds such that they could be fed from a common runner. The group of moulds resembled a litter of sucking pigs, the ingots being called “pigs” and the runner the “sow.”

## Merchant pig iron
Merchant pig iron is cold pig iron, cast into ingots and sold to third parties as feedstock for the steel and ferrous casting industries.

Merchant pig iron is produced by

* Dedicated merchant plants - all of whose production is sold to external customers; 
* Integrated steel mills - with iron that is surplus to their internal requirements and cast into ingots and sold to the merchant market.

## Types of merchant pig iron
Merchant pig iron comprises three main types:

* Basic pig iron:
  Used mainly in electric arc steelmaking

* Foundry pig iron (also known as haematite pig iron): 
  Used in mainly in the manufacture of grey iron castings in cupola furnaces

* High purity pig iron (also known as nodular pig iron): 
  used in the manufacture of ductile [also known as nodular or spheroidal graphite – SG] iron castings.

There are also various sub-types, for example low manganese basic pig iron, semi-nodular pig iron etc.

## Composition and characteristics
Pig iron contains at least 92% Fe and has a very high carbon content, typically 3.5 - 4.5%.

## Vale S.A.
Vale S.A. is a Brazilian multinational corporation engaged in metals and mining and one of the largest logistics operators in Brazil. Vale, formerly Companhia Vale do Rio Doce (the Sweet River Valley Company, referring to the Doce River), is the largest producer of iron ore and nickel in the world. Vale also produces manganese, ferroalloys, copper, bauxite, potash, kaolin, and cobalt, currently operating nine hydroelectricity plants, and a large network of railroads, ships, and ports used to transport its products.

Data source: Yahoo finance.

# **RESULTS**
Results obtained through the model estimation process.

## Variable analysis at level:
<img src="4_results/1_time_serie.jpg"> <br /> <br />
<img src="4_results/2_fac_facp_level.jpg"> <br /> <br />
<img src="4_results/3_periodogram_level.jpg"> <br /> <br />
<img src="4_results/4.jpg"> <br /> <br />

## SEASONAL ADJUSTMENT:
<img src="4_results/5_x13_results.jpg"> <br /> <br />
<img src="4_results/6_x13_seasonal_adjustment.jpg"> <br /> <br />

## Study of data stationarity:
<img src="4_results/7.jpg"> <br /> <br />
<img src="4_results/8.jpg"> <br /> <br />


## Model results:
<img src="4_results/9.jpg"> <br /> <br />

## Residual analysis:
<img src="4_results/10_residuals (acf and pacf).jpg"> <br /> <br />
<img src="4_results/11_residuals (frequency distribution).jpg"> <br /> <br />
<img src="4_results/12_residuals (time serie).jpg"> <br /> <br />

# FORECAST:
<img src="4_results/13_observed_fitted_predict.jpg"> <br /> <br />
