# Source Data Analysis

## 1. Dataset Overview

* Total Rows: 2,823
* Total Columns: 25
* Dataset Type: Retail Sales Orders (Line Item Level)

Each row represents a product sold within a specific order.

---

## 2. Data Types Summary

* Numeric: 9 columns
* Categorical: 16 columns
* Date fields stored as string: `ORDERDATE`

---

## 3. Data Quality Assessment

### Missing Values Summary

| Column       | Missing Values |
| ------------ | -------------: |
| ADDRESSLINE2 |          2,521 |
| STATE        |          1,486 |
| TERRITORY    |          1,074 |
| POSTALCODE   |             76 |

---

## 4. Duplicate Analysis

* No duplicate rows were detected.

---

## 5. Attribute Assessment

### 5.1 ADDRESSLINE2

* More than 89% missing values.
* No strong analytical value identified.
* Will be excluded from the dimensional model.

---

### 5.2 PHONE

* Not required for analytical reporting.
* Will be excluded from the dimensional model.

---

### 5.3 STATE

* Missing values are country-dependent rather than random.
* Countries like USA, Canada, Australia, and Japan contain state/province data.
* Many European countries do not provide state-level information.
* UK analysis shows:

  * Most cities have "Unknown" state
  * Only Cowes maps to "Isle of Wight"
  * No inconsistencies found within cities
* Conclusion: STATE is business-dependent and not a data quality issue.
* Will be retained in the dimensional model.
* Missing values will be replaced with `Unknown`.

---

### 5.4 TERRITORY

* Represents business sales regions (not strict geography).
* Examples:

  * Europe → EMEA
  * Australia → APAC
  * Japan → Japan
  * Singapore → APAC / Japan (mixed assignment)
* USA and Canada often have missing values.
* Missing values are business-related.
* Will be retained in the dimensional model.
* Missing values will be replaced with `Unknown`.

---

### 5.5 POSTALCODE

* Contains 76 missing values (~2.7%).
* Useful for geographic analysis.
* Will be retained.
* Missing values replaced with `Unknown`.

---

## 6. Cardinality Analysis

### Low Cardinality Attributes

* YEAR_ID (3)
* DEALSIZE (3)
* TERRITORY (3)
* QTR_ID (4)
* STATUS (6)
* PRODUCTLINE (7)

### High Cardinality Attributes

* PRODUCTCODE (109)
* ORDERDATE (252)
* ORDERNUMBER (307)
* CUSTOMERNAME (92)
* SALES (2763)

---

## 7. Order-Level Analysis

* Total Orders: 307
* Total Line Items: 2,823
* Orders contain between 1 and 18 line items
* Average line items per order: ~9

---

## 8. Grain Observation (Preliminary)

Each row appears to represent:

> One product line item within a sales order

This will be formally validated during the dimensional modeling phase.

---

## 9. Key Observations

* Dataset represents a classic retail sales transactional system.
* Strong star-schema suitability.
* Presence of clear fact-like measures (SALES, QUANTITYORDERED).
* Geography attributes are partially optional and business-driven.
* TERRITORY is a business classification, not strict geography.
* STATE is optional and varies by country structure.
* Data quality is generally high with minimal duplicates.

---

## 10. Open Questions

* Should MSRP be treated as a fact or product attribute?
* Should STATUS and DEALSIZE be modeled as junk dimension?
* Should ORDERDATE be normalized into a full Date Dimension?
* Confirm final grain definition before schema design.

---

## 11. Conclusion

The dataset is well-suited for building a **Sales Data Mart using Kimball Dimensional Modeling** with a star schema centered around sales order line items.
