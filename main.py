from MLFlow import logger
from MLFlow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLFlow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLFlow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLFlow.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\n x==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e