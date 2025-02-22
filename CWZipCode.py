##finding latitude and longitude from zipcode
zipcodes=open("/Users/madeleinechen/Desktop/11th Grade/comp sci python/2024_Gaz_zcta_national.txt", "r")

n=int(input())
for T in range(n):
    zip_input=input()

    for line in zipcodes:
        info=list(line.split())

        if zip_input==info[0]:
            lat=float(info[5])
            long=float(info[6])
            location_list=(lat),(long)
            location=tuple(location_list)
            print(location)
        else:
            continue
zipcodes.close()

def zipcode(lat,long):
    zipcodes=open("/Users/madeleinechen/Desktop/11th Grade/comp sci python/2024_Gaz_zcta_national.txt", "r")

    lat=float(lat)
    long=float(long)
    
    for line in zipcodes:
         info=list(line.split())
         if lat in float(info[5]) and long in float(info[6]):
            print(info[0])
    zipcodes.close()
