# Generated by Django 3.2.25 on 2025-03-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='acounts')),
                ('password', models.CharField(max_length=500, verbose_name='password')),
                ('email', models.CharField(max_length=254, verbose_name='email')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('phone', models.CharField(max_length=20, verbose_name='tel')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('is_active', models.IntegerField(choices=[(0, '否'), (1, '是')], default=True, verbose_name='是否激活')),
            ],
        ),
    ]
