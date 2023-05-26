from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

import requests

class Pharmacy(models.Model):
    name_of_pharmacy = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    pharmacy_email = models.CharField(max_length=100)
    pharmacy_phone_number = models.CharField(max_length=100)
    description_about_location = models.TextField()
   
    address_or_location = models.CharField(max_length=255)
    open_time = models.CharField(max_length=20 , default='8.00am - 8.00pm ')
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image_of_pharmacy = models.ImageField(upload_to='pharmacy-image', blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    stamped_application = models.ImageField(upload_to='pharm', blank=False)
    certificate_of_nationality_not_less_than_3_months = models.ImageField(upload_to='pharm', blank=False)
    certified_birth_certificate_not_less_than_3_months = models.ImageField(upload_to='pharm', blank=False)
    certified_copy_of_decorate_degree_in_pharmacy = models.ImageField(upload_to='pharm', blank=False)

    # def save(self, *args, **kwargs):
    #     # Generate and store latitude and longitude before saving the object
    #     if not self.latitude or not self.longitude:
    #         lat, lng = self.get_coordinates()
    #         self.latitude = lat
    #         self.longitude = lng
    #     super().save(*args, **kwargs)

    # def get_coordinates(self):
    #     # Use geocoding API to get coordinates based on address_or_location field
    #     address = self.address_or_location

    #     # Send a request to the Google Maps Geocoding API
    #     url = 'https://maps.googleapis.com/maps/api/geocode/json'
    #     params = {
    #         'address': address,
    #         'key': 'YOUR_API_KEY'  # Replace with your actual API key
    #     }
    #     response = requests.get(url, params=params)
    #     data = response.json()

    #     if data['status'] == 'OK':
    #         # Retrieve the latitude and longitude coordinates
    #         location = data['results'][0]['geometry']['location']
    #         latitude = location['lat']
    #         longitude = location['lng']
    #         return latitude, longitude
    #     else:
    #         # Handle error cases when geocoding is not successful
    #         return None, None

    def __str__(self):
        return self.name_of_pharmacy


    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Pharmacy'
        verbose_name_plural = 'Pharmacies'


class Drug(models.Model):
    name_of_drug = models.CharField(max_length=255)
    pharmacy = models.ManyToManyField(Pharmacy)
    description_of_drug = models.TextField()
    price = models.PositiveIntegerField()
    image_of_drug = models.ImageField(upload_to='drug-image')
    is_available = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.name_of_drug

    class Meta:
        verbose_name = 'Drug'
        verbose_name_plural = 'Drugs'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pharmacy = models.OneToOneField(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} ---------------------- > {self.pharmacy.name_of_pharmacy}'


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_of_event = models.ImageField(upload_to='event-image', blank=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        return self.name
    