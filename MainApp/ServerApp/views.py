from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h3>Добро пожаловать на главную страницу сайта</h3>')
