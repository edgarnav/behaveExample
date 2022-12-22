from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import time


def before_all(context):
    context.web_driver = InitWebDriver().init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("http://www.saucedemo.com")


def after_all(context):
    time.sleep(5)
    context.web_driver.quit()


"""def before_feature(context):

def before_scenario(context):
    
def before_step(context):"""

