from sensor.constant import training_pipeline
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException

class TrainPipeline:
    def __init__(self) -> None:
        self.trainig_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainig_pipeline)
        self.trainig_pipeline_config = training_pipeline_config
        
    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        