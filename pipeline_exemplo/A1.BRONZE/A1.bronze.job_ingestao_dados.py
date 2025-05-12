from hari import *

def main(params):

    spark = hari.criaSessaoSpark(spark, salvarMetricas=True, nivelLogSpark="ERROR", "job_ingestao_dados") 
    logger = hari.log(NIVEL="ERROR")
    parametros = params
    
    # se passar a sessao do spark, usa, senao cria
    # se True salvarMetricas, vai coletar as metricas do measure

    logger.info("Inicia a Execucao do Job")

    logger.info("Ingestão dos dados")
    df1 = hari.leituraTabela("s3://path-to-tabela1", filtros = "", tipo = "path", formato = "csv", *params)
    df2 = hari.leituraTabela("s3://path-to-tabela2", filtros = "", tipo = "path", formato = "csv", *params)
    df3 = hari.leituraTabela("s3://path-to-tabela3", filtros = "", tipo = "path", formato = "parquet", *params)


    logger.info("ETL")
    "[...]" 


    logger.info("Carga dos Dados")
    hari.salvarTabela("bronze.tabela1", formato="delta")
    hari.salvarTabela("bronze.tabela2", formato="delta")
    hari.salvarTabela("bronze.tabela3", formato="delta")

    hari.metadados.incluirDependenciaDestino("bronze.tabela1")
    hari.metadados.incluirDependenciaDestino("bronze.tabela2")
    hari.metadados.incluirDependenciaDestino("bronze.tabela3")

    hari.metadados.informarConclusaoJob("A1.bronze.job_ingestao_dados")

    hari.encerraSessaoSpark()
  