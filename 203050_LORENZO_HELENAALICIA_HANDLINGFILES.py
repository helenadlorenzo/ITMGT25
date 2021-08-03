# PRODUCTS
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# 1 GET_PRODUCT
def get_product(code):
    return products[code]
    
get_product("espresso")

# 2 GET_PROPERTY
def get_property(code, property):
    return products[code][property]
    
get_property("espresso", "price")

# 3 MAIN()
def main():
    
    americano_quantity = 0
    brewedcoffee_quantity = 0
    cappuccino_quantity = 0
    dalgona_quantity = 0
    espresso_quantity = 0
    frappuccino_quantity = 0
    
    americano_total = 0
    brewedcoffee_total = 0
    cappuccino_total = 0
    dalgona_total = 0
    espresso_total = 0
    frappuccino_total = 0
    sumtotal = 0
    
    while True:
        input_line = input("{product_code},{quantity}: ")
        input_indiv = input_line.split(",")
        product_code = input_indiv[0]
        
        if input_line == "/":
            break
        else:
            # quantity = int(input_indiv[1][1:(len(input_indiv[1])-1)])
            
            if product_code == "{americano}":
                americano_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                americano_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                americano_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                americano_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            elif product_code == "{brewedcoffee}":
                brewedcoffee_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                brewedcoffee_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                brewedcoffee_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                brewedcoffee_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            elif product_code == "{cappuccino}":
                cappuccino_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                cappuccino_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                cappuccino_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                cappuccino_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            elif product_code == "{dalgona}":
                dalgona_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                dalgona_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                dalgona_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                dalgona_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            elif product_code == "{espresso}":
                espresso_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                espresso_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                espresso_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                espresso_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            elif product_code == "{frappuccino}":
                frappuccino_code = input_indiv[0][1:len(list(input_indiv[0]))-1]
                frappuccino_name = get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "name")
                frappuccino_quantity += int(input_indiv[1][1:(len(input_indiv[1])-1)])
                frappuccino_total += int(input_indiv[1][1:(len(input_indiv[1])-1)]) * get_property(input_indiv[0][1:len(list(input_indiv[0]))-1], "price")
            else:
                print("Please try again.")
    sumtotal = americano_total + brewedcoffee_total + cappuccino_total + dalgona_total + espresso_total + frappuccino_total
    
    if americano_quantity != 0:
        line1 = (f"{americano_code}\t\t{americano_name}\t\t{americano_quantity}\t\t\t\t{americano_total}\n")
    else:
        line1 = ""
    
    if brewedcoffee_quantity != 0:
        line2 = (f"{brewedcoffee_code}\t\t{brewedcoffee_name}\t\t{brewedcoffee_quantity}\t\t\t\t{brewedcoffee_total}\n")
    else:
        line2 = ""
    
    if cappuccino_quantity != 0:
        line3 = (f"{cappuccino_code}\t\t{cappuccino_name}\t\t{cappuccino_quantity}\t\t\t\t{cappuccino_total}\n")
    else:
        line3 = ""
    
    if dalgona_quantity != 0:
        line4 = (f"{dalgona_code}\t\t\t{dalgona_name}\t\t\t{dalgona_quantity}\t\t\t\t{dalgona_total}\n")
    else:
        line4 = ""
    
    if espresso_quantity != 0:
        line5 = (f"{espresso_code}\t\t{espresso_name}\t\t{espresso_quantity}\t\t\t\t{espresso_total}\n")
    else:
        line5 = ""
    
    if frappuccino_quantity != 0:
        line6 = (f"{frappuccino_code}\t\t{frappuccino_name}\t\t{frappuccino_quantity}\t\t\t\t{frappuccino_total}\n")
    else:
        line6 = ""
    
    with open("receipt.txt","w") as receipt:
        receipt.write("""
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n""")
        receipt.write(line1)
        receipt.write(line2)
        receipt.write(line3)
        receipt.write(line4)
        receipt.write(line5)
        receipt.write(line6)
        receipt.write(f"""
Total:\t\t\t\t\t\t\t\t\t\t{sumtotal}
==""")
        receipt.close()
    
main()