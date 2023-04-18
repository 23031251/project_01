import random
import datetime
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

my_favorite_songs = list(my_favorite_songs_dict)    
print(my_favorite_songs)


selection = random.sample(my_favorite_songs, k=3)
print("Задание B. Три песни к прослушиванию: ", selection)
duration_m_s = datetime.timedelta()
for g in selection:
    p = str(my_favorite_songs_dict[g])
    (m, s) = p.split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    duration_m_s += d
    # print(d)
# print(duration_m_s)
hms = str(duration_m_s)
# print("hms: ", hms)
hh, mm, ss = hms.split(':')
hhh = int(hh)
mmm = int(mm)
duration_m = hhh * 60 + mmm
# print("duration_m: ", duration_m)
print (f"Три песни звучат", duration_m, "минут" )