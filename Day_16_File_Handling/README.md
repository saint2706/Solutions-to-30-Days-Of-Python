# 📁 Day 16: File Handling for Business Analytics

Welcome to Day 16 of the 50 Days of Python for MBA program! Today we explore file handling operations essential for business data processing and analysis.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Handle different file types (text, JSON, CSV) programmatically
- Implement text preprocessing and analysis for business documents
- Extract and validate email addresses from text data
- Perform document similarity analysis for content management
- Count technology mentions in datasets for market research
- Apply proper error handling for robust file operations

## 📋 Topics Covered

### 1. Basic File Operations

- Reading and writing text files safely
- Counting words and lines in documents
- Handling file encoding issues

### 2. Text Analysis and Preprocessing

- Cleaning text data for analysis
- Removing stop words and noise
- Word frequency analysis
- Document similarity calculations

### 3. Structured Data Processing

- JSON data extraction and analysis
- CSV file processing and analysis
- Country and language data analysis

### 4. Email Processing

- Email validation using regex
- Email extraction from documents
- Contact information management

### 5. Business Applications

- Document comparison and similarity scoring
- Technology trend analysis
- Market research data processing

## 🚀 Key Functions in `fh.py`

Our file handling module includes powerful functions for business analytics:

### Document Analysis

```python
def counter(fname: str) -> Tuple[int, int]:
    """Count words and lines in a text file."""
    
def find_most_common_words(fname: str, value: int) -> List[Tuple[int, str]]:
    """Find the most frequently used words in a text file."""
```

### Data Processing

```python
def most_spoken_languages(fname: str, value: int) -> List[Tuple[int, str]]:
    """Analyze language frequency from country data."""
    
def most_populated_countries(fname: str, value: int) -> List[Dict[str, Union[str, int]]]:
    """Find the most populated countries from JSON data."""
```

### Email Management

```python
def extract_emails(fname: str) -> List[str]:
    """Extract all email addresses from a text file."""
    
def check_email(word: str) -> bool:
    """Validate if a word is a valid email address."""
```

### Text Analytics

```python
def document_similarity(filename_1: str, filename_2: str) -> Optional[float]:
    """Calculate similarity between two text documents."""
    
def clean_text(text: str) -> str:
    """Clean and normalize text for analysis."""
```

## 💼 Why File Handling is Critical for Business Analytics

In modern business, data comes from everywhere - reports, emails, surveys, social media, and databases. File handling skills enable you to:

- **Automate Data Processing**: Process thousands of documents without manual intervention
- **Integrate Systems**: Connect different business systems through file-based data exchange
- **Generate Reports**: Create persistent analysis reports for stakeholders
- **Monitor Trends**: Track business metrics and market trends from various data sources
- **Ensure Quality**: Validate and clean data from multiple sources
- **Scale Operations**: Handle growing volumes of business data efficiently

## 💻 Exercises: Day 16

### Exercise 1: Document Statistics Analyzer

Create a function that analyzes multiple business documents and produces a summary report:

```python
def analyze_business_documents(file_paths):
    """
    Analyze multiple documents and return comprehensive statistics
    """
    total_words = 0
    total_lines = 0
    all_themes = {}
    
    for file_path in file_paths:
        words, lines = counter(file_path)
        total_words += words
        total_lines += lines
        
        # Extract top themes from each document
        themes = find_most_common_words(file_path, 5)
        for freq, word in themes:
            all_themes[word] = all_themes.get(word, 0) + freq
    
    return {
        'total_words': total_words,
        'total_lines': total_lines,
        'common_themes': sorted(all_themes.items(), key=lambda x: x[1], reverse=True)[:10]
    }
```

**Business Application**: Executive report summarization and content analysis.

### Exercise 2: Customer Contact Management System

Build a comprehensive email processing system:

```python
def process_customer_communications(input_files):
    """
    Extract and organize customer contact information
    """
    all_emails = []
    contact_database = {}
    
    for file_path in input_files:
        emails = extract_emails(file_path)
        for email in emails:
            if check_email(email):
                domain = email.split('@')[1]
                if domain not in contact_database:
                    contact_database[domain] = []
                contact_database[domain].append(email)
                all_emails.append(email)
    
    return {
        'total_contacts': len(all_emails),
        'companies': len(contact_database),
        'contact_by_company': contact_database
    }
```

**Business Application**: CRM data management and customer outreach campaigns.

### Exercise 3: Competitive Intelligence Tool

Develop a document comparison system for market analysis:

```python
def competitive_analysis(company_docs, competitor_docs):
    """
    Compare company content with competitor content
    """
    results = {}
    
    for comp_doc in company_docs:
        results[comp_doc] = {}
        for competitor_doc in competitor_docs:
            similarity = document_similarity(comp_doc, competitor_doc)
            results[comp_doc][competitor_doc] = similarity
    
    return results
```

**Business Application**: Content strategy and competitive positioning.

### Exercise 4: Market Research Data Processor

Create an advanced technology trend analysis system:

```python
def comprehensive_tech_analysis(data_files, technologies_to_track):
    """
    Track multiple technologies across various datasets
    """
    results = {}
    
    for tech in technologies_to_track:
        results[tech] = {'total_mentions': 0, 'files_mentioned': []}
    
    for file_path in data_files:
        tech_counts = analyze_technology_mentions(file_path)
        for tech, count in tech_counts.items():
            if tech in results:
                results[tech]['total_mentions'] += count
                if count > 0:
                    results[tech]['files_mentioned'].append(file_path)
    
    return results
```

**Business Application**: Technology investment decisions and market trend analysis.

## 🏆 Challenge Project: Business Intelligence File Processor

Create a comprehensive system that combines all file handling concepts:

**Requirements:**

1. **Multi-format Support**: Handle TXT, JSON, CSV files
2. **Batch Processing**: Process multiple files simultaneously
3. **Error Handling**: Graceful error recovery and reporting
4. **Analytics Dashboard**: Generate summary statistics and insights
5. **Export Functionality**: Save results in multiple formats

**Expected Features:**

- Document similarity clustering
- Email contact management
- Trend analysis and reporting
- Content quality assessment
- Automated report generation

## 📚 Key Takeaways

1. **Robust Error Handling**: Always handle file operations with try-except blocks
2. **Encoding Matters**: Use UTF-8 encoding for international business data
3. **Context Managers**: Use `with` statements for automatic resource management
4. **Path Handling**: Use `os.path.join()` for cross-platform compatibility
5. **Data Validation**: Always validate extracted data before processing
6. **Business Context**: Consider how file processing serves business objectives

## 💡 Advanced Tips for Business Applications

### 1. Batch Processing Pattern

```python
def process_business_files(directory_path, file_pattern="*.txt"):
    """Process multiple files in a directory"""
    import glob
    
    files = glob.glob(os.path.join(directory_path, file_pattern))
    results = []
    
    for file_path in files:
        try:
            result = process_single_file(file_path)
            results.append({
                'file': file_path,
                'status': 'success',
                'data': result
            })
        except Exception as e:
            results.append({
                'file': file_path,
                'status': 'error',
                'error': str(e)
            })
    
    return results
```

### 2. Progress Tracking for Large Operations

```python
def process_with_progress(files, process_func):
    """Process files with progress indication"""
    total_files = len(files)
    results = []
    
    for i, file_path in enumerate(files, 1):
        print(f"Processing {i}/{total_files}: {os.path.basename(file_path)}")
        result = process_func(file_path)
        results.append(result)
        
        # Show progress percentage
        progress = (i / total_files) * 100
        print(f"Progress: {progress:.1f}%")
    
    return results
```

## 🔗 Integration with Other Business Tools

File handling often works with:

- **Databases**: Import/export data for analysis
- **APIs**: Process downloaded data files
- **Reporting Tools**: Generate input files for dashboards
- **Email Systems**: Process attachments and communications
- **Cloud Storage**: Handle files from cloud platforms

## 📖 Next Steps

After mastering file handling, explore:

- **Day 17**: Regular Expressions for advanced pattern matching
- **Day 22**: NumPy for numerical file processing
- **Day 23**: Pandas for advanced data file manipulation
- **Day 30**: Web Scraping for automated data collection

## ✅ Solutions

You can find comprehensive solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've mastered file handling for business analytics. You can now process various file types, extract meaningful insights, and build robust data processing pipelines!
