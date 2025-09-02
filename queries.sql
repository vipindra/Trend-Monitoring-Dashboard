-- SQL Queries for Trend Monitoring Dashboard

-- Top 3 trending topics overall
SELECT topic, category, mentions
FROM trends
ORDER BY mentions DESC
LIMIT 3;

-- Average sentiment by category
SELECT category, AVG(sentiment) AS avg_sentiment
FROM trends
GROUP BY category;
