"""
imports
"""
from datetime import datetime, timedelta
from pyspark.sql.functions import sum, avg, max, min, mean, count, stddev, col
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType,
)


"""
dataframe schema
"""
schema = StructType(
    [
        StructField("Time", StringType()),
        StructField("DeviceID", IntegerType()),
        StructField("SensorID", IntegerType()),
        StructField("Reading", FloatType()),
        StructField("Count", IntegerType()),
    ]
)


#%time df.rdd.collect()
def uncompress(spark, df):

    # columns = ['Time','DeviceID','SensorID','Reading','Count']
    _list = []
    all_rows = df.rdd.collect()
    for row in all_rows:

        count = int(row.Count)

        for i in range(count):
            date = datetime.strptime(row.Time, "%Y-%m-%d %H:%M")
            date = date - timedelta(minutes=i)
            time = date.strftime("%Y-%m-%d %H:%M")
            device_id = row.DeviceID
            sensor_id = row.SensorID
            reading = row.Reading

            temp_list = time, device_id, sensor_id, reading, count
            _list.append(temp_list)
            # temp_df = spark.createDataFrame(l,schema=schema)
            # df2 = df2.union(temp_df)

    return _list


# ll = un()
# df2 = spark.createDataFrame(ll, schema=schema)

# list to tuple
# to_tuple = [tuple(x) for x in ll]

# seperate coloums
# list(zip(*un()))

# df2.show()

"""
main method
"""


def _transform(spark, df):

    df.cache()

    df = df.withColumn("Time", df["Time"].cast(StringType()))
    df = df.withColumn("DeviceID", df["DeviceID"].cast(IntegerType()))
    df = df.withColumn("SensorID", df["SensorID"].cast(IntegerType()))
    df = df.withColumn("Reading", df["Reading"].cast(FloatType()))
    df = df.withColumn("Count", df["Count"].cast(IntegerType()))

    _list = uncompress(spark, df)

    _transformedDF = spark.createDataFrame(_list, schema=schema)
    _transformedDF.show()

    return _transformedDF
