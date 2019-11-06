# templates
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

# index
content = open('content/index.html').read()

index_html = top + content + bottom
open('docs/index.html', 'w+').write(index_html)

# blog
content = open('content/blog.html').read()

blog_html = top + content + bottom
open('docs/blog.html', 'w+').write(blog_html)

# meet-the-chef
content = open('content/meet-the-chef.html').read()

meet_the_chef_html = top + content + bottom
open('docs/meet-the-chef.html', 'w+').write(meet_the_chef_html)