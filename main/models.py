from django.db import models


class Data(models.Model):
    choices = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    ]
    # choices = [('M', "Male"), ('F', "Female")]
    name = models.CharField(max_length=255, blank=True, choices=choices)
