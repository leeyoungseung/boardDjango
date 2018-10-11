from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BoardForm, UserCreateForm
from django.views.generic import ListView, TemplateView
from .models import Board
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from django.template.loader import get_template


def create_user(request):
	if request.method == 'POST':
		user = authenticate(email=request.POST['email'], password=request.POST['password1'])
		if user == 0:
			return render(request, 'registration/signup_done.html', {'message': '회원이 이미 있음'})
		else:
			email = request.POST['email']
			password = request.POST['password1']
			username = request.POST['username']
			# first_name = request.POST['first_name']
			# last_name = request.POST['last_name']
			new_user = User.objects.create_user(username, password, email)
			new_user.save()
		return render(request, 'registration/signup_done.html', {'message': '회원가입이 완료됨'})
	else:
		form = UserCreateForm()
	return render(request, 'registration/signup.html', {'form': form})


# Create your views here.
class MainPageLV(ListView):
	model = Board
	template_name = 'board/mainPage.html'
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(MainPageLV, self).get_context_data(**kwargs)
		list_all = Board.objects.all()
		paginator = Paginator(list_all, self.paginate_by)

		page = self.request.GET.get('page')
		try :
			list_paged = paginator.page(page)
		except PageNotAnInteger :
			list_paged = paginator.page(1)
		except EmptyPage :
			list_paged = paginator.page(paginator.num_pages)
		#
		context['board_list'] = list_paged
		return context


# Create your views here.
def delete(request, b_id):
	board = get_object_or_404(Board, pk=b_id)
	if request.method == 'POST':
		inputedPW = request.POST['b_passwd']
		if inputedPW == board.b_passwd:
			board.delete()
			return redirect('/board/')
	return render(request, 'board/delete.html',{'board': board})


def update(request, b_id):
	board = get_object_or_404(Board, pk=b_id)
	if request.method == 'POST':
		form = BoardForm(request.POST, instance=board)
		if form.is_valid():
			board = form.save()
			return render(request, 'board/detail.html', {'board': board})
	else :
		form = BoardForm(instance=board)
		pk = board.b_id
		return render(request, 'board/update.html', {'form': form, 'b_id': pk})


def detail(request, b_id):
	board = get_object_or_404(Board, pk=b_id)
	if request.method == 'GET':
		return render(request, 'board/detail.html', {'board': board})


def create_new(request):
	if request.method == 'POST':
		form = BoardForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/board/')
	else:
		form = BoardForm()
	return render(request,'board/create_new.html',{'form':form})

# def mainPage(request):
# 	record1 = {'no':1,'title':'hello1','writer':'mina','time':'2018-08-21','count':2}
# 	record2 = {'no':2,'title':'hello2','writer':'momo','time':'2018-08-22','count':3}
# 	record3 = {'no':3,'title':'hello3','writer':'sana','time':'2018-08-23','count':5}
# 	record4 = {'no':4,'title':'hello4','writer':'jihyo','time':'2018-08-24','count':7}
# 	records = (record1,record2,record3,record4)
# 	return render(request, "board/mainPage.html", {"records":records})
