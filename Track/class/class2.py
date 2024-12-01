# ---------------------------------
# For Loop List     
# ---------------------------------

# citylist = ['Sylhet', 'Cumilla', 'Feni','Barisal']

# for city in citylist:
#     print(city)


# ----------------------
# For Loop String   
# ---------------------
# name = "Cumilla"
# for chr in name:
#     print(chr)

# ------------------------------
# For Loop String Break
# ------------------------------
# name = "Dhaka"
# for chr in name:
#     if chr == "k":
#         break
#     print(chr)

# ------------------------------
# For Loop String continue
# ---------------------------------
# name = "Dhaka"
# for chr in name:
#     if chr == "k":
#         continue
#     print(chr)


# ----------------------
# For Loop Over Range
# ----------------------
# for item in range(0,10,2):
#     print(item)




# -----------------------------------
# While Loop Over List
# ------------------------------------
# fruits = ['apple', 'banana', 'cherry']
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# --------------------------------------
# While Loop Over String
# ---------------------------------
# name = "Cumilla"
# index = 0
# while index < len(name):
#     print(name[index])
#     index += 1


# ---------------------
# While Loop Over Range
# ------------------------
# start = 0
# end = 10
# while start < end:
#     print(start)
#     start += 1


# -----------------------
# While Loop Over Break
# -----------------------
# fruits = ['Apple', 'Banana', 'Cherry']
# index = 0
# while index < len(fruits):
#     if(fruits[index]== "Cherry"):
#         break
#     print(fruits[index])
#     index += 1


# -------------------------------
# While Loop Over Continue
# -------------------------------

# fruits = ['Apple', 'Banana', 'Cherry']
# index = 0
# while index < len(fruits):
    
#     if(fruits[index]== "Banana"):
#         continue
    
#     print(fruits[index])
#     index += 1


# ------------------------
# While Loop Over Counter
# ------------------------
# Counter = 0
# while Counter <10:
#     Counter += 1
#     if Counter % 2 == 0:
#         Counter
#     print(Counter)
    

# -----------------------------
# List 
# -----------------------------
# citylist = ['Cumilla', 'Dhaka', 'Sylhet', 'Rajshahi']
# print(citylist)

# -----------------------------
# List Append
# -----------------------------
# citylist = ['Cumilla', 'Dhaka', 'Sylhet', 'Rajshahi']
# citylist.append("Khulna")
# print(citylist)

# -----------------------------
# list Insert
# ------------------------------
# citylist = ['Cumilla', 'Dhaka', 'Sylhet', 'Rajshahi']
# citylist.insert(1,"asdf")
# print(citylist)

# ------------------------------------------
# List Extend
# ------------------------------------------
# citylist = ['Cumilla', 'Dhaka', 'Sylhet', 'Rajshahi']
# citylist2 = ['NewYork','London', 'Torento']
# citylist.extend(citylist2)
# print(citylist)

# ------------------------------------------
# List Remove 
# ------------------------------------------
# list = ['Dhaka', 'Khulna', 'Cumilla']
# list.remove('Dhaka')
# print(list)

# ------------------------------------------
# List Pop    / Remove the last item 
# ------------------------------------------
# list = ['Dhaka', 'Khulna', 'Cumilla']
# list.pop()
# print(list)

# ------------------------------------------
# List index
# ------------------------------------------
# list = ['Dhaka', 'Khulna', 'Cumilla']
# index = list.index('Khulna')
# print(index)

# ------------------------------------------
# List Count
# ------------------------------------------
# list = ['Dhaka', 'Dhaka', 'Cumilla', 'Khulna','Dhaka']
# countvalu = list.count('Dhaka')
# print(countvalu)

# ------------------------------------------
# List Sort         / Assending Order
# ------------------------------------------
# number = [1,2,3,5,2,7,4,8]
# number.sort()
# print(number)

# ------------------------------------------
# List Reverse         / Descending Order
# ------------------------------------------
# number = [1,2,3,5,2,7,4,8]
# number.reverse()
# print(number)




# ----------------------------------------
# Tuples 
# -----------------------------------------
# fruits = ('Apple','Banana','Cherry')
# print(fruits)


# ----------------------------------------
# Tuples Over Index
# -----------------------------------------
# fruits = ('apple', 'banana', 'Cherry')
# print(fruits[1])


# ----------------------------------------
# Tuples Over Count
# -----------------------------------------
# number = (1,2,3,4,6,1,2,3,4,2)
# count = number.count(2)
# print(count)



# ----------------------------------------
# Tuples Convert tuple to list
# -----------------------------------------
# citytuple = ('Dhaka', 'Rajshahi', 'Khulna')
# citylist = list(citytuple)
# print(citylist)




# --------------------------------------------------------
# ----------------------------------------
# Set Id Location cheek
# -----------------------------------------
# fruits = {'apple','banana','cherry'}
# print(id(fruits))

# fruits.add('mango')
# print(id(fruits))



# ----------------------------------------
# Set Add value
# -----------------------------------------
# fruits = {'apple', 'banana','chery'}
# fruits.add('mango')
# print(fruits)



# ----------------------------------------
# Set Update
# -----------------------------------------
# fruits = {"apple","gouava", "grap"}
# fruits.update(["A","B"])
# print(fruits)



# ----------------------------------------
# Tuples Remove
# -----------------------------------------
# fruits = {"Apple","Banana","Cherry"}
# fruits.remove("Banana")
# print(fruits)


# ----------------------------------------
# Tuples Clear
# -----------------------------------------
# fruits = {"Apple","Banana","Cherry"}
# fruits.clear()
# print(fruits)


# ----------------------------------
# Dictionary
# ----------------------------------
# ramnapark = {
#     "kamal" : "jorina",
#     "jamal" : "Karina",
#     "damal" : "Sokina",
#     "tomal" : "Sokina"
# }
# print(ramnapark)
# print(ramnapark["kamal"])


# --------------------------
# Dictionary Practice
# ---------------------------

# linkedin = {
#     "Name" : "Dhruba Majumder",
#     "Designation" : "Software Engineering Manager",
#     "Connections" : "500+",
#     "Profile_views" : 1212,
#     "IsVerified" : False,
#     "Followers" : 1500,
#     "Profile_image" : "https://name.com.png",
#     "Exp_years" : 3.5,
#     "Work_area" : "Fintech"
# }

# print(linkedin)



# -----------------------------
# disctionary keys/ valus
# ----------------------------
# iphone = {
#     "model" : "16 pro max",
#     "price" : 250000,
#     "rating" : 4.5,
#     "isStock" : True,
#     "color" : ['Titenium' , 'Black', 'White', 'Desert'],
#     "img" : {"https://imge.png"},
#     "specification" : {
#         "Size" : " 6.9 -inch",
#         "Type" : "Super Retina XDR Display",

#     }

# }
# print(iphone.keys())


# ---------------------------
# Dictionary Update
# --------------------------------
# ramnapark = {
#     "kamal" : "jorina",
#     "jamal" : "Karina",
#     "damal" : "Sokina",
#     "tomal" : "Sokina"
# }

# ramnapark.update({"damal" : "Bobita"})
# print(ramnapark)


# ---------------------
# Dictionary clear
# ----------------------------
# ramnapark = {
#     "kamal" : "jorina",
#     "jamal" : "Karina",
#     "damal" : "Sokina",
#     "tomal" : "Sokina"
# }
# ramnapark.clear()
# print(ramnapark)



# --------------------------------------
# Dictionary find methood  (get)
# --------------------------------------
# ramnapark = {
#     "kamal" : "jorina",
#     "jamal" : "Karina",
#     "damal" : "Sokina",
#     "tomal" : "Sokina"
# }
# damals = ramnapark.get('damals', None)
# print(damals)
