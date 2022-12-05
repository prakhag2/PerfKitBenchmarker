# Perfkit Benchmarker

This is a fork of [Perfkit Benchmarker](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker). Please refer the original repository's documentation for details. This section lists the changes vis-a-vis the original repostiory to address a few broken benchmarks and/or using higher tool versions for the benchmarks.

*   [cassandra-env.sh.j2](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/data/cassandra/cassandra-env.sh.j2) - Updated JVM_OPTS to use higher version of jamm-x.x.x.jar
*   [cassandra.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/cassandra.py) - Updated jna from 4.1.0 to 4.2.2 and cassandra from 2.1 to 4.1
*   [cassandra_stress_benchmark.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_benchmarks/cassandra_stress_benchmark.py) - Changed result metrics text to align with higher version of cassandra
*   [kubernetes_nginx.yaml.j2](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/data/container/kubernetes_nginx/kubernetes_nginx.yaml.j2) - Updated nginx deployment to use internal lb instead of clusterIP
*   [kubernetes_nginx_benchmark.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_benchmarks/kubernetes_nginx_benchmark.py) - Changes to fetch load balancer ip instead of cluster ip
*   [aerospike_client.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/aerospike_client.py) - Updated aerospike-tools from 7.0.5 to 8.0.2
*   [ant.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/ant.py) - Updated ant from 1.9.6 to 1.10.0
*   [mongodb_server.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/mongodb_server.py) - Updated mongodb from 3.0 to 6.0
*   [openjdk.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/openjdk.py) - Updated default from jdk 11 to 8
*   [redis_server.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/redis_server.py) - Updated redis from 6.2.1 to 7.0.3
*   [tomcat.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_packages/tomcat.py) - Updated tomcat from 8.0.28 to 9.0.67
*   [gcp_relational_db.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/providers/gcp/gcp_relational_db.py) - Updated defaults: MySQL 5.7 to 8.0 and Postgres 9.6 to 12
