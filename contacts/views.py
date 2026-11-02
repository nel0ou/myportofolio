from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from django.views.decorators.http import require_http_methods

from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    form = ContactForm()

    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts,
        'form': form
    })


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            if request.headers.get('HX-Request'):
                return render(request, 'contacts/contact_row.html', {
                    'contact': contact
                })

            return redirect('contacts:contact_list')

    else:
        form = ContactForm()

    contacts = Contact.objects.all()

    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts,
        'form': form
    })


def contact_search(request):
    query = request.GET.get('q', '')

    contacts = Contact.objects.filter(
        name__icontains=query
    ) if query else Contact.objects.all()

    return render(request, 'contacts/contact_rows.html', {
        'contacts': contacts
    })


@require_http_methods(["DELETE"])
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()

    return HttpResponse('')


def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    return render(request, 'contacts/contact_edit_row.html', {
        'contact': contact
    })


def contact_row(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    return render(request, 'contacts/contact_row.html', {
        'contact': contact
    })


@require_http_methods(["PUT"])
def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    data = QueryDict(request.body)

    contact.name = data.get('name', contact.name)
    contact.email = data.get('email', contact.email)
    contact.phone = data.get('phone', contact.phone)

    contact.save()

    return render(request, 'contacts/contact_row.html', {
        'contact': contact
    })