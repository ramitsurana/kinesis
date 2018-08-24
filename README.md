# kinesis-info
General Kinesis Information and Libraries

## General Information

| Library   |      Reference      |
|----------|:-------------:|
| Kinesis Producer Library |  https://github.com/awslabs/amazon-kinesis-producer |
| Kinesis Connector Library | - | 


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

- [x] Kinesis Stream 
- [x] iTransformer
- [x] iFilter
- [x] iBuffer
- [x] iEmitter
- [x] S3, Dynamodb, RedShift etc.
