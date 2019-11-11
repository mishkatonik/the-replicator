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

# So when I put the return as indented and part of the for loop, it only gives the first page.
# When its not indented, it only returns the last page. Why?


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
		fullpage = base_template.replace('{{content}}', content).replace('{{title}}', page['title'])
		# open(page['output'], "w+").write(fullpage)
		return fullpage

# Put em all together
def main():
	for page in pages:
		base_template = get_template()
		content = get_content()
		fullpage = compile(base_template, content)
		open(page['output'], "w+").write(fullpage)


# for page in pages:
main()
	

	# get_template()
	# get_content()

if __name__ == "__main__":
	main()