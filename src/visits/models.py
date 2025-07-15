from django.db import models


class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primary key -> autofield -> 1,2,3,4,5,6....
    path = models.TextField(blank=True, null=True)  # column
    timestamp = models.DateTimeField(auto_now_add=True)  # column