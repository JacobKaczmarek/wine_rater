from wine_rater.components.data_validation import DataValidation
from wine_rater.config.configuration import ConfigurationManager
from wine_rater import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        pipelilne = DataValidationPipeline()
        pipelilne.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e