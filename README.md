![logo](img/logo.jpg)

[![buildstatus](https://travis-ci.org/sparklingpandas/sparklingpandas.svg?branch=master)](https://travis-ci.org/sparklingpandas/sparklingpandas)

==============
SparklingPandas
==============

SparklingPandas aims to make it easy to use the distributed computing power
of PySpark to scale your data analysis with Pandas.

Documentation
=========

None (right now).


Videos
=========
An early version of Sparkling Pandas was discussed in [Sparkling Pandas - using Apache Spark to scale Pandas - Holden Karau and Juliet Hougland](https://www.youtube.com/watch?v=AcyI_V8FeIU)

Requirements
=========

The primary requirement of SparklingPandas is that you have a recent (v1.4
currently) version of Spark installed - <http://spark.apache.org> and Python
2.7.

Using
=========

Make sure you have the SPARK_HOME enviroment variable set correctly, as
SparklingPandas uses this for including the PySpark libraries. You will
need to have built the Spark assembly jar as well, which you can do with
 `./sbt/sbt assembly -Phive` in the directory where your Spark installation is.
If you are using a pre-built version of Spark it normally includes the assembly
jar, so you can skip building it.

Some SparklingPandas components are built on the JVM, if building from source you
can compile these run `./sbt/sbt assembly`.

Other than that you can install SparklingPandas with pip and just import it.
The primary unit of SparklingPandas is a PRDD (Pandas Resillent Distributed
Data Set)

State
=========

This is in early development and should not be considered usable.

Support
=========

Check out our Google group at https://groups.google.com/forum/#!forum/sparklingpandas
