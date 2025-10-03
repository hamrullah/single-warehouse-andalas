from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Category, UoM, Transaction
from .forms import ProductForm, CategoryForm, UoMForm, TransactionForm

# Product
class ProductList(LoginRequiredMixin, ListView): model = Product
class ProductCreate(LoginRequiredMixin, CreateView):
    model, form_class, success_url = Product, ProductForm, reverse_lazy("inventory:product-list")
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model, form_class, success_url = Product, ProductForm, reverse_lazy("inventory:product-list")
class ProductDelete(LoginRequiredMixin, DeleteView):
    model, success_url = Product, reverse_lazy("inventory:product-list")

# Category
class CategoryList(LoginRequiredMixin, ListView): model = Category
class CategoryCreate(LoginRequiredMixin, CreateView):
    model, form_class, success_url = Category, CategoryForm, reverse_lazy("inventory:category-list")
class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model, form_class, success_url = Category, CategoryForm, reverse_lazy("inventory:category-list")
class CategoryDelete(LoginRequiredMixin, DeleteView):
    model, success_url = Category, reverse_lazy("inventory:category-list")

# UoM
class UoMList(LoginRequiredMixin, ListView): model = UoM
class UoMCreate(LoginRequiredMixin, CreateView):
    model, form_class, success_url = UoM, UoMForm, reverse_lazy("inventory:uom-list")
class UoMUpdate(LoginRequiredMixin, UpdateView):
    model, form_class, success_url = UoM, UoMForm, reverse_lazy("inventory:uom-list")
class UoMDelete(LoginRequiredMixin, DeleteView):
    model, success_url = UoM, reverse_lazy("inventory:uom-list")

# Transaction
class TransactionList(LoginRequiredMixin, ListView): model = Transaction
class TransactionCreate(LoginRequiredMixin, CreateView):
    model, form_class, success_url = Transaction, TransactionForm, reverse_lazy("inventory:transaction-list")
class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model, form_class, success_url = Transaction, TransactionForm, reverse_lazy("inventory:transaction-list")
class TransactionDelete(LoginRequiredMixin, DeleteView):
    model, success_url = Transaction, reverse_lazy("inventory:transaction-list")
