# 📂 Automated File Management in AWS 🚀  

## 📝 Overview  
This project demonstrates an **automated file management system** using **AWS services**. It handles file uploads, event-driven processing, metadata updates, and serves a **static website** listing stored files.  

## 🏗️ Architecture  
The system consists of the following AWS components:  
![LAB3- workflow](https://github.com/user-attachments/assets/4903abe8-fb20-43d6-b648-e7df035be6bc)

### ☁️ Amazon S3 (Two Buckets)  
- **🗂️ S3 (Primary)** – Stores processed files in a `FILES` folder and is configured as a static website.  
- **📥 S3 (Input)** – Receives new file uploads and triggers notifications.  

### 🔒 Security Policy  
- **🔐 S3 (Primary)** is restricted to allow access **only from a specific home IP address**.  

### 📩 Amazon SQS  
- Receives notifications from **S3 (Input)** when a new file is uploaded.  
- Triggers **Lambda #1** for further processing.  

### ⚡ AWS Lambda Functions  
1️⃣ **Lambda #1:**  
   - Triggered by **SQS** when a file is uploaded to **S3 (Input)**.  
   - Extracts the **filename** and updates **DynamoDB** (`Processing` status).  
   - Copies the file to **S3 (Primary)** in the `FILES` folder.  

2️⃣ **Lambda #2:**  
   - Triggered **directly by S3 (Primary)** when a file is added to `FILES`.  
   - Updates **DynamoDB**, setting the status to `✅ Successful`.  

### 📊 Amazon DynamoDB  
Stores file metadata:  
- 🏷️ **Filename** (Primary key)  
- ⏳ **Timestamp** (Last updated time)  
- 📌 **Status** (`Processing` → `Successful`)  

### 🌐 Static Website in S3  
- Configured as a **static website**.  
- Displays a list of **files stored in the `FILES` folder**.  

## 🔄 Workflow  
1️⃣ A **user uploads** a file to **S3 (Input)**.  
2️⃣ **S3 (Input)** triggers a **notification** to **SQS**.  
3️⃣ **SQS** invokes **Lambda #1**, which:  
   - Extracts **filename** & updates **DynamoDB** (`Processing`).  
   - Copies the file to **S3 (Primary)** → `FILES` folder.  
4️⃣ **S3 (Primary)** triggers **Lambda #2**, which:  
   - Extracts **filename** & updates **DynamoDB** (`✅ Successful`).  
5️⃣ The file appears in the **static website listing**.  

## 🚀 Deployment  
Use **AWS CloudFormation** or **Terraform** for automation. Ensure proper **IAM roles**:  
- 🛠️ **Lambda Execution Roles** → Access to **S3, SQS, and DynamoDB**.  
- 🔐 **S3 Bucket Policies** → Restrict access to **specific IPs**.  

## 🎯 Benefits  
✔ **Fully automated event-driven processing**  
✔ **Scalable & serverless architecture**  
✔ **Secure access control with S3 policies**  
✔ **Real-time updates in DynamoDB**  

## 🔮 Future Enhancements  
✨ Implement **AWS Step Functions** for workflow management.  
📢 Add **SNS notifications** for file processing updates.  
🎨 Improve **UI** using **AWS Amplify or React**.  

## 👨‍💻 Author  
Developed by **[Idan Uziel]**  

---
