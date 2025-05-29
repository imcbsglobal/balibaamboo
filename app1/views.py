from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm  # Make sure this import is correct based on your project structure

def home(request):
    return render(request, 'index.html')

def gallery(request):
    images = [
        'main/resort1.jpg',
        'main/resort2.jpg',
        'main/resort3.jpg',
        'main/resort4.jpg',
        'main/resort5.jpg',
        # Add more images if needed
    ]
    
    description = (
        "Explore the serene beauty of our bamboo resort through our gallery. "
        "Experience the eco-friendly architecture, lush surroundings, and tranquil atmosphere "
        "that make Bali Bamboo a unique retreat. Each image captures the essence of sustainable living."
    )
    
    context = {
        'images': images,
        'description': description,
    }
    return render(request, 'gallery.html', context)

def properties(request):
    # Add properties data here later if needed
    return render(request, 'properties.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "New Contact Form Submission"
            body = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            Message: {form.cleaned_data['message']}
            """
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['your@email.com'],  # Replace with your actual destination email
                fail_silently=False
            )
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    return render(request, 'contact.html', {'form': form})

def rooms_view(request):
    return render(request, 'rooms.html')

def book(request):
    return render(request, 'book.html')





def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Optional: Print or log the data for testing
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")

        # Optional: Send an email (if configured)
        # send_mail(
        #     f'Contact Form Submission from {name}',
        #     f'Message: {message}\nPhone: {phone}',
        #     email,
        #     [settings.DEFAULT_FROM_EMAIL],
        # )

        return redirect('thank_you')  # Create a thank-you page later

    return render(request, 'contact.html')
def thank_you_view(request):
    return render(request, 'thank_you.html')


def about(request):
    return render(request, 'about.html')