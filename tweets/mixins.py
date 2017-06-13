from django.forms.utils import ErrorList
from django import forms

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.user = self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
        return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserNeededMixin,self).form_valid(form)
        form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User not allowed to change this data."])
        return self.form_invalid(form)