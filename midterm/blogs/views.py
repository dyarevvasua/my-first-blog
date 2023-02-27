from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        categories = Blog.objects.all()
        serializer = BlogSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_blog(pk):
    try:
        blog = Blog.objects.get(id=pk)
        return {
            'blog': blog,
            'status': 200
        }
    except Blog.DoesNotExist as e:
        return {
            'blog': None,
            'status': 404
        }

def get_blog(pk):
    try:
        todo_list = Blog.objects.get(id=pk)
        return {
            'blog': blog,
            'status': 200
        }
    except Blog.DoesNotExist as e:
        return {
            'todo_list': None,
            'status': 404
        }

@csrf_exempt
def blog_handler(request, pk):
    result = get_blog(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Blog not found'}, status=404)

    blog = result['blog']

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        blog.delete()
        return JsonResponse({'message': 'Blog successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


@csrf_exempt
def blog_handler(request, pk):
    result = get_blog(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Blog not found'}, status=404)

    todo_list = result['blog']

    if request.method == 'GET':
        blogs = blog.todo_set.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        data['blog_id'] = pk
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)

def get_blog(pk):
    try:
        blog = Blog.objects.get(id=pk)
        return {
            'status': 200,
            'blog': blog
        }
    except Blog.DoesNotExist as e:
        return {
            'status': 404,
            'blog': None
        }


@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        todos = Blog.objects.all()
        serializer = BlogSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

@csrf_exempt
def blog_handler(request, pk):
    result = get_blog(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Blog not found'}, status=404)

    todo = result['blog']

    if request.method == 'GET':
        serializer = BlogSerializer(todo)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors,safe=False, status=400)

    if request.method == 'DELETE':
        todo.delete()
        serializer = BlogSerializer(todo)
        return JsonResponse({'message': 'Todo was successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)
#



