from django.shortcuts import render

def home(request):
  # Вывести все категории
  return render(request, "products/home.html")

