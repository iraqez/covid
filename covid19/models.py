from django.db import models




class Rayon(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True, verbose_name='Район')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "район"
        verbose_name_plural = "райони"


class Nomenclature(models.Model): #номенклатура
    TP = (
        ('me', 'Медикаменти'),
        ('mo', 'Медичне обладнання')
    )
    groupNomenlature = models.CharField(max_length=2, choices=TP, default=None, verbose_name='Тип потреби')
    name = models.CharField(max_length=120, unique=True, blank=True, verbose_name='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Номенклатура"
        verbose_name_plural = "Номенклатури"


class Hospitals(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True, verbose_name='Назва мед. закладу')
    rayon = models.ForeignKey(Rayon, on_delete=models.PROTECT, verbose_name='Район')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "медичний заклад"
        verbose_name_plural = "медичні заклади"


class NomenclatureCount(models.Model):
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.PROTECT, verbose_name='Номенклатура')
    potreba = models.IntegerField(default=0, verbose_name='Потреба')
    nayavnist = models.IntegerField(default=0, verbose_name='Наявність')
    neobhidno = models.IntegerField(default=0, verbose_name='Необхідно',)
    hospital = models.ForeignKey(Hospitals, on_delete=models.PROTECT, verbose_name='Потреби')

    def save(self, *args, **kwargs):
        self.neobhidno = self.potreba - self.nayavnist
        super(NomenclatureCount, self).save(*args, **kwargs)

    


    def __str__(self):
        return self.nomenclature.groupNomenlature

    class Meta:
        verbose_name = "Потреби"
        verbose_name_plural = "Потреби"


class HelpPeople(models.Model): #медик, або волонтер
    pass


class BenefactorSupplier(models.Model): #постачальник або благодійник
    pass
