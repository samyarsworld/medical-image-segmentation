from image_segmentation.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self, config):
        self.config = config.get_data_ingestion_config()

    def run(self):
        data_ingestion = DataIngestion(self.config)
        data_ingestion.download_files_from_cloud()
