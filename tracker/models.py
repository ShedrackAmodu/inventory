from django.db import models

PRIORITY_CHOICES = [
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
]

class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('WORK', 'Work Task'),
        ('HABIT', 'Habit'),
        ('APPOINTMENT', 'Appointment'),
    ]

    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()}: {self.title} (Priority: {self.get_priority_display()})"
