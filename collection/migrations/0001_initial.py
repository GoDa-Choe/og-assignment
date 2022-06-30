# Generated by Django 4.0.5 on 2022-07-01 01:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', '남자'), ('W', '여자')], max_length=2)),
                ('birth', models.DateField(help_text='YYYY-MM-DD')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(help_text='010-0000-000', max_length=15, validators=[django.core.validators.RegexValidator(regex='(^01)\\d{1}-\\d{4}-\\d{4}')])),
                ('picture', models.ImageField(upload_to='artist/', verbose_name='image')),
                ('is_confirmed', models.CharField(choices=[('W', '대기'), ('C', '확인'), ('R', '거절')], default='W', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('price', models.PositiveBigIntegerField()),
                ('canvas_size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
                ('picture', models.ImageField(upload_to='artwork/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.artist')),
            ],
        ),
    ]
