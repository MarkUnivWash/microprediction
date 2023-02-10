## Examples of scheduled copula submissions


While a continuous process might be more suited to submission of rapidly changing
data, a scheduled job may work just fine. Furthermore, many streams are implied 
copulas that don't change too often. 

### What are z-streams? 

See [An Introduction to Z-Streams](https://www.linkedin.com/pulse/short-introduction-z-streams-peter-cotton-phd/) or the
microprediction [frequently asked questions](https://www.microprediction.com/faq). Put simply, some of the
seemingly univariate time series such as [this one](https://www.microprediction.org/stream_dashboard.html?stream=z2~copula_x~copula_y~70) are
really multi-variate implied copulas. You can retrieve them in multivariate
format using the .get_lagged_copulas or .get_lagged_zvalues methods of the [MicroReader](https://github.com/microprediction/microprediction/blob/master/microprediction/reader.py). 


### Copula estimators

See 
[Comble Mammal](https://github.com/microprediction/microprediction/tree/master/submission_examples_copulas) for 
an example of periodically fitting a Copula model to historical three-dimensional vectors extracted
from z3~ streams. 


### See also 

[Knowledge Center](https://www.microprediction.com/knowledge-center)
