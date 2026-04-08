# # 🚀 Autonomous DataOps AI Assistant

## 📌 Overview

Autonomous DataOps AI Assistant is a multi-agent AI system designed to automate data quality monitoring and pipeline diagnostics in modern data engineering workflows.

The system simulates a digital data engineer by orchestrating multiple specialized agents to analyze datasets, detect issues, and generate actionable insights.

---

## 🎯 Problem Statement

Data pipelines often face failures and data quality issues such as null values and duplicate records.
Manual debugging and monitoring lead to delays, inefficiencies, and reduced reliability.

---

## 💡 Solution

This project introduces a **multi-agent architecture** where a central manager agent coordinates multiple specialized agents to:

* Perform data quality checks
* Monitor pipeline health
* Generate intelligent recommendations

---

## 🧠 Architecture

User Input
↓
Manager Agent (Orchestrator)
↓
-

## | Data Quality Agent | Pipeline Agent |

↓
Summary Agent
↓
Final Response

---

## 🤖 Agents Used

### 🧠 Manager Agent

* Orchestrates workflow
* Routes requests dynamically

### 📊 Data Quality Agent

* Detects null values
* Identifies duplicate records

### ⚙️ Pipeline Agent

* Simulates pipeline failures
* Provides pipeline status

### 📝 Summary Agent

* Aggregates outputs
* Generates insights and recommendations

---

## 🔁 Workflow

1. User sends input request
2. Manager Agent analyzes intent
3. Relevant agents are triggered
4. Results are combined
5. Final insights are returned

---

## 🌐 API Endpoints

### POST /analyze

**Input:**

```json
{
  "input_text": "check dataset"
}
```

**Output:**

* Data quality report
* Pipeline status
* Recommendations

---

## ☁️ Deployment

* Google Cloud Run
* FastAPI backend
* Public API endpoint

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Google Cloud Run
* Multi-Agent Architecture

---

## 🚀 Future Enhancements

* Integration with Vertex AI (Gemini)
* Real-time data pipeline monitoring
* Database integration for historical insights
* Automated remediation workflows

---

## 🏆 Key Highlights

* Multi-agent orchestration
* Modular and scalable design
* Real-world DataOps use case
* Cloud-native deployment

---

https://autonomous-architects-dy3uyiwt5a-uc.a.run.app/docs#/default/analyze_analyze_post

## 🔗 Live API

(Attach your Cloud Run URL here)
