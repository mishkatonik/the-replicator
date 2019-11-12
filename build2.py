pages = [
	{
	'filename': 'content/index.html',
	'output': 'docs/index.html',
	'title': 'The Replicator',
	# 'is_active': '{{recipes_active}}',
	},
	{
	'filename': 'content/about.html',
	'output': 'docs/about.html',
	'title': 'About - The Food of Star Trek',
	# 'is_active': '{{about_active}}',
	},
	{
	'filename': 'content/meet-the-chef.html',
	'output': 'docs/meet-the-chef.html',
	'title': 'Meet the Chef',
	# 'is_active': '{{meet_the_chef_active}}',
	}
]


# Read in base template file
def get_template():
	base_template = open('templates/base.html').read()
	return base_template

# Read in content files
def get_content(page):
	content = open(page['filename']).read()
	return content

# Compile the fullpage, which represents the fully rendered html webpage
def compile(page, base_template, content):
	fullpage = base_template.replace('{{content}}', content).replace('{{title}}', page['title'])
	return fullpage

# Indicate which page is active and set the corresponding button to active class
	# there's gotta be a better way to do this...
def active_buttons(page, fullpage):
	if page['output'] == 'docs/index.html': 
		actvive_page = fullpage.replace('{{recipes_active}}', 'active')
	elif page['output'] == 'docs/about.html': 
		actvive_page = fullpage.replace('{{about_active}}', 'active')
	elif page['output'] == 'docs/meet-the-chef.html': 
		actvive_page = fullpage.replace('{{meet_the_chef_active}}', 'active')
	return actvive_page


# Put em all together
def main():
	for page in pages:
		base_template = get_template()
		content = get_content(page)
		fullpage = compile(page, base_template, content)
		active_page = active_buttons(page, fullpage)
		open(page['output'], "w+").write(active_page)

if __name__ == "__main__":
	main()