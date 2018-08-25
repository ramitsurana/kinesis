# kinesis-info
General Kinesis Information and Libraries

## General Information

| Component   |      Reference      |
|----------|:-------------:|
| Kinesis Producer Library |  https://github.com/awslabs/amazon-kinesis-producer |
| Kinesis Connector Library | https://github.com/awslabs/amazon-kinesis-connectors | 
| Kinesis Data Transformation | https://aws.amazon.com/blogs/compute/amazon-kinesis-firehose-data-transformation-with-aws-lambda/ |


## Shards

| Name   |      Provisioning      |
|----------|:-------------:|
| 1 Stream |  2 Shards |
| Data Input | 2 Mb/sec |
| Data Output | 4 Mb/sec |
| Reads | 10 transactions/sec |
| Writes | 2000 records/sec |

Resharding

* Shard Split
* Shard Merge

## Record

It is composed of 

* Partition Key
* Sequence Number
* Data Blob

### Kinesis Connector Library Pipeline Workflow

[1] Kinesis Stream 
[2] iTransformer
[3] iFilter
[4] iBuffer
[5] iEmitter
[6] S3, Dynamodb, RedShift etc.


## Kinesis Firehose

| Component Name   | Max Retry Time Period  |   Failed Folder Name |
|------------------:|:-------------------------:|----------------------|
| S3 | 24hrs | s3_failed | failed objects are stored in s3_failed folder |
| RedShift | 0-120 min (0-7200 sec) | Skips S3 objects and creates a manifest file for manual backup  |
| Elasticsearch | 0-120 min (0-7200 sec) | Skips index requests and stores in elasticsearch_failed folder|

## Lambda Blueprints for Kinesis Fireshose for Data Transformation

* Apache Log to JSON
* Apache Log to CSV
* Syslog to JSON
* Syslog to CSV
* General Firehose Processing
