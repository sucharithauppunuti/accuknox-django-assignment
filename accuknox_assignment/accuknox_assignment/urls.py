from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from signals_app.views import (
    test_sync_signal,
    test_thread_signal,
    test_transaction_signal,
)

def home(request):
    return HttpResponse(
        "Django Assignment Running Successfully"
    )

urlpatterns = [

    path('', home),

    path('admin/', admin.site.urls),

    path('sync-test/', test_sync_signal),

    path('thread-test/', test_thread_signal),

    path('transaction-test/', test_transaction_signal),
]