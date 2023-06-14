from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util

def md_to_html(title):
    converter = Markdown()
    fileList = util.list_entries()
    if title in fileList:
        content = util.get_entry(title)
        return converter.convert(content)
    else:
        return None

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = md_to_html(title)
    if html_content is not None:
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "text":"File not founded"
        })
    
def edit(request):
    if request.method =="POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request,"encyclopedia/edit.html",{
            "title":title,
            "content":content
        })
    
def save_edit(request):
    if request.method =="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_content = util.get_entry(title)
        return render(request, "encyclopedia/entry.html", {
                "title":title,
                "content": html_content
            })
        
def create_new(request):
    if request.method=="GET":
        return render(request, "encyclopedia/new.html")
    else:
        title =request.POST["title"]
        content =request.POST["content"]
        file_list = [item.lower() for item in util.list_entries()]
        print(file_list)
        if title.lower() not in file_list:
            util.save_entry(title, content)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":content
            })
        else:
             return render(request, "encyclopedia/error.html", {
            "text":"File already exist"
        })

def search(request):
    file_list = util.list_entries()
    if request.method=="POST":
        search_value = request.POST["q"]
        new_list = []
        for i in file_list:
            if i.lower()== search_value.lower() or search_value.lower() in i.lower():
                new_list.append(i)
    return render(request,"encyclopedia/index.html",{
        "entries":new_list
    })

def rand_page(request):
    file_list = util.list_entries()
    title = random.choice(file_list)
    content = util.get_entry(title)
    return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":content
        })




