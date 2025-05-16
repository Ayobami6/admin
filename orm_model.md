Certainly! Here’s how you can transform the given SQL schema into a Django ORM model (since you mentioned Python, and unless otherwise specified, I’ll default to Django ORM):

```python
from django.db import models

class Utils(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # You can set max_length as needed
    ai_apikey = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'utils'
```

**Notes:**
- `id integer NOT NULL, PRIMARY KEY (id)`: In Django, `AutoField(primary_key=True)` is typically used for integer PKs.
- `name character varying NOT NULL`: Django's `CharField` is used; you must specify `max_length`. The value depends on your requirements or the maximum in your schema. Here, I set it to `255` as a common default.
- `ai_apikey character varying NOT NULL`: Same rationale as above.
- `created_at timestamp without time zone NULL`: `DateTimeField(null=True, blank=True)` in Django.

If you need the model in **SQLAlchemy**, let me know!