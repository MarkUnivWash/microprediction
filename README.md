
# microprediction [MontePrediction](https://github.com/microprediction/monteprediction_colab_examples/blob/main/monteprediction_entry.ipynb) game

Here's a new game where you hurl a million 11-dimensional Monte Carlo samples at my server. If you'd like to participate:

1. Open this [colab notebook](https://github.com/microprediction/monteprediction_colab_examples/blob/main/monteprediction_entry.ipynb),
2. Change the email, at minimum,
3. Run it.

The notebook also describes the scoring mechanism. If on the other hand you seek my:

  - [papers, articles etc](https://github.com/microprediction/home)
  - Medium [blog](https://microprediction.medium.com/)

that's nice too. 

If we don't know each other yet from [LI](https://www.linkedin.com/in/petercotton/) or elsewhere, I'm an applied mathematician / practitioner but I like to provoke people into using market-inspired collective mechanisms for prediction. I used the options market to effortlessly beat 97% of participants in the year-long M6 contest - see the [post](https://www.linkedin.com/posts/petercotton_the-options-market-beat-94-of-participants-activity-7020917422085795840-Pox0?utm_source=share&utm_medium=member_desktop) or [article](https://medium.com/geekculture/the-options-market-beat-94-of-participants-in-the-m6-financial-forecasting-contest-fa4f47f57d33). My [book](https://mitpress.mit.edu/books/microprediction) is a meditation on the power of markets in a very specific but surprisingly ubiquitous domain: frequently repeated prediction. Read the [awards and reviews](https://microprediction.github.io/building_an_open_ai_network/feedback.html).   

![](https://github.com/microprediction/microprediction/blob/master/docs/assets/images/cotton_microprediction_3d_down.png)


### My benchmarking packages: [TimeMachines](https://github.com/microprediction/timemachines), [Precise](https://github.com/microprediction/precise), and [HumpDay](https://github.com/microprediction/humpday)  


| Topic                  | Package           | Elo ratings | Methods                                                                                                                                                                                  | Data sources | 
|------------------------|-------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------| 
| Univariate time-series | [timemachines](https://github.com/microprediction/timemachines)  | [Timeseries Elo ratings](https://microprediction.github.io/timeseries-elo-ratings/html_leaderboards/univariate-k_003.html) | Most popular packages ([list](https://github.com/microprediction/timemachines/tree/main/timemachines/skaters))                                                                           | [microprediction streams](https://www.microprediction.org/browse_streams.html)                                      |
| Global derivative-free optimization | [humpday](https://github.com/microprediction/humpday) |  [Optimizer Elo ratings](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html) | Most popular packages ([list](https://github.com/microprediction/humpday/tree/main/humpday/optimizers))                                                                                  | A mix of classic and new [objectives](https://github.com/microprediction/humpday/tree/main/humpday/objectives)      |
| Covariance, precision, correlation | [precise](https://github.com/microprediction/precise) | See [notebooks](https://github.com/microprediction/precise/tree/main/examples_colab_notebooks) | [cov](https://github.com/microprediction/precise/blob/main/LISTING_OF_COV_SKATERS.md) and [portfolio](https://github.com/microprediction/precise/blob/main/LISTING_OF_MANAGERS.md) lists |Stocks, electricity etc                                                                                              | 

These packages aspire to advance online autonomous prediction in a small way, but also help me notice if anyone else does.  

## Winning

The [winning](https://github.com/microprediction/winning) package includes my recently published fast algorithm for inferring relative ability from win probabilities, at any scale.  

![](https://i.imgur.com/83iFzel.png) 

## First Down

- [firstdown](https://github.com/microprediction/firstdown) - The repo that aspires to ruin the great game of football. See Wilmott [paper](https://github.com/microprediction/firstdown/blob/main/wilmott_paper/44-49_Cotton_PDF5_Jan22%20(2).pdf).

  ![](https://github.com/microprediction/firstdown/blob/main/images/firstdownpaper.png)

## Some other repos

- [embarrassingly](https://github.com/microprediction/embarrassingly) - A speculative approach to robust optimization that sends impure objective functions to optimizers.
- [pandemic](https://github.com/microprediction/pandemic) - Ornstein-Uhlenbeck epidemic simulation (related [paper](https://arxiv.org/abs/2005.10311))

  
## The currently defunct real-time time-series platform

The real-time system previously maintained by yours truly has entered a trisoloran dehydrated state but will hopefully be revived at a future date, after one of my three hundred ChatGPT generated scientific grant proposals is successful. Here's how some of the open-source stuff used to propagate down into the "algo fight club". 

1. The "[/skaters](https://github.com/microprediction/timemachines/tree/main/timemachines/skaters)" provide canonical, single-line of code access to functionality drawn from packages like [river](https://github.com/online-ml/river), [pydlm](https://github.com/wwrechard/pydlm), [tbats](https://github.com/intive-DataScience/tbats), [pmdarima](http://alkaline-ml.com/pmdarima/), [statsmodels.tsa](https://www.statsmodels.org/stable/tsa.html), [neuralprophet](https://neuralprophet.com/), Facebook [Prophet](https://facebook.github.io/prophet/), 
   Uber's [orbit](https://eng.uber.com/orbit/), Facebook's [greykite](https://engineering.linkedin.com/blog/2021/greykite--a-flexible--intuitive--and-fast-forecasting-library) and more. 
   
2. The [StreamSkater](https://microprediction.github.io/microprediction/predict-using-python-streamskater.html) makes it easy to use any "skater". 

3. Choices are sometimes advised by [Elo ratings](https://microprediction.github.io/timeseries-elo-ratings/html_leaderboards/special-k_003.html), but anyone can do what they want. 

4. It's not too hard to use my [HumpDay](https://github.com/microprediction/humpday) package for offline meta-param tweaking, et cetera. 

5. It's not too hard to use my [precise](https://github.com/microprediction/precise) package for online ensembling. 

Those repose are: 

- The [muid](https://github.com/microprediction/muid) identifier package is explained in this [video](https://vimeo.com/397352413). 
- [microconventions](https://github.com/microprediction/microconventions) captures things common to client and server, and may answer many of your more specific questions about prediction horizons, et cetera.  
- [rediz](https://github.com/microprediction/rediz) contains server side code. For the brave. 
- There are other rats and mice like [getjson](https://github.com/microprediction/getjson), [runthis](https://github.com/microprediction/runthis) and [momentum](https://github.com/microprediction/momentum).  



