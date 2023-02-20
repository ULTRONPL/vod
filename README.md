# v1.3 test - pobieracz vod - wszystkich odcinków różnych seriali

wersja 1.3 obsługuje tylko pobieranie odcinków seriali

w wersji 2.0 będzie możliwość pobierania filmów

potrzebne:
 
   - python 3.9
 
   - pip3 install requests = import requests
 
   - pip3 install regex = import re
   
   
Po poprawnym zainstalowaniu klikamy w więcej informacji a następnie w wybrany odcinek

![4](https://user-images.githubusercontent.com/98317764/220185958-a0b2a2b1-f1b2-4ec3-acbe-6ad6c5a6e82c.png)

gdy to już zrobimy kopiujemy link

![2](https://user-images.githubusercontent.com/98317764/220185160-cee34107-831e-4f01-9b0f-32b6acdd2cc4.png)

Jeśli wprowadzono poprawny link to powinno wyświetlić się

![3](https://user-images.githubusercontent.com/98317764/220185132-320d905c-79f7-4ebd-af93-5c9f17566710.png)

 'https://s4.tvp.pl/images2/d/d/a/uid_dda03c7ce4c348e18ea90ac89e1c43f4_width_'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video.ism/video-fmp4.m3u8'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-6.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-5.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-4.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-7.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video.ism/video.mpd'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-9.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-3.mp4'
 'https://sdt-netia2-114.tvp.pl/token/video/vod/66003748/20230220/2681034006/13b75a4b-1730-480c-ac4f-bec0176e95d0/video-2.mp4']
                                                                                                            pliki tylko .mp4 reszta nieważna
                                                                                                            video-(większy numer=lepsza jakość).mp4

zaznaczamy i kopiujemy link a następnie wklejamy go do przeglądarki
