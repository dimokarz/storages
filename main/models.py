from django.db import models


class Controllers(models.Model):
    class Meta:
        verbose_name = 'Контроллер'
        verbose_name_plural = 'Контроллеры'

    contr_name = models.CharField(max_length=50, verbose_name='Название')
    contr_addr = models.CharField(max_length=14, verbose_name='Адрес')
    contr_passwd = models.CharField(max_length=10, verbose_name='Пароль')

    def __str__(self):
        return self.contr_name


class OneWire(models.Model):
    class Meta:
        verbose_name = 'Температуру'
        verbose_name_plural = 'Температура'

    onewire_contr = models.ForeignKey(Controllers, on_delete=models.CASCADE, verbose_name='Контроллер')
    onewire_time = models.DateTimeField(auto_now=True, verbose_name='Дата\Время')
    onewire_name = models.CharField(max_length=50, verbose_name='Название')
    onewire_value = models.FloatField(verbose_name='Температура')
    onewire_channel = models.CharField(max_length=1, verbose_name='Канал', default='A')

    def __str__(self):
        return self.onewire_name


class Rele(models.Model):
    class Meta:
        verbose_name = 'Реле'
        verbose_name_plural = 'Реле'

    rele_contr = models.ForeignKey(Controllers, on_delete=models.CASCADE, verbose_name='Контроллер')
    rele_time = models.DateTimeField(auto_now=True, verbose_name='Дата\Время')
    rele_num = models.IntegerField(verbose_name='Номер реле')
    rele_satus = models.IntegerField(verbose_name='Состояние')

    def __str__(self):
        return 'Реле-' + str(self.rele_num)
