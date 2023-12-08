from image_segmentation.components.data_construction import DataConstruction


class DataConstructionPipeline:
    def __init__(self, config):
        self.config = config.data_construction_config()

    def run(self):
        data_construction = DataConstruction(self.config)
        train_dataset, validation_dataset = data_construction.build()

        return train_dataset, validation_dataset
