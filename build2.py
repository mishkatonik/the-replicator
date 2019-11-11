pages = [
	{
	'filename': 'content/index.html',
	'output': 'docs/index.html',
	'title': 'The Replicator',
	},
	{
	'filename': 'content/about.html',
	'output': 'docs/about.html',
	'title': 'About - The Food of Star Trek',
	},
	{
	'filename': 'content/meet-the-chef.html',
	'output': 'docs/meet-the-chef.html',
	'title': 'Meet the Chef',
	}
]


# Read in base template file
def get_template():
	base_template = open('templates/base.html').read()
	return base_template

# Read in content files
def get_content():
	for page in pages:
		content = open(page['filename']).read()
	return content

# Compile the fullpage, which represents the fully rendered html webpage
def compile(base_template, content):
	for page in pages:
		fullpage = base_template.replace('{{content}}', content) # + base_template.replace('{{title}}', page['title'])
		open(page['output'], "w+").write(fullpage)
	# return fullpage

# Put em all together
def main():
	base_template = get_template()
	content = get_content()
	compile(base_template, content)

for page in pages:
	main()
	# get_template()
	# get_content()

if __name__ == "__main__":
	main()