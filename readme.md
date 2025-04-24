# Fraud Data Analysis

## User Story

As a Fraud Operations Analyst, I want to analyze order data so that I can effectively communicate insights and actionable fraud prevention recommendations to stakeholders.

---

## Overview 

### 1. Gap Analysis and Fraud Prevention

Objective: You are given a dataset of fraud decisions made over the past month, including details about false positives, false negatives, chargebacks, and successful approvals. Analyze the data to identify key gaps and suggest changes to improve fraud prevention without overly affecting approval rates. 

**Tasks**
* Perform a gap analysis to identify areas where false positives or false negatives are higher than expected.
* Provide a short summary of the key insights you find from the data.
* Suggest 2-3 actions you would take to improve fraud prevention processes.

**Results**
- [Gap Analysis Query](/sql-queries/gap-analysis.sql)
- [Summary and Actions](/summary.md#task-1)

### 2. Fraud Trend Identification and Rules Creation

Objective: You are given a dataset of orders created over a period of time, including details of the booking and customer information.

**Tasks**
* Identify fraud trend(s) among this dataset and could you provide a short summary of your observation.
* Provide potential rules that you would write to prevent such fraud trend(s).
* When adding such rules with any fraud provider, list out your steps.

**Results**
- [Fraud Trends Query](/sql-queries/fraud-trends.sql)
- [Connected Accounts Query](/sql-queries/phone-numbers.sql)
- [Summary and Actions](/summary.md#task-2)

---

## Demo
[View demo here](https://drive.google.com/file/d/1tVafkK8zPZezlYp3zZB5eCdYg32rrNlL/view?usp=sharing)

---

## Questions?

Feel free to [contact me on GitHub](https://github.com/lsieck519).