## Run Locally

Requirements: 1] ubuntu 16.04 or above. 2] JVM 3] python3.6 or above.  

1. To use ```spark-submit``` install Apache Spark & configure bashrc, spark-env.sh.  
     this might help  
     https://medium.com/@brajendragouda/installing-apache-spark-on-ubuntu-pyspark-on-juputer-ca8e40e8e655


2. Unset if PYSPARK_DRIVER_PYTHON is set to jupyter (gedit ~/.bashrc) (Optional).**
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
5. Edit $(USER) to your _USER@host:~$_  in _conf.json_ for data src_path & dest_path (Required).  
   Edit _requirement.txt_ for required packages(Optional).
```
$ cd spark_projects/pyspark/ETL/app
$ gedit conf.json
```

6. run via spark-submit
```
$ make
$ cd ./deploy && $SPARK_HOME/bin/spark-submit --py-files jobs.zip --files conf.json main.py --job run
```
