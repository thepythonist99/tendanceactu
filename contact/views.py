from django.shortcuts import render

from contact.forms import ContactForm

# Create your views here.


def contact_display(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

    return render(request, 'contact/contact_display.html', {'contact_form': contact_form})
