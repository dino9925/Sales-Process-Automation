# Sales-Process-Automation-

#Objective:
To provide a comprehensive explanation of the approach, tools, and skills used to automate the process of web scraping, email sending, and integration with Flask.

#Skills Used:
- Python Programming: Core scripting language for all modules.
- Selenium (Web Scraping): Used Selenium WebDriver to automate dynamic website interactions and extract structured data.
- Email Automation: Used Python's smtplib and email.message to send personalized emails automatically.
- Flask Web Framework: Built a simple web interface email functions.
- Data Handling: Processed and stored scraped data using pandas and exported it to CSV.
- Automation & Error Handling: Incorporated time.sleep, exception handling to ensure reliability.

#Approach & Process

1. Web Scraping with Selenium:
 
- Launched a browser instance using Selenium WebDriver (e.g., Chrome).
- Navigated to target websites or platforms (e.g., Google Jobs).
- Scraped data such as company name, industry, location.
- Stored the collected data into a structured format (CSV).

2. Email Automation:

- Designed a clear and concise email template.
- Used smtplib to authenticate and send emails from a chosen email address.
- Loaded data from the CSV and personalized each message (e.g., using company name).

3. Flask Integration:

- Created endpoints to trigger email sending.
- Ran the application locally for testing and demo purposes.

3. Testing and Debugging:

- Ensured smooth coordination between scraping, data storage, and email modules.
