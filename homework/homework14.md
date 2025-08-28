# Reflection — Stage 14: Deployment & Monitoring

Deploying my regression model (predicting product reviews from price) brings several risks that require careful monitoring. First, schema drift may occur if new data sources or columns change format; this would be caught by logging a daily schema hash and alerting if mismatched. Second, null or malformed values in `product_price` could rise above 2%, leading to unreliable predictions; I would set an alert at that threshold. Third, the model’s accuracy may degrade over time due to market shifts; monitoring rolling RMSE on a weekly holdout set, with a threshold of RMSE > 0.5, would help detect this. Finally, system-level outages or slow responses (p95 latency > 500ms) and business misalignment (e.g., predictions diverging >20% from expected review-volume trends) are key failure modes.

Monitoring spans four layers:
- **Data**: schema hash, null percentage, feature distribution shifts (PSI > 0.05).  
- **Model**: rolling RMSE, prediction range sanity checks.  
- **System**: latency, uptime, error rate.  
- **Business**: alignment with sales/review volumes, percent of predictions accepted by downstream analysts.  

Ownership is shared. Platform engineering owns system health and on-call alerts. Data engineering owns schema checks and data freshness. The modeling team owns RMSE and drift monitoring, retraining every two weeks or when PSI > 0.05. Business stakeholders review dashboards weekly. Handoffs are structured: alerts route to the platform on-call first, logged in Jira; if model metrics fail, the ML team investigates and retrains; rollbacks require approval from both ML lead and product manager.

This layered approach ensures risks are caught early, metrics are visible, and responsibilities are clearly defined, creating a sustainable deployment and monitoring cycle.
