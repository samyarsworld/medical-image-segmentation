from image_segmentation.logging import logger
from image_segmentation.exception import CustomException
import sys

from image_segmentation.config_manager import ConfigManager
from image_segmentation.pipeline.data_ingestion import DataIngestionPipeline
from image_segmentation.pipeline.data_validation import DataValidationPipeline
from image_segmentation.pipeline.data_transformation import DataTransformationPipeline
from image_segmentation.pipeline.model_training import ModelTrainingPipeline
from image_segmentation.pipeline.model_evaluation import ModelEvaluationPipeline
from image_segmentation.pipeline.target_prediction import TargetPredictionPipeline


config = ConfigManager()

STAGE_NAME = "Data Ingestion"
try:
   logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
   data_ingestion = DataIngestionPipeline(config)
   data_ingestion.run()
   logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
except Exception as e:
    exception = CustomException(e, sys)
    logger.exception(exception)
    raise exception


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


# STAGE_NAME = "Data Transformation"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_transformation = DataTransformationPipeline(config)
#    data_transformation.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception


# STAGE_NAME = "Model Training"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    model_training = ModelTrainingPipeline(config)
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


# STAGE_NAME = "Target Prediction"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    target_prediction = TargetPredictionPipeline(config)
#    text = "hello world"
#    prediction = target_prediction.run(text)
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     exception = CustomException(e, sys)
#     logger.exception(exception)
#     raise exception

