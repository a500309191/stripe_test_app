# stripe-test-app
## Test task for a python developer vacancy.
The app is a store with a list of products available for purchase via STRIPE payment service.


task link: https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

### The app is written using DJANGO, DJANGO REST FRAMEWORK, REACT.

* deployed on heroku: https://a500-stripe-test-app.herokuapp.com/

* admmin page: https://a500-stripe-test-app.herokuapp.com/admin/
__login/password: admin__

### Local running instruction:

1. To copy git repository to the local machine, run:

```bash
git clone https://github.com/a500309191/stripe-test-app/blob/main/README.md
```
2. To install all requirements, run:

```bash
pip install requirements.txt
```

Create **.env** file in **core app folder**, add **STRIPE_API_KEY**. Information to get key: https://stripe.com/docs/keys

4. To start development server at http://127.0.0.1:8000/, run:

```bash
python manage.py runserver
```


* to populate database first items, run:
```bash
python manage.py loaddata first_data.json
````
* to create admin user, run:
```bash
python manage.py createsuperuser
```
