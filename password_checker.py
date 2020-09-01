uzunluq=0
ed=0
eded="0123456789"

shifre=input("Shifreni daxil edin: ")
# Şifrənin uzunluğunu təyin et
uz=len(shifre)
if uz>=6:
    uzunluq+=1
else:
    uzunluq=uzunluq

# ən azı 1 ədədi tapmaq
for i in shifre:
    for u in eded:
        if i==u:
            ed+=1
    else:
        ed=ed

# İstifadəçiyə şifrənin qorunması haqda məlumatı çatdırmaq
if uzunluq>=1 and ed>=1:
    print("Şifrəniz möhkəmdir")

else:
    print("Şifrəniz zəifdir")

