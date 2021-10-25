from django.db import models
from django.utils import timezone
from django.urls import reverse

#어드민에서 보여지는 내용들

class Comment(models.Model):
    
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=20, help_text='ID', null=True, blank=False)

    date = models.DateTimeField(null=True, blank=False)

    content = models.TextField(max_length=1024, help_text='comment', null=True, blank=False)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name + " >>> " + self.content
    
    def get_name(self):
        return self.name
    
    def get_content(self):
        return self.content
    
    def get_date(self):
        return self.date

    def to_json(self):
        result = {}
        result["id"] = self.id
        result["date"] = self.date
        result["name"] = self.name
        result["content"] = self.content
        return result

