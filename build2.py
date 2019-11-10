def main():
	# templates
	top = open('templates/top.html').read()
	bottom = open('templates/bottom.html').read()

	# index
	content = open('content/index.html').read()

	index_html = top + content + bottom
	open('docs/index.html', 'w+').write(index_html)

	# about
	content = open('content/about.html').read()

	about_html = top + content + bottom
	open('docs/about.html', 'w+').write(about_html)

	# meet-the-chef
	content = open('content/meet-the-chef.html').read()

	meet_the_chef_html = top + content + bottom
	open('docs/meet-the-chef.html', 'w+').write(meet_the_chef_html)

pages = [
	{
	'filename': 'content/index.html',
	'output': 'docs/index.html',
	'title': 'The Replicator'
	},
	{
	'filename': 'content/about.html',
	'output': 'docs/about.html',
	'title': 'About - The Food of Star Trek'
	},
	{
	'filename': 'content/meet-the-chef.html',
	'output': 'docs/meet-the-chef.html',
	'title': 'Meet the Chef'
	}
]

for page in pages:
	content = open(page['filename']).read()
	fullpage = content + basetemplate
	open(page['output'], "w+").write(fullpage)






if __name__ == "__main__":
	main()