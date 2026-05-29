# Accuknox Django Trainee Assignment

## Candidate Details
Name: Sucharitha

---

# Project Overview

This project contains solutions for the Accuknox Django Trainee Assignment.

The assignment includes:

1. Django Signals
2. Custom Python Rectangle Class

The project demonstrates:
- synchronous execution of Django signals
- signal execution thread behavior
- database transaction behavior of signals
- iterable custom Rectangle class implementation

---

# Requirements

- Python 3
- Django

---

# Installation Steps

## Step 1: Create Virtual Environment
```bash
python -m venv venv
Step 2: Activate Virtual Environment
Step 3: Install Dependencies
pip install -r requirements.txt
Run Migrations
python manage.py migrate
Run Server
python manage.py runserver
Django Signals Assignment

# Question 1
By default are Django signals executed synchronously or asynchronously?
Answer -> Django signals are executed synchronously by default.

Proof

A delay using time.sleep(5) is added inside the signal handler.

The execution waits for the signal to complete before moving to the next statement.

Example Output
Before save
Signal started
Signal completed
After save

Since After save is printed only after the signal completes, it proves signals execute synchronously.

#Question 2
Do Django signals run in the same thread as the caller?
Answer -> Yes, Django signals run in the same thread as the caller by default.

Proof

The thread ID is printed:

inside the caller function
inside the signal handler

using:

threading.get_ident()
Example Output
Caller Thread ID: 12345
Signal Thread ID: 12345

Both thread IDs are identical, proving signals execute in the same thread.

#Question 3
By default do Django signals run in the same database transaction as the caller?
Answer -> Yes, Django signals run in the same database transaction as the caller by default.

Proof

A database operation is wrapped inside:

transaction.atomic()

An exception is raised after saving the object.

If both:

the model data
the signal-created data

are rolled back together, it proves they share the same transaction.

Example Output
DemoModel count: 0
SignalLog count: 0

This confirms that both operations were rolled back together within the same transaction.

# Custom Rectangle Class
Description

A custom Rectangle class is implemented with:

length
width

The class supports iteration.

When iterated:

length is returned first
width is returned second

#Conclusion

This project successfully demonstrates:

1.synchronous behavior of Django signals
2.same-thread execution of signals
3.transaction behavior of signals
4.custom Rectangle class implementation