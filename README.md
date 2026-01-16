**Donor Retention Process**


**A. Project Overview**

This repository contains a complete donor retention analytics workflow designed to help organisations understand, measure, and improve donor loyalty over time.

Donor retention is one of the most important performance indicators for nonprofits because retaining donors is typically more cost-effective than acquiring new ones. This project moves beyond basic retention counts to a repeatable, structured analytics process that identifies behavioural patterns, segments donor cohorts, and supports strategic interventions.

Rather than a one-off script, this pipeline is a modular analytical system with clear stages from data preparation → feature engineering → cohort analysis → insight generation.

Although implementations vary across organisations, these principles apply broadly to most data analytics environments.

**B. System Architecture**

This analytical workflow is organised into clear, logical stages:

1. Raw Donor/Transaction Source
        ↓
2. Data Cleaning & Validation
        ↓
3. Feature Engineering (Recency, Frequency, Value)
        ↓
4. Cohort Definition & Retention Metrics
        ↓
5. Analysis & Visualisation
        ↓
6. Insights & Operational Recommendations


This layered architecture helps separate concerns, making it easier to debug, extend, and reuse each step independently.

**C. Step-by-Step Workflow Explanation**

**Step 1: Data Cleaning & Validation**

The first step ingests donor and transaction data and prepares it for analysis. This includes:

reading raw data (CSV/DB extracts)

ensuring consistent date formats

handling missing values

deduplicating records

import pandas as pd

df = pd.read_csv("donor_transactions.csv")
df["donation_date"] = pd.to_datetime(df["donation_date"])
df = df.drop_duplicates(subset=["donor_id", "donation_id"])


This phase ensures the rest of the pipeline operates on accurate, consistent data.

**Step 2: Feature Engineering**

Instead of relying on raw fields alone, behaviour-focused features are created to summarise donor engagement:

Recency — days since last donation

Frequency — number of donations in a period

Monetary Value — total donation value

df_features = df.groupby("donor_id").agg(
    recency=("donation_date", lambda x: (pd.Timestamp.today() - x.max()).days),
    frequency=("donation_id", "count"),
    monetary=("donation_amount", "sum")
).reset_index()


These engineered features are foundational to understanding retention behaviour.

**Step 3: Cohort Definition & Retention Metrics**

Donors are grouped into cohorts based on their first donation period, and retention patterns are computed.

A typical cohort table might show:

percent retained at 30 / 90 / 180 days

trend of returning donors by cohort

This cohort logic is critical for measuring actual behaviour over time.

**Step 4: Analysis & Visualisation**

The project includes visualisation scripts to show retention curves, behaviour patterns, and donor value trends.

Example (matplotlib):

import matplotlib.pyplot as plt

retention_curve.plot()
plt.title("Donor Retention Over Time")
plt.xlabel("Days Since First Donation")
plt.ylabel("Retention Rate")
plt.show()


These visuals bridge the gap between data and decision-ready insight.

**Step 5: Insights & Operational Recommendations**

Rather than just computing metrics, this step frames results in terms of decisions:

Which cohorts show early drop-off?

Are certain donor segments more resilient?

What behaviour signals predict long-term loyalty?

The outputs are designed to directly support strategic choices about engagement and stewardship.

**D. Why This Matters**

Reducing Manual Work

Before pipelines like this, donor retention calculations are often done manually across spreadsheets, pivot tables, and ad hoc filters. This pipeline automates:

donor segmentation

retention tabulation

cohort tracking

visual summaries

This saves analysts hours of manual preparation.

Supporting Operational Decisions

Clear retention analysis informs organisations about:

effectiveness of engagement strategies

timing of stewardship campaigns

value of long-term donors

By turning raw transaction data into retention insight, this project supports real decisions about where to invest effort and resources.

Innovation Beyond Occupation

This project is not just about computing a retention rate. It demonstrates how analytics can be designed as a process that supports sustained understanding and operational improvement. It shows how teams, even with limited resources, can build repeatable analytics that change the way decisions are made.

Although implementations vary across organisations, these principles apply broadly to most data analytics environments.

**E. Reflection & Learnings**

Working on the Donor Retention Process reinforced that retention is both a metric and a pattern.

Some key learnings:

Behavioural features matter more than raw counts.
Recency, frequency, and monetary value capture signals predictive of future engagement.

Cohort analysis surfaces trends that aggregate metrics hide.
Different donor groups behave differently, and understanding this helps prioritise interventions.

Visualisation communicates insight faster than tables.
Retention curves often reveal patterns at a glance that rows and columns cannot.

From a leadership perspective, this project demonstrates an important shift: analysis is not a task — it’s a process. Analysts should design workflows that can be reused, audited, and extended. That mindset elevates analytical work from “reporting” to analytical infrastructure.

For analysts moving into strategic roles, the lesson is to design workflows that are transparent, flexible, and directly linked to decisions.

**How to Use This Repository**

Clone the repository:

git clone https://github.com/Kaviya-Mahendran/Donor_Retention_Process


Install dependencies:

pip install -r requirements.txt


Place your donation dataset(s) in the root directory

**Run the main pipeline:**

python run_retention_analysis.py


Review generated outputs and visualisations

Final Note

This repository is a foundation for repeatable donor retention analytics.
It reflects the analytical discipline required to turn transactional data into operational insight.
