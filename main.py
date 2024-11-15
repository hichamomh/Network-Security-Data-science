from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
import sys
## Initiate the Data Ingestion

if __name__=='__main__':
    try:
        logging.info("Enter the try block")
        data_ingestion_config = DataIngestionConfig(TrainingPipelineConfig())
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
    
    except Exception as e:
           raise NetworkSecurityException(e,sys)