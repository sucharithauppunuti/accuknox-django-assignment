# accuknox-django-assignment

## Question 1
Django signals are synchronous by default.

Proof:
The signal handler contains time.sleep(5), and the request waits for signal completion before returning response.

## Question 2
Django signals run in the same thread as the caller.

Proof:
The thread IDs printed inside view and signal are identical.

## Question 3
Django signals run in the same database transaction by default.

Proof:
The object created inside transaction.atomic() is accessible inside the signal before transaction completion.

## Rectangle Class
The Rectangle class implements _iter_ and yields:
- {'length': value}
- {'width': value}

## Run Project

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start server:

python manage.py runserver
