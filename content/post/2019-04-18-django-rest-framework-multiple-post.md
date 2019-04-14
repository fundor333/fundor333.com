---
title: 'Django Rest Framework: Multiple post'
date: 2019-04-05T10:00:00Z
draft: false
feature_image: /images/uploads/octocat.png
tags:
  - django
  - rest
  - post
categories:
  - dev
slug: django-rest-framework-multiple-post
description: How to make a massive put with Django Rest Framework
---

I need to have a massive __put__ in my rest endpoint and Django Rest Framework doesn't do it. So I make my personal method for mycase.

# Setup fo the project

You need to follow the tutorial from the official documentation of __[Django Rest Framework](https://www.django-rest-framework.org)__.

After this you have a _MyModel_, 



{{< highlight python >}}
from rest_framework.response import Response
from rest_framework.views import APIView
from rest.models import MyModel
from rest.serializer import MyModelSerializer


class MyModelListPost(generics.GenericAPIView, APIView):
	queryset = MyModel.objects.all()
	serializer_class = MyModelSerializer

	def put(self, request, *args, **kwargs):
		output = []
		log.error("put")
		log.error(str(request.data))
		for data in request.data:
			try:
				instance = MyModel.objects.get(unique_id=data["unique_id"])
				created = False
			except Exception:
				instance = MyModel.objects.create(
					codice_MyModel=data["codice_MyModel"],
					codice_tratta=data["codice_tratta"],
					data_partenza=data["data_partenza"][:4]
					+ "-"
					+ data["data_partenza"][4:6]
					+ "-"
					+ data["data_partenza"][6:],
					ora_partenza=data["ora_partenza"][:2]
					+ ":"
					+ data["ora_partenza"][2:],
					codici_lingua=data["codici_lingua"],
					meeting_point=data["meeting_point"],
					stato=data["stato"],
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
