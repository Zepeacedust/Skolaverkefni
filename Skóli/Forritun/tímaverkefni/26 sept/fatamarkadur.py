#arnór 26 sept
framhald = True

keyptir_h_sky = 0
keyptir_d_sky = 0
keyptir_h_bux = 0
keyptir_d_bux = 0
keyptir_h_sko = 0
keyptir_d_sko = 0
keyptir_h_sok = 0
keyptir_d_sok = 0
nafn = input("skráðu inn nafn")
kennitala = input("skráðu inn kennitölu")
while framhald:
    print("veldu 1 fyrir herra skyrtur sem kostar 2740")
    print("veldu 2 fyrir dömu skyrtur sem kostar 4232")
    print("veldu 3 fyrir herra buxur sem kostar 4353")
    print("veldu 4 fyrir dömu buxur sem kostar 4478")
    print("veldu 5 fyrir herra sko sem kostar 2977")
    print("veldu 6 fyrir dömu sko sem kostar 2344")
    print("veldu 7 fyrir herra sokka sem kostar 2564")
    print("veldu 8 fyrir dömu sokka sem kostar 9575")
    print("veldu hætta til að hætta")
    val = input("veldu vöru: ")
    if val == "1":
        fjoldi = int(input("hversu margar skyrtur viltu? "))
        keyptir_h_sky += fjoldi
    elif val == "2":
        fjoldi = int(input("hversu margar skyrtur viltu? "))
        keyptir_d_sky += fjoldi
    elif val == "3":
        fjoldi = int(input("hversu margar buxur viltu? "))
        keyptir_h_bux += fjoldi
    elif val == "4":
        fjoldi = int(input("hversu margar buxur viltu? "))
        keyptir_d_bux += fjoldi
    elif val == "5":
        fjoldi = int(input("hversu mörg skópör viltu? "))
        keyptir_h_sko += fjoldi
    elif val == "6":
        fjoldi = int(input("hversu mörg skópör viltu? "))
        keyptir_d_sko += fjoldi
    elif val == "7":
        fjoldi = int(input("hversu mörg sokkapör viltu? "))
        keyptir_h_sok += fjoldi
    elif val == "8":
        keyptir_d_sok += fjoldi
        fjoldi = int(input("hversu mörg sokkapör viltu? "))    
    elif val == "hætta":
        framhald = False
verd = 0
verd += 2740 * keyptir_h_sky 
verd += 4232 * keyptir_d_sky 
verd += 4353 * keyptir_h_bux 
verd += 4478 * keyptir_d_bux 
verd += 2977 * keyptir_h_sko 
verd += 2344 * keyptir_d_sko 
verd += 2564 * keyptir_h_sok 
verd += 9575 * keyptir_d_sok 
print("""
Fatamarkaður Siggu og Grétars
{nafn}
{kennitala}

""")
