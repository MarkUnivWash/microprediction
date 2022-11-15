try:
    from microprediction.config_private import SHOLE_GAZELLE
except ImportError:
    raise Exception('You will need a write key. See https://www.microprediction.com/private-keys')
    
from microprediction.streamskater import StreamSkater

# Example of a "skater" that uses the TimeMachines package for point estimates
# And see the crawling docs: https://microprediction.github.io/microprediction/predict-using-python-microcrawler.html

# This crawls www.microprediction.org, as explained by the helper site www.microprediction.com

try:
    from timemachines.skaters.simple.thinking import thinking_slow_and_fast
except ImportError:
    print('pip install timemachines')

if __name__=='__main__':
    skater = StreamSkater(write_key=SHOLE_GAZELLE, f=thinking_slow_and_fast, use_std=False)
    skater.set_repository(
        'https://github.com/microprediction/microprediction/blob/master/crawler_examples/shole_gazelle.py')
    skater.set_email("no_email@supplied.com")  # Only used to send you a voucher if you win a daily prize
    skater.run()
