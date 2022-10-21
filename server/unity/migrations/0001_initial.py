# Generated by Django 4.1.2 on 2022-10-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscription_status', models.IntegerField(choices=[(1, 'Subscribed'), (0, 'Unsubscribed')], default=1)),
            ],
        ),
    ]