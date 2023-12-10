from image_segmentation.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:
    def __init__(self, config, train_loader, validation_loader):
        self.config = config.get_model_trainer_config()
        self.train_loader = train_loader
        self.validation_loader = validation_loader

    def run(self):
        model_trainer = ModelTrainer(self.config)
        model_trainer.train(self.train_loader, self.validation_loader)