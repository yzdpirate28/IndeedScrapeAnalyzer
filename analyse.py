import csv
import matplotlib.pyplot as plt  # Import library for creating graphs



csv_file = open('indeed_jobs1.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file)

# Skip the header row
next(csv_reader)  # Discard the header row

# Analyze the data 
job_titles = []
company_names = []
company_locations = []
ratings = []
job_descriptions = []
searched_jobs = []
searched_locations = []

for row in csv_reader:
    job_title, company_name, company_location, rating, job_description, searched_job, searched_location = row[1:8]

    # Add data to respective lists
    job_titles.append(job_title)
    company_names.append(company_name)
    company_locations.append(company_location)
    ratings.append(rating)
    job_descriptions.append(job_description)
    searched_jobs.append(searched_job)
    searched_locations.append(searched_location)


# Count the number of jobs per company
company_job_count = {}
for company in company_names:
    if company in company_job_count:
        company_job_count[company] += 1
    else:
        company_job_count[company] = 1

# Find the most common job titles
from collections import Counter
job_title_counts = Counter(job_titles)
most_common_jobs = job_title_counts.most_common(10)  # Get top 10


# Print results 
print("Number of jobs per company:")
print(company_job_count)

print("\nTop 10 most common job titles:")
for title, count in most_common_jobs:
    print(f"{title}: {count}")


# close the CSV file after reading
csv_file.close()



# Prepare data for visualization 
company_job_counts = list(company_job_count.values())  # Extract job counts from dictionary
company_names = list(company_job_count.keys())  # Extract company names

# Create a bar chart for job counts per company
plt.figure(figsize=(10, 6))  # Set figure size
plt.bar(company_names, company_job_counts)
plt.xlabel("Company Name")
plt.ylabel("Number of Jobs")
plt.title("Job Distribution Across Companies")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping elements
plt.show()  # Display the bar chart




# Save the graph as a PNG image 
plt.savefig("job_distribution.png")








