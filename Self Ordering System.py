import datetime
import restubill
print("********  WELCOME TO TIWARI RESTURANT  ********")
sum_total=0
while (1>0):
    print("WHAT DO YOU WANT TO ORDER ?")
    print("""WE OFFER 
             1. CHINESE
             2. DAHI 
             3. SALAD
             4. PAPAD
             5. PANEER
             6. ITALIAN
             7. SOUTHINDIAN
             8. DAAL
             9. Exit""")
    choice=input("ENTER YOUR CHOICE: ")
    ch=choice.lower()
    if (ch=="chinese") or (ch=="1"):
        print("                 M_E_N_U_E                       ")
        print("""           ### CHINESE ###

        Hakka Noodles          हक्का नूडल्स       120/-          1

        Veg Choumin            वेज चाउमिन        110/-          2

        Veg Noodles            वेज नूडल्स          110/-          3

        Veg Chopsuey           वेज चोपसी         140/-           4   

        Veg Fried Rice         वेज फ्राइड राइस     105/-           5

        Veg Kofte              वेज कोथे           125/-           6

        Veg Manchurian Dry     वेज मंचूरियन ड्राय     140/-           7

        Veg Manchurian GREAVY  वेज मंचूरियन ग्रेवी     120/-            8

        Chilli Paneer Dry      चिल्ली पनीर ड्राय      140/-           9

        Chilli Paneer GREAVY   चिल्ली पनीर ग्रेवी      140/-            10

        Paneer Manchurian      पनीर मंचूरियन       135/-             11

        Chinese Bhel          चायनीस गेल         135/-              12

        Gobhi Chili            गोभी चिल्ली         140/-              13

        Gobhi Manchurian       गोभी मंचूरियन       125/-              14

        Paneer Tikka Dry       पनीर टिक्का ड्राय     125/-              15

        Manchurian Noodles     मंचूरियन नूडल्स      175/-              16

        Veg Sizler             वेज सिज़्लर         175/-               17

        Chana chili Dry        चना चिल्ली ड्राय      125/-               18

        Hani Batato            हनी बाते           240/-               19

        Veg MOMOSs             वेज मोमोस         130/-               20

        ********************* TO GO BACK PRESS 900 *************************
        """)
        n_a=[1,3,7,8,19]
        n_chinese={1:120, 2:110, 3:110, 4:140, 5:105, 6:125, 7:140, 8:120, 9:140, 10:140, 11:135, 12:135, 13:140, 14:125, 15:125, 16:175, 17:175, 18:125, 19:240, 20:130,900:""}
        chinese={1:"Hakka Noodles   हक्का नूडल्स",2:"Veg Choumin  वेज चाउमिन",3:"Veg Noodles   वेज नूडल्स",4:"Veg Chopsuey  वेज चोपसी",5:"Veg Fried Rice   वेज फ्राइड राइस",6:"Veg Kofte  वेज कोथे",7:"Veg Manchurian Dry  वेज मंचूरियन ड्राय",8:"Veg Manchurian GREAVY  वेज मंचूरियन ग्रेवी",9:"Chilli Paneer Dry  चिल्ली पनीर ड्राय",10:"Chilli Paneer GREAVY  चिल्ली पनीर ग्रेवी",11:"Paneer Manchurian पनीर मंचूरियन",12:"Chinese Bhel  चायनीस गेल",13:"Gobhi Chili  गोभी चिल्ली",14:"Gobhi Manchurian       गोभी मंचूरियन",15:"Paneer Tikka Dry पनीर टिक्का ड्राय",16:"Manchurian Noodles  मंचूरियन नूडल्स",17:"Veg Sizler  वेज सिज़्लर",18:"Chana chili Dry  चना चिल्ली ड्राय",19:"Hani Batato  हनी बाते",20:"Veg MOMOSs  वेज मोमोस",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_a:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif order==900:
                 break
            elif (order>len(chinese)):
                print("PLEASE ENTER FROM THE MENUE")    
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_chinese[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="dahi special") or (ch=="2"):
        print("                M_E_N_U_E                       ")
        print(""""         ###Dahi Special###

        Plain Dahi              प्लेन दही            65/-         1

        Boondi Raita            बुंदी रायता           70/-         2

        Fruit Raita             फुटरायता            90/-         3

        Pineapple Raita         पाइनापल रायता       90/-         4

        Veg Raita               वेज रायता            80/-        5

        Aaloo Mint Raita        आलू मिंट रायता        80/-        6 

        Dahi Fry                दही फाई             75/-        7

        Dahi Fry Butter         दही फाई बटर         85/-        8

        Dahi Tadka              दही तड़का           90/-         9 
        ********************* TO GO BACK PRESS 900 *************************
         """)
        n_b=[3]
        n_dahi={1:25,2:70,3:90,4:90,5:80,6:80,7:75,8:85,9:90,900:""}
        dahi={1:"Plain Dahi  प्लेन दह",2:"Boondi Raita  बुंदी रायता",3:"Fruit Raita  फुटरायता",4:"Pineapple Raita  पाइनापल रायत",5:"Veg Raita  वेज रायता",6:"Aaloo Mint Raita  आलू मिंट रायत",7:"Dahi Fry  दही फाई",8:"Dahi Fry Butter  दही फाई बटर",9:"Dahi Tadka  दही तड़का",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_b:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif order==900:
                 break    
            elif (order>len(n_dahi)):
                print("PLEASE ENTER FROM THE MENUE")    
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_dahi[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="salad") or (ch=="3"):
        print("                   M_E_N_U_E                       ")
        print("""                ###SALAD###

       Green Salad          ग्रीन सलाद               35/-       1

       Kachumar Salad       कचुमर सलाद             40/-       2

       Tomato Salad         चेमेवे सलाद               35/-       3

       Onion Salad          ओनियन सलाद             30/-       4

       Peanut Salad         पीनट सलाद               90/-       5
       ********************* TO GO BACK PRESS 900 *************************
       """)
        n_s=[5]
        n_salad={1:35,2:40,3:35,4:30,5:90,900:""}
        salad={1:"Green Salad  ग्रीन सलाद",2:"Kachumar Salad  कचुमर सलाद",3:"Tomato Salad  चेमेवे सलाद",4:"Onion Salad ओनियन सलाद",5:"Peanut Salad  पीनट सलाद",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_s:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(salad)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_salad[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="papad") or (ch=="4"):
        print("                   M_E_N_U_E                       ")
        print("""                ###PAPAD###

              Papad Dry       पापड़ ड्राई          12/-      1

              Papad Bhurji    पापड़ भुजी          90/-      2

              Papad Fry       पापड़ फाय          20/-      3

              Papad Masala    पापड़ मसाला        35/-       4

              Papad Dry Masala पापड़ ड्राय मसाला    30/-       5
              ********************* TO GO BACK PRESS 900 *************************
              """)
        n_p=[5]
        n_papad={1:12,2:90,3:20,4:35,5:30,900:""}
        papad={1:"Papad Dry  पापड़ ड्राई ",2:"Papad Bhurji  पापड़ भुजी",3:"Papad Fry  पापड़ फाय",4:"Papad Masala    पापड़ मसाल",5:"Papad Dry Masala पापड़ ड्राय मसाला",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_p:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(papad)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_papad[order]*qat)
                print("YOUR BILL IS:",sum_total) 
    elif (ch=="paneer") or (ch=="5"):
        print("                   M_E_N_U_E                       ")
        print("""             ###TASTE OF PANEER###

        Chhola Paneer      खेला पनीर     160/-    1

        Paneer Panjabi    पनीर पंजाबी     160/-    2

        Paneer Bhurji     पनीर भुर्जी      180/-     3

        Mutter Paneer     मटर पनीर      130/-     4

        Paneer Maharaja   पनीर महाराजा   190/-      5

        Paneer Pasanda    पनीर पसंदा     220/-      6

        Palak Paneer       पालक पनीर    130/-      7

        Kadai Paneer       कड़ाई पनीर    140/-       8

        Shahi Paneer       शाही पनीर     130/-       9

        Paneer Lababdar    पनीर लबाबदार  140/-       10

        Paneer Do Pyaza    पनीर दो प्याजा   140/-      11

        Paneer Makhhanwala  पनीर मख्खनवाला  150/-     12

        Paneer Mumtaz      पनीर मुमताज    240/-       13

        Paneer Badshahil    पनीर बादशाही    265/-      14

        Kaju Paneer         काजू पनीर       170/-      15

        Kaju Curry         काजू करी        170/-       16

        Malai Kofta        मलाई कोफ्ता     140/-        17
        ********************* TO GO BACK PRESS 900 *************************
        """)
        n_p=[5]
        n_paneer={1:160,2:160,3:180,4:130,5:190,6:220,7:130,8:140,9:130,10:140,11:140,12:150,13:240,14:265,15:170,16:170,17:140,900:""} 
        paneer={1:"Chhola Paneer खेला पनीर",2:"Paneer Panjabi पनीर पंजाबी",3:"PaneerBhurji पनीरभुर्जी",4:"Mutter Paneer मटर पनीर",5:"PaneerMaharaja पनीरमहाराजा",6:"PaneerPasanda पनीरपसंदा",7:"PalakPaneer पालकपनीर",8:"KadaiPaneer कड़ाईपनीर",9:"ShahiPaneer शाहीपनीर",10:"PaneerLababdar पनीरलबाबदार",11:"PaneerDo Pyaza  पनीरदो प्याजा",12:"PaneerMakhhanwala पनीरमख्खनवाल",13:"PaneerMumtaz पनीरमुमताज",14:"PaneerBadshahil  पनीरबादशाही",15:"KajuPaneer काजूपनीर",16:"Kaju Curry  काजू करी",17:"MalaiKofta मलाईकोफ्ता",900:"" }
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_p:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(paneer)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_paneer[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="italian") or (ch=="6"):
        print("                   M_E_N_U_E                       ")
        print("""              ###ITALIAN###

        Veg Pizza           वेज पिज्जा                145/-          1

        Cheese Pizza        चीज पिज्जा                145/-          2

        ChinesePizza        चाइनीस पिज्जा             165/-           3

        Veg Burger          वेज बर्गर                  85/-           4

        Cheese Burger       चीज वर्गर                 120/-           5

        Onion Pizza         ओनियन पिज्जा             120/-            6

        Tomato Pizza        टोमेवे पिज्जा               120/-            7
        ********************* TO GO BACK PRESS 900 *************************
        """)
        n_i=[5]
        n_italian={1:145,2:145,3:165,4:85,5:120,6:120,7:120,900:""} 
        italian={1:"Veg Pizza  वेज पिज्जा ",2:"Cheese Pizza  चीज पिज्जा ",3:"ChinesePizza  चाइनीस पिज्जा ",4:" Veg Burger  वेज बर्गर",5:"Cheese Burger  चीज वर्गर",6:"Onion Pizza  ओनियन पिज्जा",7:" Tomato Pizza  टोमेवे पिज्जा ",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in n_i:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(italian)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_italian[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="south indian") or (ch=="7"):
        print("                M_E_N_U_E                       ")  
        print("""           ###SOUTH INDIAN###
        Masala Dosa          मसाला डोसा          90/-         1

        Shahi Dosa           शाही डोसा           110/-         2

        Panir Dosa           पनीर डोसा           120/-         3

        Mahsur Dosa          महशूर डोसा          140/-          4

        Plain Pepar Dosa     प्लेन पेपर डोसा        90/-           5

        Masala Pepar Dosa    मसाला पेपर डोसा       100/-         6

        Plain Dosa           प्लेन डोसा            75/-            7

        Onion Uttapam        ओनियन उत्तपम         85/-           8

        Tomato Uttapam       चेमेवे उत्तपम           85/-            9

        Rawa Masala Dosa     रवा मसाला डोसा        90/-            10

        Plain Dosa           प्लेन डोसा             80/-            11
        ******************** TO GO BACK PRESS 900 *************************
        """)
        s_i=[5]
        n_s_indian={1:90,2:110,3:120,4:140,5:90,6:100,7:75,8:85,9:85,10:90,11:80,900:""} 
        southindian={1:"Masala Dosa  मसाला डोसा ",2:"Shahi Dosa  शाही डोसा ",3:" Panir Dosa  पनीर डोस",4:"Mahsur Dosa  महशूर डोसा ",5:"Plain Pepar Dosa  प्लेन पेपर डोस",6:"Masala Pepar Dosa   मसाला पेपर डोस",7:"Plain Dosa  प्लेन डोस ",8:" Onion Uttapam   ओनियन उत्तपम",9:"Tomoto Uttapam  चेमेवे उत्तपम",10:"Rawa Masala Dosa  रवा मसाला डोसा",11:"Plain Dosa  प्लेन डोस",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in s_i:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(n_s_indian)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_s_indian[order]*qat)
                print("YOUR BILL IS:",sum_total)
    elif (ch=="daal") or (ch=="8"):
        print("                M_E_N_U_E                       ")  
        print("""               ###DAL###
        Dal Jeera       दाल जीरा           85/-            1

        Dal Alishan    दाल आलीशान         65/-            2
 
        Dal Muglay     दाल मुगलाय          115/-            3

        Dal Fry        दाल फ्राय हरी मिर्च     115/-            4

        Dal Tadka      दाल तड़का           120/-             5

        Dal Makhani     दाल मखानी          125/-             6

        Dal Yellow      दाल येलो             85/-             7

        Dal Fry         दाल फ्राय             75/-              8
        ******************** TO GO BACK PRESS 900 *************************
        """)
        s_d=[5]
        n_dal={1:85,2:65,3:115,4:115,5:120,6:125,7:85,8:75,900:""} 
        dal={1:"Dal Jeera  दाल जीर",2:"Dal Alishan  दाल आलीशान",3:"Dal Muglay  दाल मुगलाय",4:"Dal Fry   दाल फ्राय",5:"Dal Tadka  दाल तड़क",6:"Dal Makhani  दाल मखानी",7:"Dal Yellow  दाल येलो",8:"Dal Fry  दाल फ्राय ",900:""}
        while (choice!=0):
            order=int(input("ENTER THE FOOD CODE YOU WANT TO ORDER: "))
            if order in s_d:
                print("SORRY THE ITEM IS UNAVALIBLE")
            elif (order==900):
                 break    
            elif (order>len(dal)):
                print("PLEASE ENTER FROM THE MENUE")
            else:
                qat=int(input("ENTER THE NO. OF ORDERS: "))
                sum_total=sum_total+(n_dal[order]*qat)
    else:
        break
w_menu={"chinese":{1:"Hakka Noodles   हक्का नूडल्स",2:"Veg Choumin  वेज चाउमिन",3:"Veg Noodles   वेज नूडल्स",4:"Veg Chopsuey  वेज चोपसी",5:"Veg Fried Rice   वेज फ्राइड राइस",6:"Veg Kofte  वेज कोथे",7:"Veg Manchurian Dry  वेज मंचूरियन ड्राय",8:"Veg Manchurian GREAVY  वेज मंचूरियन ग्रेवी",9:"Chilli Paneer Dry  चिल्ली पनीर ड्राय",10:"Chilli Paneer GREAVY  चिल्ली पनीर ग्रेवी",11:"Paneer Manchurian पनीर मंचूरियन",12:"Chinese Bhel  चायनीस गेल",13:"Gobhi Chili  गोभी चिल्ली",14:"Gobhi Manchurian गोभी मंचूरियन",15:"Paneer Tikka Dry पनीर टिक्का ड्राय",16:"Manchurian Noodles  मंचूरियन नूडल्स",17:"Veg Sizler  वेज सिज़्लर",18:"Chana chili Dry  चना चिल्ली ड्राय",19:"Hani Batato  हनी बाते",20:"Veg MOMOSs  वेज मोमोस",900:""},"dahi":{1:"Plain Dahi  प्लेन दह",2:"Boondi Raita  बुंदी रायता",3:"Fruit Raita  फुटरायता",4:"Pineapple Raita  पाइनापल रायत",5:"Veg Raita  वेज रायता",6:"Aaloo Mint Raita  आलू मिंट रायत",7:"Dahi Fry  दही फाई",8:"Dahi Fry Butter  दही फाई बटर",9:"Dahi Tadka  दही तड़का",900:""},"salad":{1:"Green Salad  ग्रीन सलाद",2:"Kachumar Salad  कचुमर सलाद",3:"Tomato Salad  चेमेवे सलाद",4:"Onion Salad ओनियन सलाद",5:"Peanut Salad  पीनट सलाद",900:""},"papad":{1:"Papad Dry  पापड़ ड्राई ",2:"Papad Bhurji  पापड़ भुजी",3:"Papad Fry  पापड़ फाय",4:"Papad Masala    पापड़ मसाल",5:"Papad Dry Masala पापड़ ड्राय मसाला",900:""},"paneer":{1:"Chhola Paneer खेला पनीर",2:"Paneer Panjabi पनीर पंजाबी",3:"PaneerBhurji पनीरभुर्जी",4:"Mutter Paneer मटर पनीर",5:"PaneerMaharaja पनीरमहाराजा",6:"PaneerPasanda पनीरपसंदा",7:"PalakPaneer पालकपनीर",8:"KadaiPaneer कड़ाईपनीर",9:"ShahiPaneer शाहीपनीर",10:"PaneerLababdar पनीरलबाबदार",11:"PaneerDo Pyaza  पनीरदो प्याजा",12:"PaneerMakhhanwala पनीरमख्खनवाल",13:"PaneerMumtaz पनीरमुमताज",14:"PaneerBadshahil  पनीरबादशाही",15:"KajuPaneer काजूपनीर",16:"Kaju Curry  काजू करी",17:"MalaiKofta मलाईकोफ्ता",900:"" },"italian":{1:"Veg Pizza  वेज पिज्जा ",2:"Cheese Pizza  चीज पिज्जा ",3:"ChinesePizza  चाइनीस पिज्जा ",4:" Veg Burger  वेज बर्गर",5:"Cheese Burger  चीज वर्गर",6:"Onion Pizza  ओनियन पिज्जा",7:" Tomato Pizza  टोमेवे पिज्जा",900:""},"southindian":{1:"Masala Dosa  मसाला डोसा",2:"Shahi Dosa  शाही डोसा",3:"Panir Dosa  पनीर डोस",4:"Mahsur Dosa  महशूर डोसा",5:"Plain Pepar Dosa  प्लेन पेपर डोस",6:"Masala Pepar Dosa   मसाला पेपर डोस",7:"Plain Dosa  प्लेन डोस",8:"Onion Uttapam   ओनियन उत्तपम",9:"Tomoto Uttapam  चेमेवे उत्तपम",10:"Rawa Masala Dosa  रवा मसाला डोसा",11:"Plain Dosa प्लेन डोस",900:""},"dal":{1:"Dal Jeera  दाल जीर",2:"Dal Alishan  दाल आलीशान",3:"Dal Muglay  दाल मुगलाय",4:"Dal Fry   दाल फ्राय",5:"Dal Tadka  दाल तड़क",6:"Dal Makhani  दाल मखानी",7:"Dal Yellow  दाल येलो",8:"Dal Fry  दाल फ्राय",900:""},"1":{1:"Hakka Noodles   हक्का नूडल्स",2:"Veg Choumin  वेज चाउमिन",3:"Veg Noodles   वेज नूडल्स",4:"Veg Chopsuey  वेज चोपसी",5:"Veg Fried Rice   वेज फ्राइड राइस",6:"Veg Kofte  वेज कोथे",7:"Veg Manchurian Dry  वेज मंचूरियन ड्राय",8:"Veg Manchurian GREAVY  वेज मंचूरियन ग्रेवी",9:"Chilli Paneer Dry  चिल्ली पनीर ड्राय",10:"Chilli Paneer GREAVY  चिल्ली पनीर ग्रेवी",11:"Paneer Manchurian पनीर मंचूरियन",12:"Chinese Bhel  चायनीस गेल",13:"Gobhi Chili  गोभी चिल्ली",14:"Gobhi Manchurian गोभी मंचूरियन",15:"Paneer Tikka Dry पनीर टिक्का ड्राय",16:"Manchurian Noodles  मंचूरियन नूडल्स",17:"Veg Sizler  वेज सिज़्लर",18:"Chana chili Dry  चना चिल्ली ड्राय",19:"Hani Batato  हनी बाते",20:"Veg MOMOSs  वेज मोमोस",900:""},"2":{1:"Plain Dahi  प्लेन दह",2:"Boondi Raita  बुंदी रायता",3:"Fruit Raita  फुटरायता",4:"Pineapple Raita  पाइनापल रायत",5:"Veg Raita  वेज रायता",6:"Aaloo Mint Raita  आलू मिंट रायत",7:"Dahi Fry  दही फाई",8:"Dahi Fry Butter  दही फाई बटर",9:"Dahi Tadka  दही तड़का",900:""},"3":{1:"Green Salad  ग्रीन सलाद",2:"Kachumar Salad  कचुमर सलाद",3:"Tomato Salad  चेमेवे सलाद",4:"Onion Salad ओनियन सलाद",5:"Peanut Salad  पीनट सलाद",900:""},"4":{1:"Papad Dry  पापड़ ड्राई ",2:"Papad Bhurji  पापड़ भुजी",3:"Papad Fry  पापड़ फाय",4:"Papad Masala    पापड़ मसाल",5:"Papad Dry Masala पापड़ ड्राय मसाला",900:""},"5":{1:"Chhola Paneer खेला पनीर",2:"Paneer Panjabi पनीर पंजाबी",3:"PaneerBhurji पनीरभुर्जी",4:"Mutter Paneer मटर पनीर",5:"PaneerMaharaja पनीरमहाराजा",6:"PaneerPasanda पनीरपसंदा",7:"PalakPaneer पालकपनीर",8:"KadaiPaneer कड़ाईपनीर",9:"ShahiPaneer शाहीपनीर",10:"PaneerLababdar पनीरलबाबदार",11:"PaneerDo Pyaza  पनीरदो प्याजा",12:"PaneerMakhhanwala पनीरमख्खनवाल",13:"PaneerMumtaz पनीरमुमताज",14:"PaneerBadshahil  पनीरबादशाही",15:"KajuPaneer काजूपनीर",16:"Kaju Curry  काजू करी",17:"MalaiKofta मलाईकोफ्ता",900:"" },"6":{1:"Veg Pizza  वेज पिज्जा ",2:"Cheese Pizza  चीज पिज्जा ",3:"ChinesePizza  चाइनीस पिज्जा ",4:" Veg Burger  वेज बर्गर",5:"Cheese Burger  चीज वर्गर",6:"Onion Pizza  ओनियन पिज्जा",7:" Tomato Pizza  टोमेवे पिज्जा "},"7":{1:"Masala Dosa  मसाला डोसा",900:"",2:"Shahi Dosa  शाही डोसा ",3:" Panir Dosa  पनीर डोस",4:"Mahsur Dosa  महशूर डोसा ",5:"Plain Pepar Dosa  प्लेन पेपर डोस",6:"Masala Pepar Dosa   मसाला पेपर डोस",7:"Plain Dosa  प्लेन डोस ",8:" Onion Uttapam   ओनियन उत्तपम",9:"Tomoto Uttapam  चेमेवे उत्तपम",10:"Rawa Masala Dosa  रवा मसाला डोसा",11:"Plain Dosa  प्लेन डोस",900:""},"8":{1:"Dal Jeera  दाल जीर",2:"Dal Alishan  दाल आलीशान",3:"Dal Muglay  दाल मुगलाय",4:"Dal Fry   दाल फ्राय",5:"Dal Tadka  दाल तड़क",6:"Dal Makhani  दाल मखानी",7:"Dal Yellow  दाल येलो",8:"Dal Fry  दाल फ्राय",900:""},"9":{900:""}}        
Bill=restubill.restubill(sum_total,w_menu,ch,order)
print(Bll)
