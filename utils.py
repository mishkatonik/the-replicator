import jinja2
import glob
import os

all_content_files = glob.glob("content/*.html")

pages = []

def build_pages_dict():
	for content_file in all_content_files:
		file_name = os.path.basename(content_file)
		page_title, extension = os.path.splitext(file_name)
		pages.append({
			'input' : ('content/' + file_name), 
			'output' : ('docs/' + file_name),
			'basename' : file_name,
			'title' : page_title,
			'selected' : False,
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
	# for page in pages:
	# 	page['selected'] = False
	page['selected'] = True
	fullpage = jinja_template.render(pages=pages, title=page['title'], content=content)
	return fullpage

# Indicate which page is active and set the corresponding button to active class
# after creating manage.py, this no longer populates active correctly...
	# example of link loop to make active
		# {% for link in links %}
		# 	{% if link == selected_link %} 
		# 		'make active code...'
		# 	{% endif %}
		# {% endfor %}

		# selected_link = www.microsoft.com

# Put em all together
def main():
	build_pages_dict()
	for page in pages:
		page['selected'] = False
		base_template = get_template()
		content = get_content(page)
		fullpage = compile(page, base_template, content)
		# active_page = active_buttons(page, fullpage)
		open(page['output'], "w+").write(fullpage)		