from django.db import models

class Anime(models.Model):
    TITLE   = models.CharField(max_length = 100)
    DESCR   = models.CharField(max_length = 300)
    IMGPATH = models.CharField(max_length = 300)
    SHOWN   = models.BooleanField(default = False)

    def __str__(self) -> str:
        imgpath = self.IMGPATH[:12] + '...' if len(self.IMGPATH) > 15 else self.IMGPATH
        return f'{self.TITLE} at {imgpath}'
