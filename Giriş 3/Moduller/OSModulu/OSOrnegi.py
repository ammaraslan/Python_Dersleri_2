import os
print(os.name)
# print(os.path)
print(os.getcwd())
os.chdir("../MathModulu")
print(os.getcwd())

os.chdir("../")
print(os.getcwd())
if(os.path.exists("TEST")):
    print("var zaten")
else:
    os.mkdir("TEST")

# os.rename("ORNEL","OsOrnekleriKlasoru")

os.rmdir("TEST")

print(os.stat("OsOrnekleriKlasoru"))

for dosya in os.walk(os.getcwd()):
    print(dosya)