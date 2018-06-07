from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.types import StringType,IntegerType,ArrayType,StructField
from pyspark.sql.types import StructType as struct

import pyspark.sql.functions as func
from pyspark.sql.functions import udf
from pyspark.sql.types import Row
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
sc=SparkContext.getOrCreate()
ORACLE_DRIVER_PATH = "C:\Program Files\Java\ojdbc5.jar"                                            
Oracle_CONNECTION_URL ="jdbc:oracle:thin:TPA_DEV_APP01/password@CTSC00847233301:1521:orcl"
sqlContext = SQLContext(sc)
ora_tmp=spark.read.format('jdbc').options(
        url=Oracle_CONNECTION_URL,
        dbtable="ASPOLICY",
        driver="oracle.jdbc.driver.OracleDriver"
        ).load()
ora_tmp.createOrReplaceTempView("people")
asd=spark.sql("SELECT POLICYGUID,POLICYNUMBER FROM people")
tab2=spark.read.format('jdbc').options(
        url=Oracle_CONNECTION_URL,
        dbtable="ASPOLICYFIELD",
        driver="oracle.jdbc.driver.OracleDriver"
        ).load()
ta2=asd.join(tab2,['POLICYGUID'],'outer')
ta2.createOrReplaceTempView("dat1")
orgtab2=spark.sql("SELECT  POLICYGUID,POLICYNUMBER,FIELDNAME,FIELDTYPECODE,DATEVALUE,TEXTVALUE,INTVALUE,FLOATVALUE FROM dat1")
ab= orgtab2.filter(orgtab2.FIELDNAME == "AppReceivedDate")
ab.withColumn("Year",func.year(ab.DATEVALUE)).groupby("Year").count().coalesce(1).write.format('json').save('/path/AppReceivedDate.json')
Asclient=spark.read.format('jdbc').options(
        url=Oracle_CONNECTION_URL,
        dbtable="ASCLIENT",
        driver="oracle.jdbc.driver.OracleDriver"
        ).load()
Ascountry=spark.read.format('jdbc').options(
        url=Oracle_CONNECTION_URL,
        dbtable="ASCOUNTRY",
        driver="oracle.jdbc.driver.OracleDriver"
        ).load()
Asclient.createOrReplaceTempView("CLIENT1")
Ascountry.createOrReplaceTempView("COUNTRY1")
cli=spark.sql("SELECT LEGALRESIDENCECOUNTRYCODE FROM CLIENT1")
con=spark.sql("SELECT COUNTRYCODE,COUNTRYSHORTNAME FROM COUNTRY1")
SEC=cli.join(con,cli.LEGALRESIDENCECOUNTRYCODE==con.COUNTRYCODE,'outer')
SEC1=SEC.groupby("LEGALRESIDENCECOUNTRYCODE","COUNTRYSHORTNAME").count()
SE1=SEC1.filter(SEC1['count']>1)
SE1.coalesce(1).write.format('json').mode('overwrite').save('/path/CountryNumbers')
Cli=spark.sql("SELECT SEX FROM CLIENT1")
third=Cli.fillna({'SEX':'companies'})
third.groupby("SEX").count().coalesce(1).write.format('json').mode('overwrite').save('/path/GenderDistribution')







