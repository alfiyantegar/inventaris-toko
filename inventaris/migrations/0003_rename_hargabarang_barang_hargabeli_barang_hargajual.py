# Generated by Django 4.0.4 on 2022-06-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris', '0002_supplier_barang_idsupplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barang',
            old_name='hargaBarang',
            new_name='hargaBeli',
        ),
        migrations.AddField(
            model_name='barang',
            name='hargaJual',
            field=models.IntegerField(null=True),
        ),
    ]
