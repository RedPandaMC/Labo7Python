# Labo7Python

This repository has a basic tool to create static websites. You can use a markdown document from the '_input-markdown-document-here' folder to generate web pages with the help of the main.py code. There are two templates to choose from, called "earth" and "sky", that come with three different types of web pages each. This makes it easy to create good-looking static websites with little effort.

The include pages in each template:
- homepage
- post
- aboutme

you can add as many of these pages as you want in the "_site" directory, which will also be generated on first use

Instructions for using the markdown document.


```
---
Date: -> when writing a post you should put a date here, otherwise just put a random value here
Title: -> the title of the generated html page document
Author: -> when writing a post you should put a name here, otherwise just put a random value here
TemplateName: -> the template you want to use
PageType: -> the html page you want to use from the template you chose above
---

markdown goes here
```

A handy guid can be found here
https://www.markdownguide.org/basic-syntax
