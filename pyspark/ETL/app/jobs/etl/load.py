def _load(conf, transformedDF):
    transformedDF.write.mode("overwrite").parquet(f"{conf.get('dest_path')}/s3_output")
