from django.shortcuts import render, redirect, reverse, HttpResponse

def index( request ):
    return HttpResponse( "Successfully loaded simple:index")
