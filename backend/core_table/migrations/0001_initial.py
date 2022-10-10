# Generated by Django 3.2.6 on 2022-10-07 17:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoldBar',
            fields=[
                ('escrow_date', models.DateField(auto_created=True, auto_now_add=True)),
                ('bar_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('warrant_number', models.CharField(max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Gold Bar',
                'verbose_name_plural': 'Gold Bars',
            },
        ),
        migrations.CreateModel(
            name='Mint',
            fields=[
                ('mint_date', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('burnt', models.BooleanField(default=False)),
                ('bar_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_table.goldbar')),
            ],
            options={
                'verbose_name': 'Mint',
                'verbose_name_plural': 'Mints',
            },
        ),
        migrations.CreateModel(
            name='Burn',
            fields=[
                ('burnt_date', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bar_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_table.goldbar')),
            ],
            options={
                'verbose_name': 'Burnt',
                'verbose_name_plural': 'Burnts',
            },
        ),
        migrations.CreateModel(
            name='BarHolder',
            fields=[
                ('holder_date', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('holder_xinfin_address', models.CharField(max_length=42)),
                ('token_balance', models.FloatField()),
                ('bar_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_table.goldbar')),
            ],
            options={
                'verbose_name': 'Bar Holder',
                'verbose_name_plural': 'Bar Holders',
            },
        ),
    ]
