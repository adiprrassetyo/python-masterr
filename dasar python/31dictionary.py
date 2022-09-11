# Belajar Tipe Data Dictionary

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);

daftar_customer = []
eko = { "Name":"Eko", "Age":30, "Address":"Subang" , "Company":"X"}
budi = { "Name":"Budi", "Age":25, "Address":"Surabaya" , "Company":"Y"}
joko = { "Name":"Joko", "Age":31, "Address":"Cirebon" , "Company":"Z"}

daftar_customer.append(eko)
daftar_customer.append(budi)
daftar_customer.append(joko)

for customer in daftar_customer:
    print("====================")
    for key,value in customer.items():
        print(f"{key}:{value}")

