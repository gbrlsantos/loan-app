# Generated by Django 3.2.14 on 2022-07-06 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_rename_rate_table_ratetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('account_type_label', models.CharField(choices=[('CC', 'Conta Corrente'), ('CP', 'Conta Poupança')], default='CC', max_length=2)),
                ('account_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('desired_value', models.FloatField()),
                ('total_loan', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.client')),
                ('installment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.installment')),
            ],
        ),
    ]