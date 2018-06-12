from django.shortcuts import render, get_object_or_404

from blog.models import Entry

# Create your views here.


def blog_entries(request):
    entries = Entry.get_top_entries()
    entries_length = len(entries)

    return render(request, 'blog/blog_entries.html',
                  {'entries': entries, 'length': entries_length})


def entry_detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)

    return render(request, 'blog/entry_detail.html', {'entry': entry})
