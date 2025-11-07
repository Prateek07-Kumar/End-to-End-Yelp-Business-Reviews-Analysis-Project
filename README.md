# End-to-End-Yelp-Business-Reviews-Analysis-Project

## Yelp Business Reviews Analysis
### Project Overview
This project performs a comprehensive analysis of Yelp business data and customer reviews using SQL and Python. It extracts insights about business categories, user behavior, review sentiment, and rating patterns to support data-driven decision-making.

### Project Architecture
The project consists of four main components that work together to ingest, process, and analyze Yelp data:

**1. Data Preparation and Splitting** **(split.py)**

**Purpose:** Handle the large 5GB Yelp review dataset by splitting it into manageable chunks.

**Process:**
- Reads the original **yelp_academic_dataset_review.json** file (5GB)
- Counts total lines in the JSON file to calculate distribution
- Splits the file into 10 smaller JSON files for easier processing
- Each split file contains an equal number of records
- Output files are named **split_file_1.json** through **split_file_10.json** and stored in a designated output directory

Why this step? Large JSON files are difficult to process and upload. Splitting makes the data manageable while maintaining individual JSON object integrity (one object per line).

**2. Sentiment Analysis Setup**
**(analyze_sentiment.ipynb)**

Purpose: Create a Python-based sentiment analysis function in the database.

### Key Steps:
  - Create a test table with sample reviews containing positive, negative, and neutral language
  - Develop a User Defined Function (UDF) called **analyze_sentiment()** using Python and the TextBlob library
  - The function analyzes review text and classifies sentiment into three categories:
      - Positive: Sentiment polarity > 0
      - Neutral: Sentiment polarity = 0
      - Negative: Sentiment polarity < 0
        
**Technology:** Uses TextBlob for natural language processing to determine sentiment polarity scores.

**3. Business Data Loading** **(yelp_businesses.ipynb)**

Purpose: Load and structure Yelp business data from AWS S3.

**Process:**
  - Create a raw variant table to store JSON data directly from S3
  - Use AWS credentials to access the S3 bucket containing
          **yelp_academic_dataset_business.json**
  - Parse the JSON variant data and extract relevant fields into a structured table:
      - **business_id**(string): Unique business identifier
      - **name**(string): Business name
      - **city**(string): City location
      - **state**(string): State/Province
      - **review_count** (string): Total number of reviews
      - **stars**(number): Average rating
      - **categories**(string): Comma-separated list of business categories
  - Create the final table **tbl_yelp_businesses** with 100 sample records
  - Verify data integrity with sample queries

**4. Reviews Data Loading** **(yelp_reviews.ipynb)**

**Purpose:** Load review data and apply sentiment analysis.

**Process:**
  - Create a raw variant table for JSON review data from S3
  - Use AWS credentials to access the S3 bucket containing review JSON files
  - Parse and extract review fields into a structured format:
      - **business_id** (string): Foreign key linking to businesses
      - **review_date** (date): Date the review was posted
      - **user_id** (string): Unique user identifier
      - **review_stars** (number): Star rating (1-5)
      - **review_text** (string): Full review text
      - **sentiments** (string): Sentiment classification from **analyze_sentiment()** UDF
  - Create the final table **tbl_yelp_reviews** with 1000 sample records
  - Apply the sentiment analysis function to all review texts

**Analysis Queries** **(SQL_Yelp_Analysis.ipynb)**

The project includes 10 comprehensive SQL analysis queries:

**Query 1: Business Categories Distribution**
  - Count the number of businesses in each category
  - Uses lateral split to handle comma-separated category values
  - Helps identify popular business types

  **Query 2: Top Restaurant Reviewers**
  - Identifies the 10 users who reviewed the most restaurants
  - Filters businesses by 'restaurant' category
  - Counts distinct businesses reviewed per user

**Query 3: Most Popular Categories by Review Volume**
  - Ranks business categories by total number of reviews
  - Combines category splitting with review aggregation
  - Shows which category types receive the most attention

**Query 4: Recent Reviews by Business**
  - Retrieves the 3 most recent reviews for each business
  - Uses window functions (ROW_NUMBER) with date partitioning
  - Useful for monitoring current business performance

**Query 5: Peak Review Month**
  - Identifies which month receives the highest review count
  - Aggregates reviews at the monthly level
  - Helps understand seasonal review patterns

**Query 6: 5-Star Review Percentage**
  - Calculates the percentage of 5-star reviews for each business
  - Uses conditional aggregation (CASE WHEN)
  - Shows which businesses have the highest customer satisfaction

**Query 7: Top Businesses by City**
  - Ranks the 5 most-reviewed businesses in each city
  - Uses the QUALIFY clause for partitioned ranking
  - Enables city-level competitive analysis

**Query 8: Average Rating for Popular Businesses**
  - Filters businesses with at least 100 reviews
  - Calculates average rating for established businesses
  - Focuses on quality metrics for well-reviewed businesses

**Query 9: Top Users and Their Reviews**
  - Lists the top 10 most-reviewed users
  - Shows all businesses reviewed by these power users
  - Identifies influential reviewers in the community

**Query 10: Top Businesses by Positive Sentiment**
  - Ranks businesses with the most positive sentiment reviews
  - Uses sentiment classification from the UDF
  - Highlights businesses with the best customer satisfaction

**Technology Stack**
  - Database: Snowflake (cloud data warehouse)
  - Data Storage: AWS S3
  - Query Language: SQL
  - Sentiment Analysis: Python (TextBlob library)
  - Data Format: JSON
  - Notebook Environment: Jupyter

### Key Features
  - Automated sentiment analysis on review text
  - Efficient handling of large datasets through splitting
  - Scalable cloud-based architecture using Snowflake and S3
  - Comprehensive business performance metrics
  - User behavior and engagement analysis
  - City and category-level insights
