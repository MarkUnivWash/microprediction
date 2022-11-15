from microprediction.config_private import THALLODAL_CAT
from microprediction.sequentialcrawler import SequentialStreamCrawler, DigestDist

# New video tutorials are available at https://www.microprediction.com/python-1 to help you
# get started running crawlers at www.microprediction.com
# And see the crawling docs: https://microprediction.github.io/microprediction/predict-using-python-microcrawler.html


if __name__ == "__main__":
    crawler = SequentialStreamCrawler(write_key=THALLODAL_CAT, min_lags=500, machine_type=DigestDist)
    # Aside: as of 0.10.12, DigestMachine is the default machine_type, so this need not even be supplied
    crawler.set_repository(
        url='https://github.com/microprediction/microprediction/blob/master/crawler_examples/thallodal_cat.py')
    # Setting repo is optional, it simply hyperlinks your crawler on the leaderboard
    crawler.set_email("no_email@supplied.com")  # Only used to send you a voucher if you win a daily prize
    crawler.min_lags = 500
    crawler.max_active = 500
    crawler.run()

