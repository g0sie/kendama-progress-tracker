from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import user_passes_test
from django.core.management import call_command


@user_passes_test(lambda u: u.is_superuser)
def add_tutorials(request, number: int):
    call_command('gettutorials', max=number)
    return HttpResponseRedirect(reverse('admin:tutorials_tutorial_changelist'))
