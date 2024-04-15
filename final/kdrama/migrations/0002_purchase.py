# Generated by Django 5.0.1 on 2024-04-15 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kdrama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('kdrama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kdrama.kdrama')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kdrama.user')),
            ],
        ),
    ]
