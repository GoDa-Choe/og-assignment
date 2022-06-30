from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=16)
    gender = models.CharField(max_length=2, choices=(('M', '남자'), ('W', '여자')))
    birth = models.DateField(help_text="YYYY-MM-DD")
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,
                                    validators=[RegexValidator(regex=r'(^01)\d{1}-\d{4}-\d{4}')],
                                    help_text="010-0000-000")

    picture = models.ImageField('image', upload_to='artist/')

    is_confirmed = models.CharField(max_length=2, default='W', choices=(('W', '대기'), ('C', '확인'), ('R', '거절')))

    # ForeignKey
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Artwork(models.Model):
    title = models.CharField(max_length=64)
    price = models.PositiveBigIntegerField()
    canvas_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    picture = models.ImageField(upload_to='artwork/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ForeignKey
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_price(self):
        return str(format(self.price, ","))
