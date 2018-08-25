
# Menu

* [Data-Pipeline](#data-pipeline)
* [AWS-IOT](#aws-iot)
* [Elasticsearch](#elasticsearch)
* [Kinesis](#kinesis)

## Data Pipeline

[Templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/welcome.html) available are -

* Process Data Using Amazon EMR with Hadoop Streaming
* Import and Export DynamoDB Data Using AWS Data Pipeline
* Copy CSV Data Between Amazon S3 Buckets Using AWS Data Pipeline
* Export MySQL Data to Amazon S3 Using AWS Data Pipeline
* Copy Data to Amazon Redshift Using AWS Data Pipeline

## AWS-IOT

| Component   |      Reference      |
|----------|:-------------:|
| Python IoT SDK |  https://github.com/aws/aws-iot-device-sdk-python |
| Device Gateway | Responsible for maintaining the sessions and subscriptions for all connected devices in an IoT solution |
| Rule Engine | It utilizes a SQL-based syntax that selects data from message payloads and triggers actions based on the characteristics of the IoT data|
| Device Shadow | It acts as a message channel to send commands reliably to a device, and store the lastknown state of a device in the AWS platform. |
| Things | The device and fleet of devices |
| Control Layer | The control point for access to the Speed Layer and the nexus for fleet management |
| Speed Layer | The inbound, high-bandwidth device telemetry data bus and the outbound device command bus |
| Serving Layer | The access point for systems and humans to interact with the devices in a fleet, to perform analysis, archive, and correlate data, and to use real-time views of the fleet.|
| Authorization | https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html |

Ref - https://d0.awsstatic.com/whitepapers/core-tenets-of-iot1.pdf

## Elasticsearch

| Component   |      Reference      |
|----------|:-------------:|
| Elasticsearch Domain |  https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html |
| Sample Demo Setup with VPC Logs | https://aws.amazon.com/blogs/security/how-to-visualize-and-refine-your-networks-security-by-adding-security-group-ids-to-your-vpc-flow-logs/#more-3559 | 

## Kinesis
General Kinesis Information and Libraries

### General Information

| Component   |      Reference      |
|----------|:-------------:|
| Kinesis Producer Library |  https://github.com/awslabs/amazon-kinesis-producer |
| Kinesis Connector Library | https://github.com/awslabs/amazon-kinesis-connectors | 
| Kinesis Data Transformation | https://aws.amazon.com/blogs/compute/amazon-kinesis-firehose-data-transformation-with-aws-lambda/ |


### Shards

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

### Record

It is composed of 

* Partition Key
* Sequence Number
* Data Blob

### Kinesis Connector Library Pipeline Workflow

* (1) Kinesis Stream 
* (2) iTransformer
* (3) iFilter
* (4) iBuffer
* (5) iEmitter
* (6) S3, Dynamodb, RedShift etc.


### Kinesis Firehose

| Component Name   | Max Retry Time Period  |   Failed Folder Name |
|------------------:|:-------------------------:|----------------------|
| S3 | 24hrs | failed objects are stored in (s3_failed folder) |
| RedShift | 0-120 min (0-7200 sec) | Skips S3 objects and creates a manifest file in S3 for manual backup under (errors folder) |
| Elasticsearch | 0-120 min (0-7200 sec) | Skips index requests and stores in (elasticsearch_failed folder)|

* The PutRecordBatch() operation can take up to 500 records per call or 4 MB per call, whichever is smaller. 
* Buffer size ranges from 1 MB to 128 MB.

## Lambda Blueprints for Kinesis Fireshose for Data Transformation

* Apache Log to JSON
* Apache Log to CSV
* Syslog to JSON
* Syslog to CSV
* General Firehose Processing
