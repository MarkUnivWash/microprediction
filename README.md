
# microprediction [![Downloads](https://static.pepy.tech/personalized-badge/microprediction?period=total&units=international_system&left_color=green&right_color=grey&left_text=Downloads)](https://pepy.tech/project/microprediction) ![tests](https://github.com/microprediction/microprediction/workflows/tests/badge.svg) ![deploy](https://github.com/microprediction/microprediction/workflows/deploy/badge.svg)

Looking for [microprediction](https://github.com/microprediction/microprediction/tree/master/microprediction), [m6](https://github.com/microprediction/m6) or 
[timemachines](https://github.com/microprediction/timemachines)? Hi, this is my [dog](https://i.imgur.com/2E3pskp.jpg). This is my [blog](https://www.microprediction.com/blog). I run a slack channel for those interested in open-source time-series prediction ([invite](https://join.slack.com/t/microprediction/shared_invite/zt-10ad1yiec-Jgsjkit~~dwNnpvRzyBTaQ)) and informal Google Meets twice a week announced in the Slack. 

### Microprediction TLDR
Algorithms come to you. 

- You publish live data repeatedly, [like this](https://github.com/microprediction/microprediction/blob/master/stream_examples_traffic/traffic_live.py) say, and it
 creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=electricity-load-nyiso-overall).
- As soon as you do, algorithm "crawlers" like [this guy](https://github.com/microprediction/microprediction/blob/master/crawler_examples/soshed_boa.py) compete to make distributional predictions of
your data feed 1 min ahead, 5 min ahead, 15 min ahead and 1 hr ahead. 

In this way you can:
 - Get live prediction of public data for free (yes it really is an [api](http://api.microprediction.org/) that predicts anything!)
 - See which R, Julia and Python time series approaches seem to work best, saving you from
  trying out [hundreds of packages](https://www.microprediction.com/blog/popular-timeseries-packages) from PyPI and github of uncertain quality. 
  
That's all.


# [Microprediction](https://github.com/microprediction/microprediction/tree/master/microprediction) Python client
If you don't know about the live algorithm frenzy at [microprediction.org](https://www.microprediction.org/) then an extremely simple way to grok it is to open this colab [notebook](https://github.com/microprediction/microprediction/blob/master/submission_examples_die/first_submission.ipynb) and run it on Google's dime. This will create an identity for you and enter your algorithm in an ongoing contest to predict the next roll of a die. The [client](https://github.com/microprediction/microprediction) assists use of the [microprediction api](http://api.microprediction.org/) that enables turnkey, *repeated short term predictions* of anything, for any purpose, for anyone, at any time. The bare-bones API and functionality is:

|   | Task                                      | Method or function                | Full code example                                                                                                                                   | Video tutorial                                                                    |
|---|-------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| A | Create a write_key                        | new_key                           | [enter_die_contest_one_off.py](https://github.com/microprediction/microprediction/blob/master/submission_examples_die/enter_die_contest_one_off.py) | [python-1: Your first submission](https://www.microprediction.com/python-1)       |
| B | Publish one scalar value at a time, usually representing a live measurement.   | MicroWriter.set()                 | [creating_a_stream.py](https://github.com/microprediction/microtutorial/blob/master/examples/creating_a_stream.py)                                  | [python-4: Creating a stream](https://www.microprediction.com/python-4)           |
| C | Send 225 guesses of the next value of a stream, after a fixed quarantine period. | MicroWriter.submit()              | [enter_die_contest_one_off.py](https://github.com/microprediction/microprediction/blob/master/submission_examples_die/enter_die_contest_one_off.py) | [python-2: Creating your first crawler](https://www.microprediction.com/python-2) |
| D | Retrieve community predictions (PDF) 1min, 5min, 15min or 1hr ahead.            | MicroWriter.get_own_predictions() | [defassa_dog.py](https://github.com/microprediction/microprediction/blob/master/submission_examples_golf/defassa_dog.py)                            |                                                                                   |                  |                                                                                   |   |

Someone wanting live information predicted performs A, B and D. Someone providing predictions performs A and C, mindful of the reward mechanism explained in [Collective Distributional Prediction](https://www.microprediction.com/blog/intro).  


# [TimeMachines](https://github.com/microprediction/timemachines) and related packages

The timemachines package provides autonomous time-series prediction algorithms in a simple functional form. They are benchmarked using a subset of the 
[microprediction streams](https://www.microprediction.org/browse_streams.html) and thus, [Elo ratings](https://microprediction.github.io/timeseries-elo-ratings/html_leaderboards/univariate-k_003.html) are published. 
 
 I also maintain a few other repos required for the microprediction platform

- [MUID](https://github.com/microprediction/muid) - Memorable Unique Identifiers used as write keys. The only thing I'll be remembered for. 
- [microconventions](https://github.com/microprediction/microconventions) - common to client and server may answer many of your questions. 
- [rediz](https://github.com/microprediction/rediz) - Server side code, for the brave. 
- [getjson](https://github.com/microprediction/getjson), [momentum](https://github.com/microprediction/momentum) and other rats and mice.  

# [M6](https://github.com/microprediction/m6) and other time-series related packages
If you are chasing the $300,000 in M6 prizes...
- [m6](https://github.com/microprediction/m6) - Some utilities for the M6 Forecasting competition (fast numerical rank probabilities without Monte Carlo) 
- [Winning](https://github.com/microprediction/winning) - A recently published fast algorithm for inferring relative ability from win probability (stable). 
- [HumpDay](https://github.com/microprediction/humpday) - Derivative-free optimizers in canonical form, with [Elo ratings](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html), potentially useful for hyper-parameters.  
- [Embarrassingly](https://github.com/microprediction/embarrassingly) - A speculative approach to robust optimization that sends impure objective functions to optimizers.

Unrelated:

- [Pandemic](https://github.com/microprediction/pandemic) - Ornstein-Uhlenbeck epidemic simulation (related [paper](https://arxiv.org/abs/2005.10311))
- [FirstDown](https://github.com/microprediction/firstdown) - The repo that might ruin the great game of football.  

# Microprediction versus TimeMachines

The [TimeMachines](https://github.com/microprediction/timemachines) package is traditional open-source software for point-estimates and confidence, whereas the [Microprediction](https://github.com/microprediction/microprediction) client offers live crowd based distributional prediction.

Hundreds of algorithms compete at [Microprediction](https://github.com/microprediction/microprediction) and quite a few of the [TimeMachines](https://github.com/microprediction/timemachines) algorithms (see [/skaters](https://github.com/microprediction/timemachines/tree/main/timemachines/skaters)) are involved, drawn from packages like [river](https://github.com/online-ml/river), [pydlm](https://github.com/wwrechard/pydlm), [tbats](https://github.com/intive-DataScience/tbats), [pmdarima](http://alkaline-ml.com/pmdarima/), [statsmodels.tsa](https://www.statsmodels.org/stable/tsa.html), [neuralprophet](https://neuralprophet.com/), Facebook [Prophet](https://facebook.github.io/prophet/), 
   Uber's [orbit](https://eng.uber.com/orbit/), Facebook's [greykite](https://engineering.linkedin.com/blog/2021/greykite--a-flexible--intuitive--and-fast-forecasting-library) and more. Some are open source (look for CODE badges on [leaderboards](https://www.microprediction.org/leaderboard.html)) but others are private to their author.  
 
One bridge between the [/skaters](https://github.com/microprediction/timemachines/tree/main/timemachines/skaters) and the microprediction [leaderboards](https://www.microprediction.org/leaderboard.html) is provided by the StreamSkater class in the microprediction package, illustrated in the [StreamSkater examples](https://github.com/microprediction/microprediction/tree/master/crawler_skater_examples) folder. This makes it trivial to use any skater from the TimeMachines package in a MicroCrawler (a live algorithm). 

## More about the Microprediction Python Client
See also [README_EXAMPLES.md](https://github.com/microprediction/microprediction/blob/master/README_EXAMPLES.md) or 
[README_LONGER.md](https://github.com/microprediction/microprediction/blob/master/README_LONGER.md)

### Class Hierarchy 

Use [MicroReader]((https://github.com/microprediction/microprediction/blob/master/microprediction/reader.py) if you just need to get data and don't care to use a key. Create streams [like this](https://github.com/microprediction/microprediction/blob/master/feed_examples_live/traffic_live.py) using
the [MicroWriter](https://github.com/microprediction/microprediction/blob/master/microprediction/writer.py).   

    MicroReader
       |
    MicroWriter ----------------------------
       |                                   |
    MicroPoll                         MicroCrawler
    (feed creator)               (self-navigating algorithm)
                
### Scheduled submissions versus crawling

| Type                               | Suggestion                                                                                                     | Example                                                                                                                     | More examples                                                                                                                   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Scheduled submission               | [MicroWriter](https://github.com/microprediction/microprediction/blob/master/microprediction/writer.py)        | [Ambassy Fox](https://github.com/microprediction/microprediction/blob/master/submission_examples_transition/ambassy_fox.py) | [submission_examples_transition](https://github.com/microprediction/microprediction/tree/master/submission_examples_transition) |
| Running process                    | [MicroCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/crawler.py)      | [Malaxable Fox](https://github.com/microprediction/microprediction/blob/master/crawler_examples/malaxable_fox.py)           | [crawler_examples](https://github.com/microprediction/microprediction/tree/master/crawler_examples)                             |
| Running process using timemachines | [StreamSkater](https://github.com/microprediction/microprediction/blob/master/microprediction/streamskater.py) | [Shole Gazelle](https://github.com/microprediction/microprediction/blob/master/crawler_examples/shole_gazelle.py)           | [crawler_skater_examples](https://github.com/microprediction/microprediction/tree/master/crawler_skater_examples)               |

A more complete picture would include [SimpleCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/simplecrawler.py), 
[RegularCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/simplecrawler.py), 
[OnlineHorizonCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/onlinecrawler.py), 
[OnlineStreamCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/onlinecrawler.py) and
[ReportingCrawler](https://github.com/microprediction/microprediction/blob/master/microprediction/reportingcrawler.py).


### Creating streams

as well
as additional conveniences for creating streams such as 
[ChangePoll](https://github.com/microprediction/microprediction/blob/master/microprediction/polling.py), [MultiPoll](https://github.com/microprediction/microprediction/blob/master/microprediction/polling.py),
and [MultiChangePoll](https://github.com/microprediction/microprediction/blob/master/microprediction/polling.py).

### [Microprediction.Com](https://www.microprediction.com/) versus [Microprediction.org](https://www.microprediction.org/)

The former contains the [blog](https://www.microprediction.com/blog), a [knowledge center](https://www.microprediction.com/knowledge-center) with video tutorials, details of [competitions](https://www.microprediction.com/competitions) and prizemoney, and so forth. The latter is browser for humans looking to see how their algorithms are are performing, or whether their streams are updating.     

### Slack & Google Meets Tue 8pm/ Fri noon EST

Most people looking to contribute to this open initiative (and win beer money) join the [microprediction slack](https://join.slack.com/t/microprediction/shared_invite/zt-10ad1yiec-Jgsjkit~~dwNnpvRzyBTaQ). If that invite fails there might be one in the [knowledge center](https://www.microprediction.com/knowledge-center) that hasn't expired. There you will find Google Meet invite details for our regular informal chats.  

### Microprediction bookmarks

**Data**: [stream list](https://www.microprediction.org/browse_streams.html) | [stream explanations](https://www.microprediction.com/blog/livedata) | [csv](https://www.microprediction.org/features.html) **Client**: [client](https://github.com/microprediction/microprediction) | [reader](https://github.com/microprediction/microprediction/blob/master/microprediction/reader.py) | [writer](https://github.com/microprediction/microprediction/blob/master/microprediction/writer.py) | [crawler](https://github.com/microprediction/microprediction/blob/master/microprediction/crawler.py) | [crawler examples](https://github.com/microprediction/microprediction/tree/master/crawler_examples) | [notebook examples](https://github.com/microprediction/microprediction/tree/master/notebook_examples)
**Resources**: [popular timeseries packages](https://www.microprediction.com/blog/popular-timeseries-packages) |
[knowledge center](https://www.microprediction.com/knowledge-center) | [faq](https://www.microprediction.com/faq) |
[linked-in](https://www.linkedin.com/company/65109690) |
[microprediction.org (dashboard)](https://www.microprediction.org) | [microprediction.com (resources)](https://www.microprediction.com) |
[what](https://www.microprediction.com/what) | [blog](https://www.microprediction.com/blog) | [contact](https://www.microprediction.com/contact-us) |
[competitions](https://www.microprediction.com/competitions) |
[make-predictions](https://www.microprediction.com/make-predictions) |
[get-predictions](https://www.microprediction.com/get-predictions) |
[applications](https://www.microprediction.com/welcome-3) | [collective epidemiology](https://www.swarmprediction.com/about.html) 
**Video tutorials** : [1: non-registration](https://www.microprediction.com/python-1) | [2: first crawler](https://www.microprediction.com/python-2) |[3: retrieving historical data](https://www.microprediction.com/python-3) | [4: creating a data stream](https://www.microprediction.com/python-4) | [5: modifying your crawler's algorithm](https://www.microprediction.com/python-5) | 
[6: modifying crawler navigation](https://www.microprediction.com/python-6) 
**Colab notebooks**
[creating a new key](https://github.com/microprediction/microprediction/blob/master/notebook_examples/New_Key.ipynb) |
[listing current prizes](https://github.com/microprediction/microprediction/blob/master/notebook_examples/List%20Current%20Prizes.ipynb) |
[submitting a prediction](https://github.com/microprediction/microprediction/blob/master/notebook_examples/Python_Module_1_First_Submission.ipynb) | 
[choosing streams](https://github.com/microprediction/microprediction/blob/master/notebook_examples/Crawler_choosing_streams.ipynb) |
[retrieving historical data](https://github.com/microprediction/microprediction/blob/master/notebook_examples/Python_Module_3_Getting_History.ipynb)
**Related** [humpday](https://github.com/microprediction/humpday) | [timemachines](https://github.com/microprediction/timemachines) | [timemachines-testing](https://github.com/microprediction/timemachines-testing) | [microconventions](https://github.com/microprediction/microconventions) | [muid](https://github.com/microprediction/muid) | [causality graphs](https://github.com/microprediction/microactors-causality/tree/main/gallery) | [embarrassingly](https://github.com/microprediction/embarrassingly) | [key maker](https://github.com/microprediction/keymaker) | [real data](https://github.com/microprediction/realdata)| [chess ratings prediction](https://github.com/microprediction/chess) 
**Eye candy** [copula plots](https://github.com/microprediction/microactors-plots/tree/main/gallery) | [causality plots](https://github.com/microprediction/microactors-causality/tree/main/gallery) | [electricity case study](https://www.linkedin.com/posts/rusty-conover-ba5a6_predicting-nys-electricity-using-machine-activity-6750837765761503233-vYFu) 

Probably best to start in the [knowledge center](https://www.microprediction.com/knowledge-center) and remember [Dorothy, You're Not in Kaggle Anymore](https://www.linkedin.com/pulse/dorothy-youre-kaggle-anymore-peter-cotton-phd/). 

  
### Cite
See [CITE.md](https://github.com/microprediction/microprediction/blob/master/CITE.md)

### FAQ:
[FAQ](https://www.microprediction.com/faq) 

### Video tutorials
See the [Knowledge Center](https://www.microprediction.com/knowledge-center)

### Hey, where did the old README go? 

[README_LONGER.md](https://github.com/microprediction/microprediction/blob/master/README_LONGER.md)





