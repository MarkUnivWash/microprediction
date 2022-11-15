try:
    from microprediction.config_private import COMAL_CHEETAH
except ImportError:
    raise Exception('You will need a write key. See https://www.microprediction.com/private-keys')
    
from microprediction.fitcrawler import FitCrawler
from microprediction.univariate.expnormdist import ExpNormDist


# Illustrates the use of offline parameter estimation
# See the repo  microprediction/offline for how to use Github actions for this purpose

# This crawls www.microprediction.org, as explained by the helper site www.microprediction.com
# New video tutorials are available at https://www.microprediction.com/python-1 to help you get started
# And see the crawling docs: https://microprediction.github.io/microprediction/predict-using-python-microcrawler.html


STORED_PARAM_URL = 'https://raw.githubusercontent.com/microprediction/offline/main/modelfits/expnorm'


class RegularFitCrawler(FitCrawler):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def include_stream(self, name=None, **ignore):
        return '~' not in name


if __name__ == '__main__':
    crawler = RegularFitCrawler(write_key=COMAL_CHEETAH, machine_type=ExpNormDist, max_evals=50,
                         min_seconds=1, min_elapsed=60*60, max_active=500, decay=0.005,
                         param_base_url=STORED_PARAM_URL, stop_loss=50)
    crawler.set_repository(
        url='https://github.com/microprediction/microprediction/blob/master/crawler_examples/comal_cheetah.py')
    crawler.set_email("me@gmail.com")  # Only used to send you a voucher if you win a daily prize
    crawler.run()
