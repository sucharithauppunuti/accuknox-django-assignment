import threading
import time

from django.db import transaction
from django.http import HttpResponse

from .models import DemoModel


# Question 1
def test_sync_signal(request):

    start = time.time()

    print("Creating object")

    DemoModel.objects.create(name="Sync Test")

    print("Object created")

    end = time.time()

    total = end - start

    return HttpResponse(
        f"Completed in {total:.2f} seconds"
    )


# Question 2
def test_thread_signal(request):

    print("Caller Thread ID:",
          threading.get_ident())

    DemoModel.objects.create(
        name="Thread Test"
    )

    return HttpResponse(
        "Thread Test Completed"
    )


# Question 3
def test_transaction_signal(request):

    try:

        with transaction.atomic():

            DemoModel.objects.create(
                name="Transaction Test"
            )

            print("Object created")

            raise Exception(
                "Force rollback"
            )

    except Exception:

        print("Transaction rolled back")

    return HttpResponse(
        "Transaction Test Completed"
    )