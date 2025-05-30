❄️ Snowflake-Streaming

This repository contains the configuration and components for a real-time data streaming application using Apache NiFi, AWS S3, and Snowflake.

🔍 Application Overview

The diagram below illustrates the high-level design (HLD) of the data streaming pipeline:
![image](https://github.com/user-attachments/assets/a262fb22-37f5-4576-8392-59c4c3d62415)



🚀 Project Objective

The goal of this project is to enable real-time data streaming into Snowflake, leveraging Apache NiFi for data movement and Snowflake’s Snowpipe, Streams, and Tasks for ingestion and transformation. An additional feature includes Amazon SNS alerts to monitor S3 bucket activity (e.g., detecting missing or delayed files).

⚙️ Architecture Overview

1. Data Generation

Synthetic data is generated using the Python script Test_Data_Generator.py.

2. Apache NiFi Deployment
   
Apache NiFi is deployed on an EC2 (large instance) with 100 GB storage.

Runs inside Docker using configuration in docker-compose.yml.

EC2 provisioning is automated using commands in the EC2_Commands.txt file.

3. Data Ingestion Workflow
   
NiFi pushes the generated data to an Amazon S3 bucket (Raw/ folder). 

The Raw files are moved to the Archive folder after 30 mins- 1hour of the object creation time.

An SNS (Simple Notification Service) topic is configured to monitor S3 activity. If no new files are detected within a defined time threshold (e.g., 24 hours), an alert is triggered.

Snowpipe continuously monitors the S3 bucket and loads the raw data into Snowflake.

4. Snowflake Processing
   
Stream objects track metadata changes from the raw table.

Tasks are used to automatically load and transform data into a changes table using the SCD Type 1 (SCD1) method and SCD2 Type 2 method as well.

🧊 Snowflake Table Structure

Table	Description

raw_table	Stores the full extract of customer data ingested from Snowpipe

changes_table	Contains the latest version of each record, applying SCD1 logic

type-2_changes_table	Contains the current and latest version of each record, applying SCD2 logic

All relevant SQL queries and DDL scripts can be found in the SQL Commands file.

📁 Repository Structure

├── Test_Data_Generator.py       # Python script to generate test data

├── docker-compose.yml           # Docker configuration for NiFi

├── EC2_Commands.txt             # EC2 setup and deployment steps

├── SQL_Commands.sql             # Snowflake SQL scripts for tables, streams, and tasks

├── lambda_error_handler.py      # Lamdba code for Alerting and movement of files into different folders

└── README.md                    # Project documentation

🛠️ Tech Stack

Python – Data generation

Apache NiFi – Data flow orchestration

AWS EC2 & S3 – Hosting and storage

Snowflake – Data warehouse with real-time ingestion and transformation features

AWS Lambda - To enable the alerting of the application and movement of files

Future enhancements

Embedding CI/CD



📸 Pipeline Execution

Below images describe the execution flow of the streaming pipeline:

EC2 Instance Initialization with Required Configuration
![image](https://github.com/user-attachments/assets/19b3bfd1-31f5-4bb9-b9eb-7679c8bfb71e)

Data Generation via Python Script
The Python script starts generating mock data for the pipeline.
![image](https://github.com/user-attachments/assets/57002cfd-4873-4d59-8ea6-210d02e55567)

Apache NiFi On-Prem Pipeline
The generated data flows through the NiFi data pipeline.
![image](https://github.com/user-attachments/assets/550f1654-ba98-491c-b346-aca80f684599)

Data Loaded to Amazon S3
Data successfully lands in the designated S3 bucket.
![image](https://github.com/user-attachments/assets/b7d13e58-8c3d-4efe-b538-cf26d57bae84)

Snowpipe Loads Data to Snowflake
Snowpipe detects the new data in S3 and ingests it into the Snowflake raw table.
![image](https://github.com/user-attachments/assets/e47de68b-3dc2-4481-a81a-3ddedec3774d)

Updating a Record
A sample update is made to an existing record to test change tracking.
![image](https://github.com/user-attachments/assets/8390b1bf-c320-4e6a-b375-3956fc3f91f5)

Changes Reflected in changes_table
The latest version of the record is captured in the changes table as per SCD1 logic.
![image](https://github.com/user-attachments/assets/b91f0d53-4517-4e05-b553-622b374d4cca)
