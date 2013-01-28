from django.db import models

class Redirect(models.Model):
    short_key = models.CharField(max_length='10')
    long_key = models.CharField(max_length='512')
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s -> %s' % (self.short_key, self.url)
