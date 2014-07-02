"""
Provide a way to work with panda data frames in Spark
"""
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pandaspark.utils import add_pyspark_path, run_tests
add_pyspark_path()
from pyspark.join import python_join, python_left_outer_join, \
    python_right_outer_join, python_cogroup
from pyspark.rdd import RDD
from pandaspark.pstatcounter import PStatCounter
import pandas

class PRDD:
    """
    A Panda Resilient Distributed Dataset (PRDD), is an extension of the RDD.
    It is an RDD containg Panda dataframes and provides special methods that
    are aware of this. You can access the underlying RDD at _rdd, but be careful
    doing so. Note: RDDs are lazy, so you operations are not performed until required.
    """

    def __init__(self, rdd):
        self._rdd = rdd

    @classmethod
    def fromRDD(cls, rdd):
        """Construct a PRDD from an RDD. No checking or validation occurs"""
        return PRDD(rdd)

    def applymap(self, f, **kwargs):
        """
        Return a new PRDD by applying a function to each element of each
        Panda DataFrame.
        """
        return self.fromRDD(self._rdd.map(lambda data: data.applymap(f), **kwargs))

    def __getitem__(self, key):
        """
        Returns a new PRDD of elements from that key


        """
        return self.fromRDD(self._rdd.map(lambda x: x[key]))

    def collect(self):
        """
        Collect the elements in an PRDD and concatenate the partition

        """
        def appendFrames(frame_a, frame_b):
            return frame_a.append(frame_b)
        return self._rdd.reduce(appendFrames)

    def stats(self, columns = []):
        """
        Compute the stats for each column provided in columns.
        Parameters
        ----------
        columns : list of str, contains all comuns for which to compute stats on
        """
        def reduceFunc(sc1, sc2):
            return sc1.merge_pstats(sc2)

        return self._rdd.mapPartitions(lambda i: [PStatCounter(dataframes = i, columns = columns)]).reduce(reduceFunc)

if __name__ == "__main__":
    run_tests()
