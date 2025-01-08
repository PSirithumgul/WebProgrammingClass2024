import csv
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Load the HTML template
template = env.get_template('template.html')

# Load data from the CSV file
students = []
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert the comma-separated string of items into a list
        row['items'] = row['items'].split(',')
        students.append(row)

# Generate an HTML file for each student
for student in students:
    output = template.render(
        title=f"{student['username']}'s Dashboard",
        user_name=student['username'],
        items=student['items']
    )

    # Save each student's HTML to a file
    filename = f"{student['username'].replace(' ', '_')}.html"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Generated HTML file: {filename}")
