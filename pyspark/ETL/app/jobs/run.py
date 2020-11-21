from jobs.etl import extract, transform, load


def _run(spark, conf):
    df = extract._extract(spark, conf)
    transformedDF = transform._transform(spark, df)
    load._load(conf, transformedDF)
