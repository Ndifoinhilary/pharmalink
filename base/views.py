from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from base.forms import ContactForm, DrugForm, PharmacyForm, StaffForm, UserForm
from . models import Pharmacy, Drug, Event, Staff
from django.urls import reverse
from django.db.models import Q


def home(request):
    return render(request, 'base/home.html')


def harmacy(request):
    pharm = Pharmacy.objects.all()[:5]
    context = {
        'pharm': pharm
    }
    return render(request, 'base/pharmacy.html', context)


def drugsearch(request):
    if request.method == 'GET':
        # Get the search query from the request
        search_query = request.GET.get('q')
        if search_query:
            drugs = Drug.objects.filter(
                name_of_drug__icontains=search_query, is_available=True)
            pharmacies = Pharmacy.objects.filter(
                drug__name_of_drug__icontains=search_query)
        else:
            drugs = Drug.objects.filter(is_available=True)[:10]
            pharmacies = Pharmacy.objects.none()
    else:
        drugs = Drug.objects.filter(is_available=True)[:10]
        pharmacies = Pharmacy.objects.none()

    context = {
        'drugs': drugs,
        'pharmacies': pharmacies,
    }
    return render(request, 'base/drugsearch.html', context)


def all_pharmacy(request):
    search_query = request.GET.get('q')
    
    if search_query:
        result = Q(name_of_pharmacy__icontains=search_query) | Q(
            address_or_location__icontains=search_query) | Q(description_about_location__icontains=search_query)
        pharmacies = Pharmacy.objects.filter(result)
    else:
        pharmacies = Pharmacy.objects.all()
    
    context = {
        'pharmacies': pharmacies,
        'search_query': search_query
    }
    return render(request, 'base/all-pharmacy.html', context)


def pharmacy_details(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy, id=pharmacy_id)
    # geting all drugs that belong to a particular pharmacy
    staff = pharmacy.staff
    all_drugs = pharmacy.drug_set.all()
    context = {
        'pharmacy': pharmacy,
        'all_drugs': all_drugs,
        'staff': staff
    }

    return render(request, 'base/pharmacy-details.html', context)


def register(request):
    if request.method == "POST":
        form = PharmacyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base-user-register')
    else:
        form = PharmacyForm()

    context = {
        'form': form
    }
    return render(request, 'base/register.html', context)


def drug_details(request, drug_id):
    drug_detail = get_object_or_404(Drug, id=drug_id)

    context = {
        'drug_detail': drug_detail
    }
    return render(request, 'base/drug-details.html', context)


def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        forms = StaffForm(request.POST)
        if form.is_valid() and forms.is_valid():
            form.save()
            forms.save()
            return redirect('base-login')
    else:
        form = UserForm()
        forms = StaffForm()
    context = {
        'form': form,
        'forms': forms
    }
    return render(request, 'base/user-register.html', context)


def add_drug(request):
    # Get the current user
    user = request.user

    # Retrieve the staff object associated with the user
    staff = Staff.objects.get(user=user)

    # Get the pharmacy associated with the staff
    pharmacy = staff.pharmacy

    if request.method == 'POST':
        form = DrugForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form with the pre-filled pharmacy
            drug = form.save(commit=False)
            drug.pharmacy = pharmacy  # Associate the drug with the pharmacy
            drug.save()
            return redirect('base-home')
    else:
        form = DrugForm(initial={'pharmacy': pharmacy})

    context = {
        'form': form,
    }
    return render(request, 'base/add.html', context)


def edit(request, edit_id):
    get_drug = get_object_or_404(Drug, id=edit_id)
    if request.method == "POST":
        form = DrugForm(request.POST, instance=get_drug)
        if form.is_valid():
            pharmacy_id = get_drug.pharmacy.first().id
            return redirect(reverse('base-pharmacy-details', kwargs={'pharmacy_id': pharmacy_id}))

    form = DrugForm(instance=get_drug)
    context = {
        'form': form
    }
    return render(request, 'base/add.html', context)


def event(request):
    return render(request, 'base/event.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base-home')
    else:
        form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'base/contact.html',context)