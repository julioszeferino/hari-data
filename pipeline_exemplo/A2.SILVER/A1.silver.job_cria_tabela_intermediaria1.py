from hari import *


def transformacao_2(parametros, spark, logger, df):
    return df


def transformacao_1(parametros, spark, logger, df):
    return df


def main(params):

    spark = hari.criaSessaoSpark(spark, salvarMetricas=True, nivelLogSpark="ERROR", "job_cria_tabela_intermediaria1") 
    logger = hari.log(NIVEL="ERROR")
    parametros = params
    
    # se passar a sessao do spark, usa, senao cria
    # se True salvarMetricas, vai coletar as metricas do measure

    hari.metadados.incluirDependenciaOrigem("bronze.tabela1")
    hari.metadados.incluirDependenciaOrigem("bronze.tabela2")
    hari.metadados.incluirDependenciaOrigem("bronze.tabela3")

    logger.info("Inicia a Execucao do Job")

    logger.info("Ingestão dos dados")
    df1 = hari.leituraTabela("bronze.tabela1", filtros = "", tipo = "catalog")
    df2 = hari.leituraTabela("bronze.tabela2", filtros = "", tipo = "catalog")
    df3 = hari.leituraTabela("bronze.tabela3", filtros = "", tipo = "catalog")


    logger.info("ETL")
    df1 = transformacao_1(parametros, spark, logger, df1)

    df3 = transformacao_2(parametros, spark, logger, df3)
    

    logger.info("Carga dos Dados")
    hari.salvarTabela("silver.tabela4", formato="delta")

    hari.metadados.incluirDependenciaDestino("silver.tabela4")

    hari.metadados.informarConclusaoJob("A1.silver.job_ingestao_dados")

    hari.encerraSessaoSpark()
