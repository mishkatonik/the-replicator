pages = [
	{
	'filename': 'content/index.html',
	'output': 'docs/index.html',
	'title': 'What\'s Cookin',
	},
	{
	'filename': 'content/about.html',
	'output': 'docs/about.html',
	'title': '<h2>ABOUT The Food of <em>Star Trek</em></h2>',
	},
	{
	'filename': 'content/meet-the-chef.html',
	'output': 'docs/meet-the-chef.html',
	'title': 'Meet the Chef',
	}
]

# Read in base template file
def get_template():
	for page in pages:
		base_template = open('templates/base.html').read()
	return base_template

# Read in content files
def get_content():
	for page in pages:
		content = open(page['filename']).read()
	return content

# Compile the fullpage, which represents the fully rendered html webpage
def compile():
	for page in pages:
		fullpage = base_template.replace('{{content}}', content) + base_template.replace('{{title}}', page['title'])
		open(page['output'], "w+").write(fullpage)


# Put em all together
def main():
	get_template()
	get_content()
	compile()

main()

if __name__ == "__main__":
	main()