import jinja2
import glob
import os

all_content_files = glob.glob("content/*.html")

pages = []

def build_pages_dict():
	for file in all_content_files:
		file_name = os.path.basename(file)
		page_title, extension = os.path.splitext(file_name)
		pages.append({
			'input' : ('content/' + file_name), 
			'output' : ('docs/' + file_name),
			'title' : page_title,
		})

# Read in base template file
def get_template():
	base_template = open('templates/base.html').read()
	return base_template

# Read in content files
def get_content(page):
	content = open(page['input']).read()
	return content

# Compile the fullpage, which represents the fully rendered html webpage
def compile(page, base_template, content):
	jinja_template = jinja2.Template(base_template)
	fullpage = jinja_template.render(title=page['title'], content=content)
	return fullpage

# Indicate which page is active and set the corresponding button to active class
# after creating manage.py, this no longer populates active correctly...
def active_buttons(page, fullpage):
	if page['output'] == 'docs/The Replicator.html': 
		active_page = fullpage.replace('{{recipes_active}}', 'active')
	elif page['output'] == 'docs/About - The Food of Star Trek.html': 
		active_page = fullpage.replace('{{about_active}}', 'active')
	elif page['output'] == 'docs/Meet the Chef.html': 
		active_page = fullpage.replace('{{meet_the_chef_active}}', 'active')
	return active_page


# Put em all together
def main():
	build_pages_dict()
	for page in pages:
		base_template = get_template()
		content = get_content(page)
		fullpage = compile(page, base_template, content)
		active_page = active_buttons(page, fullpage)
		open(page['output'], "w+").write(active_page)