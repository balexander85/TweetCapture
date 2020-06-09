"""test_tweet_capture.py"""
from os import path

from furl import furl
import pytest

from tweet_capture import TweetCapture

CHROME_DRIVER_PATH = ""
SCREEN_SHOT_DIR_PATH = "screenshots"


@pytest.mark.parametrize(
    "url",
    [
        "https://twitter.com/RealKaylaJames/status/1237720669024108545",
        "https://twitter.com/BeQueerDoCrime/status/1268036084765798402",
        "https://twitter.com/Cawlitative/status/1268886549531426823",
        "https://twitter.com/Austin_Police/status/1267226527848181763",
        "https://twitter.com/reidepstein/status/1268738899616182272",
        "https://twitter.com/pastormarkburns/status/1268887999934353410",
        "https://twitter.com/washingtonpost/status/1268854962525798400",
    ],
)
def test_tweet_screen_shot_tweet(url):
    """
    Verify functionality tweet_capture module
    """
    tweet_id = furl(url).path.segments[-1]

    with TweetCapture(
        chrome_driver_path=CHROME_DRIVER_PATH, headless=True
    ) as tweet_capture:
        screen_cap_file_path = tweet_capture.screen_capture_tweet(url)

    assert screen_cap_file_path == path.join(
        SCREEN_SHOT_DIR_PATH, f"tweet_capture_{tweet_id}.png"
    )
