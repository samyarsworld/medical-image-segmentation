
class TargetPredictionPipeline:
    def __init__(self, config):
        self.config = config.get_target_prediction_config()

    def run(self, img):        
        output = "output"

        return output