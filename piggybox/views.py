from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import DealForm, SignUpForm, WishlistForm
from .mixins import BudgetPerDayMixin, MonthCalendarMixin, MonthWithScheduleMixin
from .models import Deal, Wishlist

class DealCreate(CreateView):
    model = Deal
    form_class = DealForm
    success_url = reverse_lazy('piggybox:calendar')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DealCreate, self).form_valid(form)

class DealUpdate(UpdateView):
    model = Deal
    fields = ['date', 'in_out', 'category', 'summary']

class DealDelete(DeleteView):
    model = Deal
    success_url = reverse_lazy('piggybox:calendar')

class CalendarByUserView(LoginRequiredMixin, MonthWithScheduleMixin, TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    model = Deal
    template_name = 'piggybox/calendar.html'
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class SignUp(CreateView):
  form_class = SignUpForm
  template_name = "piggybox/signup.html" 
  success_url = reverse_lazy('piggybox:mypage')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    self.object = user 
    return HttpResponseRedirect(self.get_success_url())

class WishlistCreate(CreateView):
  model = Wishlist
  form_class = WishlistForm
  success_url = reverse_lazy('piggybox:mypage')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(DealCreate, self).form_valid(form)

class WishListView(LoginRequiredMixin, BudgetPerDayMixin, ListView):
  model = Wishlist
  template_name = "piggybox/mypage.html"

  def get_context_data(self):
    # コンテキストを取得するために, まずベースとなる実装を呼び出します
    context = super(WishListView, self).get_context_data()
    list_context = list(self.get_queryset().values())
    # 任意のデータを作成してコンテキストに追加します
    for wishlist in list_context:
      price = wishlist['price']
      target_date = wishlist['target_date']
      created_at = wishlist['created_at']

      wishlist['goal_days']   = (target_date-created_at).days
      wishlist['goal_weeks']  = int(wishlist['goal_days']/7)
      wishlist['goal_months'] = int(wishlist['goal_days']/28)
    
      wishlist['goal_per_day'] = int(price/wishlist['goal_days'])
      wishlist['goal_per_week'] = min(wishlist['goal_per_day']*7, price)
      wishlist['goal_per_month'] = min(wishlist['goal_per_day']*28, price)

    print(context)
    return context

  def get_queryset(self):
    return Wishlist.objects.all()

def index(request):
    return render(request, "piggybox/index.html")