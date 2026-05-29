import threading
import time

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DemoModel, SignalLog


@receiver(post_save, sender=DemoModel)
def demo_signal(sender, instance, created, **kwargs):

    print("\nSIGNAL STARTED")

    print("Signal Thread ID:", threading.get_ident())

    time.sleep(5)

    SignalLog.objects.create(
        message="Signal executed"
    )

    print("SIGNAL FINISHED\n")