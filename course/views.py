from django.shortcuts import render
from .models import Course, Blog, Teacher, Pricing, Contact


def home(request):
    return render(request, 'index.html')


def course(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'course/course-grid-2.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'blog/blog.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog-single.html", context)


def teachers(request):
    teachers = Teacher.objects.all()
    context = {"teachers":teachers}
    return render(request, 'teachers/teachers.html', context)


def pricings(request):
    pricings = Pricing.objects.all()
    context = {"pricings":pricings}
    return render(request, 'pricing/pricing.html', context)


def contact(request):
    if request.method=="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        detail = request.POST["comments"]
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            detail=detail,
        )

    return render(request, 'contact/contact.html')
