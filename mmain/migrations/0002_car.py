# Generated by Django 5.2.1 on 2025-06-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Імя машини', max_length=20)),
                ('price', models.DecimalField(blank=True, decimal_places=5, max_digits=6)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='photo/')),
                ('owner', models.TextField(db_index=True, unique=True)),
                ('description', models.TextField(null=True, verbose_name='Опис')),
                ('updated', models.DateField(auto_now_add=True)),
                ('published', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машини',
                'db_table': 'db_Cars',
                'ordering': ['price'],
            },
        ),
    ]
