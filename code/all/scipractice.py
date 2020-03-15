from pyspark import SparkContext
sc=SparkContext('local','myapp')
data=[('a',3),('b',4),('a',1)]
zz=sc.parallelize(data).reduceByKey(lambda x,y:x+y)
# zz=sc.parallelize(data).reduceByKey(lambda x,y:x+y,10)

print(zz.collect())