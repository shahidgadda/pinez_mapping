from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView, TemplateView
from account.views import SignupView, LoginView, LogoutView, DeleteView
from account.views import ConfirmEmailView
from account.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
from account.views import SettingsView
from machine.models import Gadgets

urlpatterns = patterns(
    "",
    url(r'^$', ListView.as_view(queryset=Gadgets.objects.all()[:6],
                                template_name="account/index.html")),
    url(r'^laptop/$',  ListView.as_view(queryset=Gadgets.objects.all(),
                                template_name="account/laptop.html")),
    url(r'^tablet/$', ListView.as_view(queryset=Gadgets.objects.all(),
                                template_name="account/tablet.html")),
    url(r'^monitor/$', ListView.as_view(queryset=Gadgets.objects.all(),
                                template_name="account/monitor.html")),
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^login/$", LoginView.as_view(), name="account_login"),
    url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    url(r"^delete/$", DeleteView.as_view(), name="account_delete"),
)
