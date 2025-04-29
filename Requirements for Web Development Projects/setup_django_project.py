
import os

# Install required packages
os.system('pip install django djangorestframework requests')

# Ask for project name
project_name = input("Enter your Django project name: ")

# Create Django project
os.system(f'django-admin startproject {project_name}')

print("\nDjango project created successfully!")
print(f"Navigate to your project folder: cd {project_name}")
print("Run the server: python manage.py runserver")


