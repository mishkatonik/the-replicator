pages = [
	{
	'filename': 'content/index.html',
	'output': 'docs/index.html',
	'title': 'What\'s Cookin',
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


# GET TEMPLATE FUNCTION
def get_template():
	base_template = open('templates/base.html').read()
	return base_template

# COMPILE DOCS FUNCTION
def compile(i=0):
	page = pages[i]
	for page in pages:
		content = open(pages[i]['filename']).read()
		base_template = open('templates/base.html').read()
		fullpage = base_template.replace('{{content}}', content) + base_template.replace('{{title}}', pages[i]['title'])
		open(pages[i]['output'], "w+").write(fullpage)
		page = pages[i+1]

def main():
	get_template()
	compile()

# main()

if __name__ == "__main__":
	main()