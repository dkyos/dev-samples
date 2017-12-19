

https://www.elastic.co/kr/downloads
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.0.1.tar.gz
wget https://artifacts.elastic.co/downloads/logstash/logstash-6.0.1.tar.gz

https://www.youtube.com/watch?v=rKy4sFbIZ3U
Use Logstash to load CSV into Elasticsearch

https://www.youtube.com/watch?v=imrKm6dV3NQ
Lecture 16 logstash job Kibana visualization

====================================================================
sample Dev Tools
====================================================================

get /cars

get /cars/_search
{
    "query": {
        "match_all":{}
    }
}

get /cars/_count


# cat config/elasticsearch.yml | grep disk
cluster.routing.allocation.disk.threshold_enabled: false

PUT _cluster/settings
{
    "transient": {
        "cluster.routing.allocation.disk.threshold_enabled": false
    }
}



====================================================================




