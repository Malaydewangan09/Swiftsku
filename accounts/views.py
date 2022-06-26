from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import Customer
from .forms import OrderForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response


# def home(request):
# 	# orders = Order.objects.all()
# 	if request.method == 'GET':
# 		customers = Customer.objects.all()

# 		total_customers = customers.count()

# 	# total_orders = orders.count()
# 	# delivered = orders.filter(status='Delivered').count()
# 	# pending = orders.filter(status='Pending').count()

# 		context = {'customers':customers}

# 		return Response({'customers':customers})

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/api')
# 		context = {'form':form}
# 		return Response({'form':form})

# # def products(request):
# # 	products = Product.objects.all()

# # 	return render(request, 'accounts/products.html', {'products':products})

# # def customer(request, pk_test):
# # 	customer = Customer.objects.get(id=pk_test)

# # 	orders = customer.order_set.all()
# # 	order_count = orders.count()

# # 	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
# # 	return render(request, 'accounts/customer.html',context)

# @api_view(['POST'])
# def createOrder(request):
# 	form = OrderForm()
	
# 		#print('Printing POST:', request.POST)
# 	form = OrderForm(request.POST)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('/api')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)



# def updateOrder(request, pk):

# 	order = Customer.objects.get(id=pk)
# 	form = OrderForm(instance=order)

	
# 	form = OrderForm(request.POST, instance=order)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('/api')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# def deleteOrder(request, pk):
# 	order = Customer.objects.get(id=pk)
# 	order.delete()
	
	
# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)
# 	return redirect('/api')
class CustomerCreate(CreateView):
	model = Customer
	fields = ['name', 'email', 'phone']
	template_name = 'accounts/order_form.html'
	success_url = '/'
	

class CustomerList(ListView):
	model = Customer
	object_list= model.objects.all()
	template_name = 'accounts/customerl.html'

	
class Customerupdate(UpdateView):
	model = Customer
	fields = ['name', 'email', 'phone']
	template_name = 'accounts/order_form.html'
	success_url = '/'



class Customerdelete(DeleteView):
	model = Customer
	template_name = 'accounts/delete.html'
	success_url = '/'
