# from sensor.configuration.mongo_db_connection import MongoDBClient

from sensor.constant import training_pipeline
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig


if __name__ == "__main__":
    # mongodb_client = MongoDBClient()
    # print("Collection name", mongodb_client.database.list_collection_names())
    
    training_pipeline_config = TrainingPipelineConfig()
    