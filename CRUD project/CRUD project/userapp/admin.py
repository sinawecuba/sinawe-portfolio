from django.contrib import admin
from .models import User  # Import the User model from this app

# Register the User model to make it appear in the admin site
admin.site.register(User)
