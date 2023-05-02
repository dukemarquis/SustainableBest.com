from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect

from .models import Sustainable_Products

@csrf_protect
class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "sus_product_list"

    def get_queryset(self):
        """ Get the latest list of all recommended sustainable product """
        return Sustainable_Products.objects.order_by("-created_date")


class RecommendResultView(generic.DetailView):
    model = Sustainable_Products
    context_object_name = "sus_product"
    template_name = "main/recommend_result.html"


class SusProductDetailView(generic.DetailView):
    model = Sustainable_Products

@csrf_protect
def recommend(request):
    sustainable_product = Sustainable_Products.objects.create(
                                                            product_image = request.FILES['sus_product_photo'],
                                                            product_name = request.POST['sus_product_name'],
                                                            recommend_reason = request.POST['recommend_reason'],
                                                            reference_link = request.POST['reference_link'])

    return HttpResponseRedirect(reverse("main:recommend_result", args=(sustainable_product.id,)))
