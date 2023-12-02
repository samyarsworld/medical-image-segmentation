from image_segmentation.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:
    def __init__(self, config):
        self.config = config.get_model_trainer_config()

    def run(self):
        model_trainer= ModelTrainer(self.config)
        model_trainer.train()