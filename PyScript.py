from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Load the HTML template
template = env.get_template('template.html')

# Define the dynamic content
data = {
    "title": "User Dashboard",
    "user_name": "John Doe",
    "items": ["Laptop", "Smartphone", "Headphones"]
}

# Render the template with the dynamic data
output = template.render(data)

# Save the rendered HTML to a file
with open("output.html", "w") as f:
    f.write(output)

print("HTML file has been generated: output.html")
