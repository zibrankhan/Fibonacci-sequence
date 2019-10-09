from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latency', models.CharField(blank=True, max_length=100, null=True)),
                ('numeric', models.PositiveIntegerField(blank=True, null=True)),
                ('output', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]