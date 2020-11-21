def _extract(spark, conf):
    return (
        spark.read.format("csv") \
                  .option("header", "true") \
                  .load(f"{conf.get('src_path')}/sensor_data.csv")
    )
