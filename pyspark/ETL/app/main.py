import json
import logging
import importlib
import argparse
from pyspark.sql import SparkSession


def _createSparkSession():
    return SparkSession.builder.master("local[*]").appName("etl").getOrCreate()


def _parseArguments():
    # Parse arguments by spark-submit
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    return parser.parse_args()


def main():

    args = _parseArguments()

    logging.debug("loading conf.json...")
    with open("conf.json", "r") as conf_file:
        conf = json.load(conf_file)

    logging.debug("creating SparkSession...")
    spark = _createSparkSession()

    logging.debug("jobs/run.py...")
    job_module = importlib.import_module(f"jobs.{args.job}")
    job_module._run(spark, conf)


if __name__ == "__main__":
    main()