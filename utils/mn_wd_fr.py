import datetime
from random import choice


# Если пн,ср или пт возвращает ссылку
def day_pic():
    monday_pic = [
        'https://lh3.googleusercontent.com/proxy/6tLX5cGBEg4_CeLtmK82o2SpD_ZnsyS2w2oSRXvWFWKtFOJGhxesdGtR7-UQ_EJ2mATdNOPtG6973uUNwSIz43xibKM',
        'https://cs2.pikabu.ru/post_img2/2014/02/03/4/1391398638_1123079859.jpg',
        'https://pm1.narvii.com/7142/c40694bdb9c66d77b9960e96c1a97df1f46307c8r1-1080-1249v2_hq.jpg',
        'https://proprikol.ru/wp-content/uploads/2019/06/prikolnye-kartinki-pro-ponedelnik-4.jpg',
        'https://tolknews.ru/picture/6245/1920x.jpg',
        'http://risovach.ru/upload/2013/01/mem/kakoy-pacan_9155750_orig_.jpeg',
        'https://www.meme-arsenal.com/memes/75453be2c8a848e0a4220ffd08f2f1b5.jpg',
        'https://lh3.googleusercontent.com/proxy/vbMPJXVc6fNK6IwuPWrv1eGQYLS46WMFh9jFxQvFbsCDWDwyp5t2_NOwYwiYjS5UxrDTWlkYkam865LrXM_eDdp0jrI',
    ]

    wednesday_pic = [
        'https://lh3.googleusercontent.com/proxy/Ey6Xrh80KiGmQz79l08Cd8DoZbK2BuJZ5B1iIK34iBTzoobb1FDMnge2fK8sEcLS5rxnvYT-MGWvf3MAXd8oKgK_GmY',
        'https://www.meme-arsenal.com/memes/698eabe0ce7f4d41707c0691df0d630d.jpg',
        'https://privetpeople.ru/3D/A1/sreda-90.jpg',
        'https://lh3.googleusercontent.com/proxy/-_4-UI2AZk5WIvU0xJyf8tAMrH0pZ8KrJE80_owkXS1B_9n3FSszPR6H8Wx82fGxpLhoQ1saWUE8-HFzM__WDbDQGaM',
        'https://lh3.googleusercontent.com/proxy/UNQRpTmoM_mWSoM_3-xiMLVErbRM9lmfyasb-iDUjq7oNw7I4KtelxR7kOutNYqb16-MehPTerwKIS-jg2_UuBvNp1s',
        'https://lh3.googleusercontent.com/proxy/X-TG8efznxOEc-0ohcBVRaYw5yXhmWiQIy9PkL8k7BbOApeIWnCuY91jHTcmPJg4a-peH6RVpegm1oJi68v_2Yt3ArM',
        'http://risovach.ru/upload/2014/03/mem/kot-iz-shreka_45057222_orig_.jpeg',
        'http://risovach.ru/upload/2016/04/mem/uzbagoisya_112130829_orig_.jpg',
        'http://memchik.ru/images/mems/5df0e8046ecf8.jpg'
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxumyUFjpMfJ3oNjvL2MhfmNvhYarofP-_q7IslwgdKgdznKvkdGrmgXilvpLsYk_y07w&usqp=CAU'
    ]

    friday_pic = [
        'https://u01.appmifile.com/images/2018/06/29/bc024a13-ddf6-4d25-b90f-5e55ed1f5a68.png',
        'https://memepedia.ru/wp-content/uploads/2019/04/pyatnitsa-mem-15.jpg',
        'https://lh3.googleusercontent.com/proxy/ngkKZnwFk3YijTYMarRFZEdXP0EehGgPhUndH9QoXjFP7DPpLnqVhQ4---UOrJAU4gYk_ykMTskAv5c2Qdr3Pk11ptc',
        'https://memepedia.ru/wp-content/uploads/2019/04/pyatnitsa-mem-17.jpg',
        'https://memepedia.ru/wp-content/uploads/2019/04/pyatnitsa-mem-19.jpg',
        'https://lh3.googleusercontent.com/proxy/hIB3PTO9E4mcCSP1ocYEbpoPWEsOpZCSlFMfeftdTNNekjBsNTMkOGmiKYorlX-5SLGA7BZcWEFP181AsDB9sQ3HfdU',
        'https://cs4.pikabu.ru/post_img/2015/06/12/9/1434119312_937438936.jpg',
        'https://memepedia.ru/wp-content/uploads/2019/04/pyatnitsa-mem-8.jpg',
        'https://www.meme-arsenal.com/memes/42bf4bcff91902b45fa991ddaca4fcda.jpg',
        'http://risovach.ru/upload/2014/11/mem/psih_67599661_orig_.jpg',
    ]
    week_days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    dict_days = {
        "monday": monday_pic,
        "wednesday": wednesday_pic,
        "friday": friday_pic
    }
    now = datetime.datetime.now()
    day = week_days[now.weekday()]
    for d, p in dict_days.items():
        if day == d:
            return choice(p)