# QUERY1 : DATASET OVERVIEW

USE consumer_shopping_analytics;

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT `Customer ID`) AS unique_customer_ids,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount,
    ROUND(AVG(`Review Rating`), 2) AS average_review_rating
FROM shopping_behavior;


# QUERY 2  : PRODUCT CATEGORY PERFORMANCE 

SELECT
    Category,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM shopping_behavior
GROUP BY Category
ORDER BY total_purchase_amount DESC;


# QUERY 3 : AGE GROUP ANALYSIS

SELECT
    CASE
        WHEN Age < 20 THEN 'Under 20'
        WHEN Age BETWEEN 20 AND 29 THEN '20-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        ELSE '60+'
    END AS age_group,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount
FROM shopping_behavior
GROUP BY age_group
ORDER BY age_group;


#QQUERY 4 : SEASONAL ANALYSIS

SELECT
    Season,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount,
    SUM(`Purchase Amount (USD)`) AS total_purchase_amount
FROM shopping_behavior
GROUP BY Season
ORDER BY total_purchase_amount DESC;

#QUERY 5 : DISCOUNT ANALYSIS

SELECT
    `Discount Applied`,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount,
    ROUND(AVG(`Review Rating`), 2) AS average_review_rating
FROM shopping_behavior
GROUP BY `Discount Applied`;


# QUERY 6 : PAYMENT METHOD ANALYSIS 

SELECT
    `Payment Method`,
    COUNT(*) AS purchase_records,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM shopping_behavior),
        2
    ) AS percentage_of_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount
FROM shopping_behavior
GROUP BY `Payment Method`
ORDER BY purchase_records DESC;

# QUERY 7 : SUBSCRIPTION ANALYSIS

SELECT
    `Subscription Status`,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount,
    ROUND(AVG(`Review Rating`), 2) AS average_review_rating
FROM shopping_behavior
GROUP BY `Subscription Status`;


# QUERY 8 : PRODUCT CATEGORY AND GENDER

SELECT
    Gender,
    Category,
    COUNT(*) AS purchase_records,
    ROUND(AVG(`Purchase Amount (USD)`), 2) AS average_purchase_amount
FROM shopping_behavior
GROUP BY Gender, Category
ORDER BY Category, Gender;