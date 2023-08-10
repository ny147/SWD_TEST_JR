
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
thai_num = ["ศูนย์","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
unit = ["","สิบ","ร้อย","พัน","หมื่น","แสน","ล้าน"]

def thai_num_rule(num,u):
    strnum_con = thai_num[num]
    unit_con  = unit[u]
    if( num == 2 and u == 1):
        strnum_con = "ยี่"
    elif(num == 1 and u == 0):
        strnum_con = 'เอ็ด'
    elif(num == 0):
        strnum_con = ''
        unit_con = ''
    elif(num == 1 and u == 1):
        strnum_con = ''
    return strnum_con + unit_con
    


def thai2num(num):
    strnum = str(num)
    result = ''
    decimalFlag = False
    if('.' in strnum):
        strnum,strdecimal = strnum.split('.')
        decimalFlag = True
    
    #  integer convert
    if (len(strnum)==1):
        return thai_num[num]
    for i in range(0,len(strnum)):
        result +=  thai_num_rule(int(strnum[i]),(len(strnum) - i-1))
    

    #  decimal convert 
    if(decimalFlag):
        result += 'จุด'
        for i in range(0,len(strdecimal)):
            result += thai_num[int(strdecimal[i])]
    return result


getnumber = input('enter number : ')
print(thai2num(getnumber))