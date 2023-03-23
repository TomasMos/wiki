from django.shortcuts import render
from markdown2 import Markdown
from . import util
from random import choice

def conversion(title):
    body = util.get_entry(title)
    if body == None:
        return body
    else:
        markdowner = Markdown()
        return markdowner.convert(body)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def NewPage(request):
    if request.method =="GET":
        return render(request, "encyclopedia/index.html", {
            "newpage": True
        })
    else:
        title = request.POST['title']
        body = request.POST['body']
        stock = util.get_entry(title)
        if stock is not None:
            return render(request, "encyclopedia/404.html", {
                "link": title
            })
        else:
            util.save_entry(title, body)
            return render(request, "encyclopedia/page.html", {
            "content": conversion(title),
            "title": title
            })

def title(request, title):
    content = conversion(title)
    if content == None:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/page.html", {
            "content": content,
            "title": title
        })

def search(request):
    if request.method == "POST":
        query = request.POST['q']
        content = conversion(query)
        if content is None:
            # get list of all entries
            E_list = util.list_entries()
            # loop over all entries and check if the query is a substring of each entry
            sub = []
            for entry in E_list:
                # save the list of matching entries
                if query.lower() in entry.lower():
                    sub.append(entry)
            # and display index by passing that dict
            return render(request, "encyclopedia/index.html", {
                            "entries": sub,
                            "search": True
                        })
        else:
            return render(request, "encyclopedia/page.html", {
                "content": content,
                "title": title
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['page_title']
        body = util.get_entry(title)
        print(title, body)
        return render(request, "encyclopedia/index.html", {
                "edit": True,
                "title": title,
                "content": body
            })

def save(request):
    title = request.POST['title']
    body = request.POST['body']
    print(title, body)
    util.save_entry(title, body)
    return render(request, "encyclopedia/page.html", {
    "content": conversion(title),
    "title": title
    })

def random(request):
    E_list = util.list_entries()
    rand = choice(E_list)
    return render(request, "encyclopedia/page.html", {
    "content": conversion(rand),
    "title": rand
    })






