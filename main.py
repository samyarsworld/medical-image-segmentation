from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
import sys

from image_segmentation.config_manager import ConfigManager
from image_segmentation.pipeline.data_ingestion import DataIngestionPipeline
from image_segmentation.pipeline.data_validation import DataValidationPipeline
from image_segmentation.pipeline.data_construction import DataConstructionPipeline
from image_segmentation.pipeline.model_training import ModelTrainingPipeline
from image_segmentation.pipeline.model_evaluation import ModelEvaluationPipeline
from image_segmentation.pipeline.target_prediction import TargetPredictionPipeline
from image_segmentation.components.data_construction import DataConstruction



config = ConfigManager()

# STAGE_NAME = "Data Ingestion"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_ingestion = DataIngestionPipeline(config)
#    data_ingestion.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


# STAGE_NAME = "Data Validation"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_validation = DataValidationPipeline(config)
#    data_validation.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


# STAGE_NAME = "Data Build and Transformation"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_construction = DataConstructionPipeline(config)
#    train_dataset, validation_dataset, train_loader, validation_loader = data_construction.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
   
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


# STAGE_NAME = "Model Training"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    model_training = ModelTrainingPipeline(config, train_loader, validation_loader)
#    model_training.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


# STAGE_NAME = "Model Evaluation"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    model_evaluation = ModelEvaluationPipeline(config)
#    model_evaluation.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


STAGE_NAME = "Target Prediction"
try:
   logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
   target_prediction = TargetPredictionPipeline(config)
   target_prediction.run()
   logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
except Exception as e:
    exception = CustomException(e, sys)
    logger.exception(exception)
    raise exception



