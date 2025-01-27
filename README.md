# IndeedScrapeAnalyzer
# JobScraperBot

IndeedScrapeAnalyzer is a Python-based automation tool for scraping job postings from **Indeed** and analyzing the extracted data. This repository contains scripts to gather job information, process it, and generate visualizations to gain insights into job markets.

## Features

- Scrapes job postings from **Indeed** using Selenium and BeautifulSoup.
- Extracts key information such as job titles, company names, locations, salaries, ratings, and descriptions.
- Saves the data into a CSV file for further analysis.
- Analyzes job data, including top companies hiring and common job titles.
- Visualizes job distribution using bar charts.

## Prerequisites

To use this repository, ensure you have the following installed:

- Python 3.8 or higher
- Google Chrome
- ChromeDriver

## Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `beautifulsoup4`
- `selenium`
- `lxml`
- `matplotlib`
- `webdriver-manager`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IndeedScrapeAnalyzer.git
   cd IndeedScrapeAnalyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `base_url` or `pagination_url` in the script to specify your target search criteria (e.g., job title and location).

## Usage

1. Run the script to scrape job data:
   ```bash
   python job_offers.py
   ```

2. The scraped job data will be saved in a CSV file named `indeed_jobs1.csv`.

3. Analyze the data:
   - The script performs basic analysis, including counting job postings by company and listing the top 10 job titles.

4. Visualize the data:
   - A bar chart of job distribution across companies is displayed and saved as `job_distribution.png`.

## Output Files

- **CSV File**: `indeed_jobs1.csv` contains the scraped job data.
- **Visualization**: `job_distribution.png` shows a bar chart of job counts by company.

## Example

Sample output after running the script:

```plaintext
Number of jobs per company:
{'Company A': 10, 'Company B': 5, 'Company C': 7}

Top 10 most common job titles:
Python Developer: 15
Data Scientist: 12
Software Engineer: 10
...
```

![Job Distribution Chart](job_distribution.png)

## Notes

- This script is designed for educational purposes and may require updates for changes to the Indeed website's structure.
- Be mindful of the terms of service of any website you scrape.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Happy Scraping!**
