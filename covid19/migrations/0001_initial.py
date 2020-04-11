# Generated by Django 3.0.5 on 2020-04-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BenefactorSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HelpPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupNomenlature', models.CharField(choices=[('me', 'Медикаменти'), ('mo', 'Медичне обладнання')], default=None, max_length=2, verbose_name='Тип потреби')),
                ('name', models.CharField(blank=True, max_length=120, unique=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Номенклатури',
            },
        ),
        migrations.CreateModel(
            name='Rayon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, unique=True, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'район',
                'verbose_name_plural': 'райони',
            },
        ),
        migrations.CreateModel(
            name='NomenclatureCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potreba', models.IntegerField(default=0, verbose_name='Потреба')),
                ('nayavnist', models.IntegerField(default=0, verbose_name='Потреба')),
                ('neobhidno', models.IntegerField(default=0, verbose_name='Необхідно')),
                ('nomenclature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='covid19.Nomenclature', verbose_name='Номенклатура')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, unique=True, verbose_name='Назва мед. закладу')),
                ('NomenclatureCount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='covid19.NomenclatureCount', verbose_name='Потреби')),
                ('rayon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='covid19.Rayon', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'медичний заклад',
                'verbose_name_plural': 'медичні заклади',
            },
        ),
    ]