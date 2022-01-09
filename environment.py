from BrainBucket.BDDBehave.Chapter_15_2.config_reader import ConfigReader
from BrainBucket.webelements.browser import Browser
from time import sleep


def before_all(context):
    configs = ConfigReader("BrainBucket/BDDBehave/Chapter_15_2/15_2_2/config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
    context.browser = browser


def after_scenario(context, scenario):
    context.browser.shutdown()
