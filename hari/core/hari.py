"""
"""

from pyspark.sql import SparkSession, DataFrame

from spark_stage_metrics import StageMetrics

from typing import Optional, Literal

class Hari:
    """
    
    """
    def __init__(self, spark_session, save_metrics = False, stagemetrics = None):
        self.__spark_session: SparkSession = spark_session
        self.__save_metrics: bool = save_metrics
        self.__stagemetrics: StageMetrics = stagemetrics

    @property
    def stagemetrics(self) -> StageMetrics:
        return self.__stagemetrics

    
    def load_table(
        self: object, 
        path: str,
        type: Literal['path', 'catalog'],
        format: Optional[Literal['csv', 'parquet', 'orc', 'excel']] = None,
        filters: Optional[str] = None,
    ) -> DataFrame:
        
        if type == 'path' and not format:
            raise ValueError("The 'format' parameter is required when 'type' is set to 'path'.")


    def _load_table_catalog(
        self: object,
        path: str,
        filters: Optional[str] = None,
    ) -> DataFrame:
        
        if self.__spark_session.catalog.tableExists(path):
            df = self.__spark_session.read.table(path)
            if not df.isEmpty():
                if filters:
                    df = df.where(filters)
                    return df
                else:
                    return df
            else:
                raise Exception(f"This table {path} is empty!")
        else:
            raise Exception(f"This path of table {path} not exists on catalog!")
    

    def _load_path_table() -> DataFrame:
        pass

        
        

        

        

        