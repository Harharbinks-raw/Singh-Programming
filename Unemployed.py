dict = {
    "usd" : 1.00,
    "eur" : 0.84,
    "gbp" : 0.72,
    "jpy" : 109.98,
    "aud" : 1.33,
    "cad" : 1.26,
    "chf" : 0.92,
    "cny" : 6.45,
    "hkd" : 7.76,
    "nzd" : 1.43
}
usercur = float(input("you money  : "))
covertto= input("convert to ???:").lower()
usercurt = input("USD, eur, gbp, jpy, aud, cad,chf,hkd,nzd :").lower()


formula = usercur / dict[covertto] * dict[usercurt]
print(f"{formula} {usercurt}")

if covertto not in dict :
    print("currentcy is no avail")

else:
    print(f"{formula} {usercurt}")
