import pandas as pd
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Load the HTML template
template = env.get_template('template.html')

# Load data from the CSV file using Pandas
df = pd.read_csv('students2.csv')

# Process each student in the DataFrame
for _, row in df.iterrows():
    # Convert the comma-separated string of items into a list
    items = row['items'].split(',')

    # Render the template with dynamic data
    output = template.render(
        title=f"{row['username']}'s Dashboard",
        user_name=row['username'],
        items=items
    )

    # Save each student's HTML to a file
    filename = f"{row['username'].replace(' ', '_')}.html"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Generated HTML file: {filename}")
