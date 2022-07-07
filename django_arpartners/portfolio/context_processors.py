from .models import Contact


def add_contact(request):
    contact_info = Contact.objects.all()
    return {
        "contact_info": contact_info,
    }
