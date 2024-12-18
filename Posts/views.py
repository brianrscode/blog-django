from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'Posts/posts_page.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'Posts/post.html', {'post': post})


def formulario(request):
    form = PostForm()  # crea el formulario
    if request.method == 'POST':  # si se envia el formulario
        form = PostForm(request.POST, request.FILES)  # Obtiene los datos del formulario
        if form.is_valid():  # si el formulario es valido
            form.save()  # guarda el formulario
            return redirect('home')  # redirige a la pagina de inicio
    return render(request, 'Posts/post_form.html', {'form': form})


def eliminar_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'eliminar_post.html', {'post': post})


def editar_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    update = 1
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        return redirect('home')
    return render(request, 'Posts/post_form.html', {'form': form, 'update': update})