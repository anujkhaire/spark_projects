# Run Locally

Requirements: 1] ubuntu 16.04 or above. 2] JVM 3] python3.6 or above.

1. To use ```spark-submit``` install Apache Spark & configure bashrc, spark-env.sh.

2. Unset if PYSPARK_DRIVER_PYTHON is set to jupyter (~/.bashrc).
```
$ unset PYSPARK_DRIVER_PYTHON=jupyter 
```

3. install pyspark to use it in python scripts.
```
$ pip install pyspark
```

4. git clone
```
$ git clone https://github.com/anujkhaire/spark_projects
```

5. run
```
$ cd spark_projects/pyspark/ETL/app
$ make
$ cd ./deploy && $SPARK_HOME/bin/spark-submit --py-files jobs.zip --files conf.json main.py --job run
```
