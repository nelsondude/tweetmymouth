from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q

# Create your views here.
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            if new_tweet:
                return HttpResponseRedirect(new_tweet.get_absolute_url())
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    # queryset = Tweet.objects.all()
    # model or queryset
    model = Tweet
    success_url = reverse_lazy('tweet:list')
    template_name = "tweets/delete_confirm.html"


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    form_class = TweetModelForm
    # success_url = "/tweet/"
    template_name = "tweets/update_view.html"
    queryset = Tweet.objects.all()


class TweetCreateView(FormUserNeededMixin, CreateView): #LoginRequiredMixin, 
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = "/tweet/create/"

    # login_url = '/admin/'
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(TweetCreateView, self).form_valid(form)

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    # queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query) #complex lookups
                )


        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        # context["another thing"] = 42
        return context




##################################################################
def tweet_detail_view(request,pk=None):

    obj = Tweet.objects.get(pk=pk) #GET object
    context = {
        'object': obj,


    }
    return render(request, "tweets/detail_view.html",context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        'object_list': queryset,


    }
    return render(request, "tweets/list_view.html",context)


