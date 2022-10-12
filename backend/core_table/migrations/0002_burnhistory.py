# Generated by Django 3.2.6 on 2022-10-11 14:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core_table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BurnHistory',
            fields=[
                ('burnt_date', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('adjusted_user', models.CharField(max_length=42)),
                ('adjusted_amount', models.FloatField()),
                ('tx_hash', models.CharField(max_length=66)),
                ('adjusted_bar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='adjusted_bar', to='core_table.goldbar')),
                ('burnt_bar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='burnt_bar', to='core_table.goldbar')),
            ],
            options={
                'verbose_name': 'Burnt History',
                'verbose_name_plural': 'Burnts History',
            },
        ),
    ]
