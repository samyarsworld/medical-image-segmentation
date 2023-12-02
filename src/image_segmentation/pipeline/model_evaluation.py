from image_segmentation.components.model_evaluation import ModelEvaluation
class ModelEvaluationPipeline:
    def __init__(self, config):
        self.config = config.get_model_evaluation_config()
    
    def run(self):
        model_evaluation = ModelEvaluation(self.config)
        model_evaluation.evaluate()