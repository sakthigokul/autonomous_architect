import random

# ---- Data Quality Agent ----
def data_quality_agent(data):
    return {
        "nulls": random.randint(0, 10),
        "duplicates": random.randint(0, 5)
    }

# ---- Pipeline Agent ----
def pipeline_agent():
    return "Pipeline failed at stage 2"

# ---- Summary Agent ----
def summary_agent(qc, pipeline):
    return f"""
🔍 Data Quality Insights:
• Null Values: {qc['nulls']}
• Duplicates: {qc['duplicates']}

⚙️ Pipeline Status:
• {pipeline}

💡 Recommendations:
• Handle null values using imputation
• Remove duplicate records
• Retry pipeline execution

🚀 System Confidence: High
"""
history = []
# ---- Manager Agent ----
def manager_agent(input_text):
    history.append(input_text)
    text = input_text.lower()

    if "pipeline" in text:
        pipeline = pipeline_agent()
        return f"⚙️ Pipeline Status:\n{pipeline}"

    elif "data" in text or "dataset" in text:
        qc = data_quality_agent(input_text)
        return f"""
🔍 Data Quality Report:
- Nulls: {qc['nulls']}
- Duplicates: {qc['duplicates']}
"""

    else:
        qc = data_quality_agent(input_text)
        pipeline = pipeline_agent()
        return summary_agent(qc, pipeline)