from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('изображение', upload_to="advertisements/", null=True, blank=True)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold; ">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='обновлено')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold; ">Обновлено: {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/adv.png"

    @admin.display(description='изображение')
    def img_preview(self):
        return format_html(
            '<img src="{}" class="img-responsive thumbnail" alt="image" width="50%" height="50%">',
            self.get_photo_url
        )

    class Meta:
        db_table = 'advertisements'
