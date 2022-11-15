try:
    from microprediction.config_private import MESOLE_MAMMAL
except:
    raise Exception('You will need a write key. See https://www.microprediction.com/private-keys')
    
from microprediction.sequentialcrawler import SequentialStreamCrawler
from microprediction.univariate.skewdist import SkewDist


# This crawls www.microprediction.org, as explained by the helper site www.microprediction.com
# New video tutorials are available at https://www.microprediction.com/python-1 to help you
# get started
# And see the crawling docs: https://microprediction.github.io/microprediction/predict-using-python-microcrawler.html


if __name__ == "__main__":
    crawler = SequentialStreamCrawler(write_key=MESOLE_MAMMAL, min_lags=20, machine_type=SkewDist)
    crawler.set_repository(
        url='https://github.com/microprediction/microprediction/blob/master/crawler_examples/mesole_mammal.py')
    crawler.set_email("no_email@supplied.com")  # Only used to send you a voucher if you win a daily prize
    crawler.min_lags = 50
    crawler.max_active = 50
    crawler.run()
