from django.shortcuts import render, redirect
from .models import Oblast, City, House
from .forms import CreateCityForm, CreateHouseForm, CreateOblastForm


def home_page(request):
    if request.user.is_authenticated:
        oblasts = Oblast.objects.filter(owner_id=request.user.id)
        return render(request, 'blogs/index.html', {'oblasts': oblasts, 'user': request.user})
    else:
        return redirect('/auth/login/')


def create_oblast(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateOblastForm()
            return render(request, 'blogs/create-oblast.html', {'form': form})
        if request.method == 'POST':
            form = CreateOblastForm(request.POST)
            if form.is_valid():
                image = form.files.get('image')
                oblast = form.cleaned_data.get('oblast')
                Oblasts = Oblast(oblast=oblast, owner_id=request.user.id)
                Oblasts.save()
                return redirect('/')
            else:
                return render(request, 'blogs/create-oblast.html', {'form': form})
    else:
        return redirect('/auth/login/')


def oblast_details(request, pk):
    if request.user.is_authenticated:
        oblast = Oblast.objects.get(id=pk)
        cities = City.objects.filter(oblast_id=pk).order_by('-created_at')
        houses = House.objects.filter(oblast_id=pk).order_by
        form1 = CreateCityForm()
        form2 = CreateHouseForm()
        return render(request, 'blogs/oblast-details.html', {'oblast': oblast, 'cities': cities, 'houses': houses, 
                                                    'form1': form1, 'form2': form2})
    else:
        return redirect('/auth/login/')


def city_create(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateCityForm()
            return render(request, 'blogs/create-oblast.html', {'form': form})
        oblast = Oblast.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateCityForm(request.POST)
            if form.is_valid():
                city_name = form.data.get('city')
                city = City(city=city_name, oblast_id=pk)
                city.save()
                return redirect('/blogs/' + str(oblast.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def house_create(request, pk):
    if request.user.is_authenticated:
        oblast = Oblast.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateHouseForm(request.POST)
            if form.is_valid():
                address = form.data.get('address')
                region = form.data.get('region')
                street = form.data.get('street')
                flat = form.data.get('flat')

                house = House(address=address, region=region, street=street, flat=flat, oblast=oblast)
                house.save()
                return redirect('/blogs/' + str(oblast.id) + '/')
            else:
                return redirect('/')
        else:
            form = CreateHouseForm()
            return render(request, 'blogs/create-oblast.html', {'form': form})
    else:
        return redirect('/auth/login/')


def delete_oblast(request, pk):
    if request.user.is_authenticated:
        oblast = Oblast.objects.get(id=pk)
        if oblast.owner.id == request.user.id:
            oblast.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_house(request, pk):
    if request.user.is_authenticated:
        house = House.objects.get(id=pk)
        oblast = Oblast.objects.get(id=house.oblast.id)
        if oblast.owner.id == request.user.id:
            house.delete()
            return redirect('/blogs/' + str(oblast.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
