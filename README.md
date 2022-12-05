This is a fork of [Perfkit Benchmarker](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker). Please refer the original repository's documentation for details. This section lists the changes vis-a-vis the original repostiory to address a few broken benchmarks and/or using higher tool versions in running the benchmarks.

*   [cassandra-env.sh.j2](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/data/cassandra/cassandra-env.sh.j2) - Updated JVM_OPTS to use higher version of jamm-x.x.x.jar
*   [cassandra_stree_benchmark.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_benchmarks/cassandra_stress_benchmark.py) - Changed the result metrics text to be aligned with the higher version of cassandra benchmarking package.
*   [kubernetes_nginx.yaml.j2](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/data/container/kubernetes_nginx/kubernetes_nginx.yaml.j2) - Updated the nginx deployment to use internal lb instead of exposing it via clusterIP
*   [kubernetes_nginx_benchmark.py](https://github.com/prakhag2/PerfKitBenchmarker/blob/master/perfkitbenchmarker/linux_benchmarks/kubernetes_nginx_benchmark.py) - Changes to fetch the load balancer ip instead of the cluster ip
