from utils.logger import *

class Config():
    def __init__(self, load=True):

        if not os.path.exists(self.dir_output):
            os.makedirs(self.dir_output)

        # singleton logger
        self.logger = sc_logger.get_logger()

    # general config
    dir_output = "results/test"
    filename = "data/test.csv"
