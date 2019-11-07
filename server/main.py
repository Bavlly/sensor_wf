import urequests 


print('\nDEMO#1: getting test webpage...')
userdata = "udata"
r = urequests.post('http://172.20.10.2:8080/Parkeergarage/get.php?{userdata}')
print(r)
print(r.content)
print(r.text)


