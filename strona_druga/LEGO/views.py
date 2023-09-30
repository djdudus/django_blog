from django.shortcuts import render
from django.db.models import Sum
from .models import Set, Brick, SetBricks
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .legocalc import get_set_parts, get_brick_info
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
import re


# Create your views here.
@login_required
def lego(request):  # sourcery skip: use-contextlib-suppress
    if request.method == "POST":
        set_number = request.POST.get("input_value")
        get_set_parts(set_number)
        messages.success(request, "Set info collected.")
        set_info, brick_info = get_set_parts(set_number)
        set_number = set_info["data"]["item"]["no"]
        min_price = set_info["data"]["min_price"]
        avg_price = set_info["data"]["avg_price"]
        max_price = set_info["data"]["max_price"]

        set1, created = Set.objects.get_or_create(
            set_number=set_number,
            defaults={
                "min_price": min_price,
                "avg_price": avg_price,
                "max_price": max_price,
                "brickprice": 0,
            },
        )

        for entry in brick_info["data"]:
            (
                brick_number,
                color_id,
                category_id,
                brick_type,
                quantity,
                bmin_price,
                bavg_price,
                bmax_price,
                notes,
            ) = get_brick_info(entry)
            if brick_type == "INSTRUCTION":
                continue  # Skip the entry

            brick_obj, created = Brick.objects.get_or_create(
                brick_number=str(brick_number),
                color_id=color_id,
                defaults={
                    "category_id": category_id,
                    "type": brick_type,
                    "min_price": bmin_price,
                    "avg_price": bavg_price,
                    "max_price": bmax_price,
                    "notes": notes,
                },
            )
            brick_obj.save()

            set_brick, created = SetBricks.objects.get_or_create(
                set_number=set1,
                brick_number=brick_obj,
                type=brick_type,
                defaults={"quantity": quantity},
            )
            set_brick.save()
            temp_brickprice = SetBricks.objects.filter(set_number=set1).aggregate(
                sum=Sum("brick_number__avg_price")
            )
            set1.brickprice = temp_brickprice["sum"]
            set1.save()
    context = {"sets": Set.objects.all(), "title": "Kalkulator Lego"}
    return render(request, "lego.html", context)


class SetDetailView(LoginRequiredMixin, DetailView):
    model = Set
    fields = ["set_number", "avg_price"]


# def check_brick_existence(brick):
#     print(brick.brick_number)
