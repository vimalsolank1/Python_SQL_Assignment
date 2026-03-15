'''
2. Task 2 - html parser

a) Read the following html text in python as a string
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
b) Use BeautifulSoup package to print the following
i. All href links in the given html text
ii. All class values for <a> tags
iii. Extra points for also writing a recursive python code which is capable to parse the above html text
and give the output of point (i) and (ii) without using BeautifulSoup package
'''
html_text="""
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
# create parser soup object
soup = BeautifulSoup(html_text, "html.parser")

# b(i) All href links in the given html text
# find all anchor tags and print their href links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# b(ii) All class values for <a> tags
# find all <a> tags and print  class values
links = soup.find_all('a')
for link in links:
    print(link.get('class'))


'''b(iii).writing a recursive python code which is capable to parse the above html text 
give the output of point (i) and (ii) without using BeautifulSoup package'''


def parse_links(html_text, start_index=0):

    anchor_start = html_text.find("<a", start_index)

    if anchor_start == -1:
        return

    tag_close = html_text.find(">", anchor_start)

    anchor_tag = html_text[anchor_start:tag_close]

    # extract href link using string slicing 
    href_start = anchor_tag.find('href="') + 6
    href_end = anchor_tag.find('"', href_start)
    href_link = anchor_tag[href_start:href_end]

    # extract class name  using string slicing
    class_start = anchor_tag.find('class="') + 7
    class_end = anchor_tag.find('"', class_start)
    class_name = anchor_tag[class_start:class_end]

    print("href link :-", href_link)
    print("class  name:-", class_name)

    parse_links(html_text, tag_close)


parse_links(html_text)