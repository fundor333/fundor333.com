---
title: 'Django Rest Framework: Multiple post'
date: 2019-04-23 10:00:00 +0000
feature_image: "api.gif"
tags:
- django
- rest
- post
- api
categories:
- dev
slug: django-rest-framework-multiple-post
description: How to make a massive put with Django Rest Framework

---
I need to have a massive **put** in my rest endpoint and Django Rest Framework doesn't do it. So I make my personal method for mycase.

## Setup fo the project

You need to follow the tutorial from the official documentation of [**Django Rest Framework**](https://www.django-rest-framework.org).

After this you have a _MyModel_, MyModelSerializer and a view class MyModelListPost.

## Why I can't use the default?

After you did the tutorial you have a base for a __standard__ Django Rest Framework. This mean that you have only a get massive not an update massive. So we make one from scratch.

## The __CODE__

This is the code for __massive put__. You need to map your classes and your fields for make this code working

{{< highlight python >}} 
# Code from https://fundor333.com

from rest_framework.response import Response 
from rest_framework.views i_port APIView 
from rest.models import MyModel_ 
from rest_framework import generics
from rest.serializer import MyModelSerializer

class MyModelListPost(generics.GenericAPIView, APIView): 
    queryset = MyModel.objects.all() 
    serializer_class = MyModelSerializer

    def put(self, request, *args, **kwargs):
        output = []
        for data in request.data:
            try:
                instance = MyModel.objects.get(unique_id=data["unique_id"])
                created = False
            except Exception:
                instance = MyModel.objects.create(
                    field1=data["field1"],
                    field2=data["field2"],
                )
                created = True
    
            if created:
                serializer = self.get_serializer(data=data)
            else:
                serializer = self.get_serializer(instance, data=data)
            if serializer.is_valid():
                serializer.save()
                output.append(serializer.data)
            else:
                output.append(serializer._errors)
        return Response(output, status=status.HTTP_200_OK)

{{< / highlight >}}

In this case we use the __unique_id__ to find any instance and update one by one with the __get__ method. 
I know it's not very Python Way but if you have some better solution please write below. Thanks
