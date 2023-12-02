from image_segmentation.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self, config):
        self.config = config.get_data_validation_config()

    def run(self):
        data_ingestion = DataValidation(self.config)
        
        return data_ingestion.validate()