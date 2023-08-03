from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Title
# Description
# Price
# Negotiable
# Created
# Last Updated

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    negotiable = models.BooleanField("Торг", help_text="Уместен ли торг?")
    created = models.DateTimeField("Созданo", auto_now_add=True)
    last_updated = models.DateTimeField("Обновленo", auto_now=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.pk}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisements"

    @admin.display(description="Создано")
    def created_date(self):
        from django.utils import timezone
        if self.created.date() == timezone.now().date():
            created_time = self.created.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        else:
            return format_html(
                '<span style="color: darkgreen; font-weight: bold">{}</span>', 
                f"{self.created.date().strftime('%d.%m.%Y')} в {self.created.time().strftime('%H:%M:%S')}"
            )
        
    @admin.display(description="Обновлено")
    def last_updated_date(self):
        from django.utils import timezone
        if self.last_updated.date() == timezone.now().date():
            last_updated_time = self.last_updated.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: gold; font-weight: bold">Сегодня в {}</span>', last_updated_time
            )
        else:
            return format_html(
                '<span style="color: goldenrod; font-weight: bold">{}</span>', 
                f"{self.last_updated.date().strftime('%d.%m.%Y')} в {self.last_updated.time().strftime('%H:%M:%S')}"
            )
