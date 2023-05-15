import requests

a = 1
dosya = open("cikti.txt","w")
for i in range(1000):
    
    
    try:
        response = requests.get("https://www.pdfdrive" + str(a) +".com",verify=False)

    
    except requests.exceptions.ConnectionError:
        response = "bağlantı yok"
    print(a)
    print(response)
    dosya.write(str(a) + "/n")
    dosya.write(str(response))
    
    a +=1
    