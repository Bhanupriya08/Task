from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class FibonnaciView(viewsets.ViewSet):

    def list(self, request):
        try:
            number = int(request.data['number'])
        except Exception as e:
            return Response({"error":"Send a valid number"})

        n1, n2 = 0, 1
        count = 0
        fibo_list = []
        if number <= 0:
            return Response({"error":"Please enter a positive integer"})
        elif number == 1:
            return Response({"Fibonacci sequence's last number :" : number})
        else:
            while count < number:
                fibo_list.append(n1)
                n1 , n2 = n2 ,n1+ n2
                count += 1
        print(fibo_list)
        return Response({"Fibonacci sequence's last number : ":fibo_list[-1]})

