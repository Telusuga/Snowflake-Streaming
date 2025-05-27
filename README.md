❄️ Snowflake-Streaming

This repository contains the configuration and components for a real-time data streaming application using Apache NiFi, AWS S3, and Snowflake.
Below HLD depicts the Application Overview
![image](https://github.com/user-attachments/assets/38474baf-ca1f-4e97-b7f6-4ec8af3c1044)


📌 Project Objective

The goal of this project is to enable real-time data streaming into Snowflake, leveraging Apache NiFi for data movement and Snowflake's Snowpipe, Streams, and Tasks for ingestion and transformation.

⚙️ Architecture Overview

1. Data Generation

Synthetic data is generated using the Python script Test_Data_Generator.py.

2. Apache NiFi Deployment
   
Apache NiFi is deployed on an EC2 (large instance) with 100 GB storage.

NiFi runs via Docker, using the configuration in docker-compose.yml.

EC2 setup and provisioning commands are documented in the EC2 Commands file.

3. Data Ingestion Workflow

NiFi pushes generated data to Amazon S3.

Snowpipe in Snowflake continuously monitors the S3 bucket and loads incoming data into a raw table.

4. Snowflake Processing
   
Stream objects track metadata changes from the raw table.

Tasks are used to automatically load and transform data into a changes table using the SCD Type 1 (SCD1) method.

🧊 Snowflake Table Structure

Table	Description

raw_table	Stores the full extract of customer data ingested from Snowpipe

changes_table	Contains the latest version of each record, applying SCD1 logic

All relevant SQL queries and DDL scripts can be found in the SQL Commands file.

📁 Repository Structure

├── Test_Data_Generator.py       # Python script to generate test data

├── docker-compose.yml           # Docker configuration for NiFi

├── EC2_Commands.txt             # EC2 setup and deployment steps

├── SQL_Commands.sql             # Snowflake SQL scripts for tables, streams, and tasks

└── README.md                    # Project documentation

🛠️ Tech Stack

Python – Data generation

Apache NiFi – Data flow orchestration

AWS EC2 & S3 – Hosting and storage

Snowflake – Data warehouse with real-time ingestion and transformation features

🔮 Future Enhancements

📊 Data Visualization: Integrate with BI tools like Tableau, Power BI, or Streamlit for interactive dashboards and reporting.

🏷️ SCD Type 2 (SCD2): Add support for slowly changing dimensions type 2 to maintain historical versions of records for audit and trend analysis.



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
