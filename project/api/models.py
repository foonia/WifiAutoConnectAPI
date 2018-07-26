from django.db import models


class Wifi(models.Model):
    FACILITY = (
        ('a', '관공서'),
        ('b', '지역문화시설'),
        ('c', '편의시설'),
        ('d', '서민복지시설'),
        ('e', '교통시설'),
        ('z', '기타'),
    )

    place = models.CharField(max_length=128, help_text='설치장소명')
    place_description = models.CharField(max_length=128, help_text='설치장소상세설명')
    city = models.CharField(max_length=128, help_text='설치시명')
    country = models.CharField(max_length=128, help_text='설치군구명')
    facility = models.CharField(max_length=128, choices=FACILITY, help_text='설치시설구분')
    service_provider = models.CharField(max_length=128, help_text='서비스제공사')
    wifi_ssid = models.CharField(max_length=128, help_text='와이파이SSID')
    installed_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
