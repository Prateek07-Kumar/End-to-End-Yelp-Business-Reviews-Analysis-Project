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
        
Technology: Uses TextBlob for natural language processing to determine sentiment polarity scores.

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
