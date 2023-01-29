"""My first idea to do python"""
def main():
    """all i want to do"""
    names, univer, got = [], [], {}

    date = {1:"6 มิ.ย.65", 2:"13 มิ.ย.65", 3:"20 มิ.ย.65", 4:"20 มิ.ย.65", 5:"25 มิ.ย.65", \
        6:"27 มิ.ย.65", 7:"27 มิ.ย.65", 8:"27 มิ.ย.65", \

        9:"4 ก.ค.65", 10:"4 ก.ค.65", 11:"11 ก.ค.65", 12:"18 ก.ค.65", \
            
            13:"1 ส.ค.65", 14:"1 ส.ค.65", 15:"8 ส.ค.65"\
            , 16:"8 ส.ค.65", 17:"8 ส.ค.65", 18:"8 ส.ค.65"\
                , 19:"8 ส.ค.65", 20:"8 ส.ค.65", 21:"15 ส.ค.65", 22:"15 ส.ค.65"}
    
    universe = {1:"ม.อุบลราชธานี", 2:"ม.พะเยา", 3:"ม.เชียงใหม่", 4:"ม.นเรศวร", 5:"ม.บูรพา", \
         6:"ม.สงขลานครินทร์", 7:"ม.เกษตรศาสตร์", 8:"ม.ขอนแก่น", \
        
        9:"ม.ศิลปากร", 10:"ม.แม่โจ้", 11:"มรภ.สวนสุนันทา", 12:"ม.พระนครเหนือ", \
            
            13:"เทคโนลาดกระบัง", 14:"มรภ.บ้านสมเด็จ", 15:"ม.พระจอมเกล้าธนบุรี", \
                16:"ม.มหิดล", 17:"ม.ธรรมศาสตร์", 18:"ม.เทคโนโลยีสุรนารี"\
                , 19:"จุฬา", 20:"มศว.", 21:"ม.แม่ฟ้าหลวง", 22:"ม.สวนดุสิต"}
    
    for i in universe:
        print("[%d] %s"%(i, universe[i]))
    
    numloop = int(input("\n!จำนวนเพื่อนที่ต้องการเทียบ [คน]\n\t"))
    print("\nชื่อเพื่อน (name)")
    for i in range(numloop):
        name = input("%d.) "%(i+1))
        names.append(name)
        get = int(input("? มหาวิทยาลัยที่ %s อยู่ [ตัวเลข]? (University)\n\t"%name))
        univer.append(get)
    print()
    for j in range(numloop):
        snames = names[j]
        dates = date[univer[j]]
        got.update({univer[j] : (snames + " " + dates) })

    keys = sorted(got.keys())

    count = ""
    for _ in (got[keys[-1]] + universe[keys[-1]]):
        count += "-"
    print("Your result  ไล่จาก 'มาก' ลงไปหา 'น้อย'")
    print(count)
    for i in keys:
        print("%s %s" %(universe[i], got[i], ))
        if i == keys[-1]:
            pass
        else:
            print("\tv")
    print(count)
main()

### ยังไม่รองรับมหาลัยซ้ำกัน 
