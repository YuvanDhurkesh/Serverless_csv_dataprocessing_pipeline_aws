# Serverless CSV Data Processing Pipeline using AWS

## 📌 Project Overview

This project demonstrates a complete serverless data engineering pipeline built using AWS cloud services.  
The pipeline automatically processes CSV files uploaded to Amazon S3, performs preprocessing using AWS Lambda, catalogs the data using AWS Glue, transforms it into optimized Parquet format, enables SQL querying through Amazon Athena, and visualizes insights using Amazon QuickSight.

The architecture is fully serverless, scalable, event-driven, and suitable for modern cloud-native ETL workflows.


---

# 🚀 AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Store raw, processed, and final data |
| AWS Lambda | Preprocess uploaded CSV files |
| AWS Glue Crawler | Automatically detect schema |
| AWS Glue ETL | Transform CSV into Parquet |
| AWS Glue Data Catalog | Store metadata and table definitions |
| Amazon Athena | Query data using SQL |
| Amazon QuickSight | Build interactive dashboards |
| Amazon CloudWatch | Monitor Lambda logs |
| AWS IAM | Access control and permissions |

---

# 📂 Project Workflow

## 1️⃣ Upload CSV File to S3

A raw CSV file is uploaded into:

```text
csv-raw-data-yuvan
```

This triggers the entire pipeline automatically.

---

## 2️⃣ AWS Lambda Preprocessing

An S3 event triggers the Lambda function:

```text
csv-preprocessor
```

The Lambda function:
- reads the uploaded CSV
- validates records
- performs preprocessing/cleaning
- stores the processed CSV into:

```text
csv-processed-data-yuvan
```

---

## 3️⃣ AWS Glue Crawler

The Glue crawler scans the processed CSV bucket and:
- identifies schema
- infers column data types
- creates metadata tables in Glue Data Catalog

Database used:

```text
csv_pipeline_db
```

---

## 4️⃣ AWS Glue ETL Job

AWS Glue ETL job:
- reads cataloged CSV data
- transforms data into Parquet format
- writes optimized output into:

```text
csv-final-data-yuvan
```

Benefits of Parquet:
- columnar storage
- faster analytics
- lower query cost

---

## 5️⃣ Amazon Athena Querying

Athena is used to query the processed Parquet data directly from S3 using SQL.

Example query:

```sql
SELECT * 
FROM csv_processed_data_yuvan
LIMIT 10;
```

---

## 6️⃣ Amazon QuickSight Dashboard

QuickSight connects with Athena to create:
- bar charts
- pie charts
- analytics dashboards
- visual reports

---

# 📊 Features

- Fully serverless architecture
- Event-driven automation
- Automated schema discovery
- ETL transformation pipeline
- SQL querying without servers
- Cloud-native analytics workflow
- Dashboard visualization

---

# 📁 Project Structure


# ⚙️ Setup Steps

## Step 1 — Create S3 Buckets

Create:
- raw bucket
- processed bucket
- final parquet bucket
- Athena results bucket

---

## Step 2 — Configure Lambda

- Create Lambda function
- Add S3 trigger
- Attach IAM role
- Upload preprocessing code

---

## Step 3 — Upload CSV

Upload CSV into raw bucket.

---

## Step 4 — Configure Glue Crawler

- Create crawler
- Select processed S3 bucket
- Create Glue database
- Run crawler

---

## Step 5 — Create Glue ETL Job

- Use Glue Studio Visual ETL
- Add source from Data Catalog
- Add transformation
- Write output as Parquet to S3

---

## Step 6 — Query Using Athena

- Configure Athena result bucket
- Select Glue database
- Run SQL queries

---

## Step 7 — Build Dashboard in QuickSight

- Connect Athena dataset
- Import data
- Create charts and dashboards

---

# 📸 Screenshots



# 🔒 IAM Permissions Used

The project required IAM roles with permissions for:
- S3 access
- Lambda execution
- Glue operations
- Athena querying
- QuickSight access

---

# 📈 Future Improvements

- Add AWS Step Functions orchestration
- Add SNS email notifications
- Implement CI/CD pipeline
- Use Terraform or CloudFormation
- Add data quality validation
- Schedule automatic crawler execution
- Integrate EventBridge monitoring

---

# 🎯 Learning Outcomes

Through this project, I learned:
- serverless architecture design
- AWS event-driven workflows
- ETL pipeline implementation
- cloud-native analytics
- schema discovery automation
- Athena SQL querying
- dashboard visualization using QuickSight

---

# 🧹 Resource Cleanup

After project completion:
- deleted QuickSight account
- removed Glue jobs and crawlers
- deleted S3 buckets
- removed Lambda functions

to avoid unnecessary AWS charges.

---

# 👨‍💻 Author

**Yuvan Dhurkesh SJ**

B.Tech CSE Student | AWS SAA | AWS DVA | AWS CLF
