from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Website


def index(request):
    return render(request, 'pingy/base.html')

@login_required
def user_panel_view(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        if address:
            Website.objects.create(
                owner=request.user,
                address=address,
                status='offline',
                last_checked=None
            )
        return redirect('user_panel')

    user_urls = Website.objects.filter(owner=request.user)
    return render(request, 'users/user_panel.html', {
        'user_urls': user_urls
    })

@login_required
def delete_url_view(request, site_id):
    site = get_object_or_404(Website, id=site_id, owner=request.user)
    site.delete()
    return redirect('user_panel')

