import jinja2
import glob
import os

all_content_files = glob.glob("content/*.html")

pages = []

# Detect content files and store them as dict
def build_pages_dict():
	for content_file in all_content_files:
		file_name = os.path.basename(content_file)
		page_title, extension = os.path.splitext(file_name)
		pages.append({
			'input' : ('content/' + file_name), 
			'output' : ('docs/' + file_name),
			'basename' : file_name,
			'title' : page_title,
		})

# To be run in terminal to generate a new file with placeholder content
def new_content():
	new_file_name = input("Enter a name and ext for this file: ")
	new_file = open('content/' + new_file_name, 'w+')
	new_file.write('''
		<div>
			<h2>New Section<h2>
			<p>New stuff goes here!</p>
		</div>
		''')

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
	fullpage = jinja_template.render(pages=pages, title=page['title'], content=content)
	return fullpage

# Put em all together
def main():
	build_pages_dict()
	for page in pages:
		base_template = get_template()
		content = get_content(page)
		fullpage = compile(page, base_template, content)
		open(page['output'], "w+").write(fullpage)