## Summary

## Task 1  
### Gap Analysis and Fraud Prevention

**1. False Negatives**

**Definition:** Transactions that were not flagged as fraud but resulted in chargebacks.

**Analysis:**
- **Count:** There are 12 false negative transactions in the dataset.
- **Fraud Scores:** Range from 22 to 65.
- **Insights:** 20% of transactions are bypassing the fraud detection measures, resulting in chargebacks. Reviewing these transactions for patterns could lead to the identification of additional fraud screening rules. It's worth noting that chargebacks can also occur for reasons other than fraud. In these cases, root cause analysis would be beneficial.

**Actions:**
- Review the accounts for potential friendly fraud and consider alternative prevention methods outside of fraud screening (e.g., unclear billing descriptors may cause cardholders to not recognize a legitimate purchase).
- Determine if there are patterns that could have indicated true fraud.
- Adjust scoring for existing rules or create additional rules to address suspicious patterns.

**2. False Positives**

**Definition:** Transactions flagged as fraud but approved and did not result in chargebacks.

**Analysis:**
- **Count:** There are 10 false positive transactions in the dataset.
- **Fraud Scores:** Range from 78 to 88.
- **Insights:** 10% of transactions are inaccurately flagged as fraud. This decreases revenue from legitimate customers and reduces customer satisfaction. Legitimate transactions in the fraud queue also take time away from reviewing actual fraud.

**Actions:**
- Consider increasing the scoring threshold for the fraud queue.
- Perform data analysis to determine if specific rules are behind patterns of false positives. Reduce rule scores if relevant.
- If repeat customers end up in the false positive category, consider adding them to a "safe" list.

---

## Task 2  
### Fraud Trend Identification and Rules Creation

**Fraud Trends:**
- Mismatches between billing country and IP location country  
  → 127 transactions have mismatched country data  
- Same phone number used across multiple user IDs  
  → 18 phone numbers are associated with more than 1 account  
  → One phone number is associated with 5 accounts, and referral fraud is suspected  
- Suspiciously low or unusually high transaction amounts  
  → 168 were over $5k and 18 were under $10 — customer history would provide important context  
- Last-minute bookings  
  → 109 bookings were made within 1 day of check-in/departure — customer history would also provide important context here

**Example Rules:**
- **Billing country ≠ IP country**  
  → Flag transaction and assign moderate risk score (can be combined with issuer country mismatch for higher severity).  
- **Customer phone number associated with > _ accounts**  
  → Assign dynamic score based on number of associated accounts:  
  - 2–3 accounts: moderate  
  - 4+ accounts: high risk  
- **Transaction amount outside expected range**  
  → Flag if amount is significantly below historical average (possible test transaction).  
  → Flag if amount is significantly above customer’s historical range or known product price points.  
- **Last-minute booking + high-risk signals**  
  → If booking is within 24 hours of travel/event **and** the customer is new or device ID has prior fraud history, assign a high severity alert.

---

### Rule Creation Process

**1. Review Existing Rules**
- Audit current rules
- Identify gaps based on recent fraud patterns
- Note rules with high false positive or false negative rates

**2. Define and Prioritize New Rules**
- Create rules based on observed trends (e.g., IP and billing mismatch, high-value transactions from new accounts)
- Set clear conditions and thresholds for each rule
- Prioritize based on risk level and frequency

**3. Configure Rule Actions**
- Assign actions to each rule (e.g., auto-decline, flag for review, score)
- For brand new rules, do not auto-decline until after testing is complete

**4. Test with Historical Data**
- Run rules on past data to validate logic.
- Measure impact on fraud detection and approval rates.

**5. Deploy and Monitor**
- Deploy rules in a controlled environment.
- Monitor outcomes for unexpected behavior or volume changes.

**6. Set Up Feedback Loop**
- Use manual review outcomes and chargeback data to refine rules.
- Adjust thresholds and logic as needed.

**7. Review and Update Regularly**
- Schedule rule audits to ensure relevance.
- Use analytics to detect new trends and inform updates.
- Monitor BI dashboards to continuously track KPIs.
