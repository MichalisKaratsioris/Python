map = {
    "William A. Lathan": "405-709-1865",
    "John K. Miller": "402-247-8568",
    "Hortensia E. Foster": "606-481-6467",
    "Amanda D. Newland": "319-243-5613",
    "Brooke P. Askew": "307-687-2982"
}

# print("What is John K. Miller's phone number?")
print(map["John K. Miller"])

# print("Whose phone number is 307-687-2982?")
for k, v in map.items():
    if v == "307-687-2982":
        print(k)
        break

# print("Do we know Chris E. Myers' phone number? (yes/no)")
print("yes" if "Chris E. Myers" in map.keys() else "no")


# print("Do we know Brooke P. Askew' phone number? (yes/no)")
# print("yes" if "Brooke P. Askew" in map.keys() else "no")