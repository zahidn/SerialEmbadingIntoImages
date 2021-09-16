import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View



class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):

        return JsonResponse({'status': 'good'})


class Login(View):
    def get(self, request):
        return render(request, 'Register.html')

    def post(self, request):

        return JsonResponse({'status': 'good'})
