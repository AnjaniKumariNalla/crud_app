
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movies



def splash(request):
    return render(request, 'movieapp/splash.html')

def index(request):
    movies = Movies.objects.all()
    return render(request, 'movieapp/index.html', {'movies': movies})



def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        status = request.POST.get('status')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')
        image = request.FILES.get('image_url')

        if not title or not genre or not status or not release_year or not rating:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        movie = Movies.objects.create(
            title=title,
            genre=genre,
            status=status,
            release_year=int(release_year),
            rating=float(rating),
            image_url=image
        )

        count = Movies.objects.count()  
        return JsonResponse({'success': 'Movie added successfully!', 'count': count})

    return render(request, 'movieapp/add.html')

def edit_movie(request, id):
    movie = get_object_or_404(Movies, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        status = request.POST.get('status')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')
        image = request.FILES.get('image_url') 
        if not title or not genre or not status or not release_year or not rating:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        movie.title = title
        movie.genre = genre
        movie.status = status
        movie.release_year = int(release_year)
        movie.rating = float(rating)
        if image:
            movie.image_url = image
        # movie.image_url = image 
        movie.save()

        return JsonResponse({'success': 'Movie updated successfully!'})

    return render(request, 'movieapp/edit.html', {'movie': movie})



def delete_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    if request.method == 'POST':
        movie.delete()
        count = Movies.objects.count()
        return JsonResponse({'success': 'Movie deleted successfully!', 'count': count})
    return render(request, 'movieapp/delete.html', {'movie': movie})

