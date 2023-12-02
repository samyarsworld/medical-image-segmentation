from image_segmentation.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self, config):
        self.config = config.get_data_transformation_config()

    def run(self):
        data_transformation = DataTransformation(self.config)
        data_transformation.transform()
