from bs4 import BeautifulSoup
from csv import writer
import time
from lxml import etree as et
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
base_url = 'https://www.indeed.com/jobs?q=python&l=Texas'
paginaton_url = "https://www.indeed.com/jobs?q={}&l={}&radius=35&start={}"

driver = webdriver.Chrome(ChromeDriverManager().install())

def get_current_url(url, job_title, location):
    job = job_title
    loc = location
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location}"
    driver.get(url)
    time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys(job_title)
    #time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="text-input-where"]').send_keys(location)
    #time.sleep(1)
    driver.find_element_by_xpath("//button[text() ='Search']").click()
    time.sleep(1)
    
    current_url = driver.current_url
    page_content = driver.page_source
    product_soup = BeautifulSoup(page_content, 'html.parser')
    dom = et.HTML(str(product_soup))
  
    return current_url , job , loc , dom


current_url , job_title , location , dom = get_current_url(base_url,'Data',"US")
print(current_url)
print(job_title)


jobs_num = driver.find_element(By.CLASS_NAME,"jobsearch-JobCountAndSortPane-jobCount").get_attribute("innerText")
jobs_num = jobs_num.replace(' jobs','')
    
if ',' in jobs_num and (jobs_num := jobs_num.replace(',', '')).isdigit():
    jobs_num = int(jobs_num)
print(jobs_num)

# functions to extract job link
def get_job_link(job):
   try:
       job_link = job.xpath('./descendant::h2/a/@href')[0]
   except Exception as e:
       job_link = 'Not available'
   return job_link

# functions to extract job title
def get_job_title(job):
   try:
       job_title = job.xpath('./descendant::h2/a/span/text()')[0]
   except Exception as e:
       job_title = 'Not available'
   return job_title


# functions to extract the company name
def get_company_name(job):
   try:
       company_name = job.xpath('.//span[@class="css-92r8pb eu4oa1w0"]/text()')
   except Exception as e:
       company_name = 'Not available'
   return company_name


# functions to extract the company location
def get_company_location(job):
   try:
       company_location = job.xpath('.//div[@data-testid="text-location"]/text()')
   except Exception as e:
       company_location = 'Not available'
   return company_location


# functions to extract salary information
def get_salary(job):
   try:
       salary = job.xpath('//span[@class="css-19j1a75 eu4oa1w0"]/text()')
   except Exception as e:
       salary = 'Not available'
   if len(salary) == 0:
       try:
           salary = job.xpath('./descendant::div[@class="metadata salary-snippet-container"]/div/text()')
       except Exception as e:
           salary = 'Not available'
   else:
       salary = salary[0]
   return salary





# functions to extract job rating
def get_rating(job):
   try:
       rating = job.xpath('//span[@class="css-ppxtlp e1wnkr790"]/text()')
   except Exception as e:
       rating = 'Not available'
   return rating


# functions to extract job description
def get_job_desc(job):
   try:
       job_desc = job.xpath('./descendant::div[@class="job-snippet"]/ul/li/text()')
   except Exception as e:
       job_desc = ['Not available']
   if job_desc:
       job_desc = ",".join(job_desc)
   else:
       job_desc = 'Not available'
   return job_desc



with open('indeed_jobs1.csv', 'w', newline='', encoding='utf-8') as f:
    theWriter = writer(f)
    heading = ['job_link', 'job_title', 'company_name', 'company_location', 'salary', 'rating', 'job_description', 'searched_job', 'searched_location']
    theWriter.writerow(heading)
    all_jobs = []
    for page_no in range(0, 100, 10):
        url = paginaton_url.format(job_title, location , page_no)
        #page_dom = get_dom(url)
        jobs = dom.xpath('//div[@class="job_seen_beacon"]')
        all_jobs = all_jobs + jobs
    for job in all_jobs:
        job_link = base_url + get_job_link(job)
        time.sleep(1)
        job_title = get_job_title(job)
        time.sleep(1)
        company_name = get_company_name(job)
        time.sleep(1)
        company_location = get_company_location(job)
        time.sleep(1)
        salary = get_salary(job)
        time.sleep(1)
        rating = get_rating(job)
        time.sleep(1)
        job_desc = get_job_desc(job)
        time.sleep(1)
        record = [job_link, job_title, company_name, company_location, salary, rating, job_desc, job_title, location]
        theWriter.writerow(record)

# Closing the web browser
driver.quit()
   

    



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  