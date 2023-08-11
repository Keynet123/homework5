#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Домашка по 4 занятию")
