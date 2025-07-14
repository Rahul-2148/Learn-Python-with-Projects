warrior_name = "Thor"
warrior_health = 100
warrior_attack = 50

mage_name = "Gandalf"
mage_health = 80
mage_attack = 70

def attack_warrior():
    print(f'Warrior attacks with power', warrior_attack)
    
def attack_mage():
    print(f"Mage attacks with power", mage_attack)
    
attack_warrior()
attack_mage()


'''
run toh sahi se kr rha but, ab is code me problem kya h wo samjho, sabse pahle h 
i. Redundant code -> it means ki har character ko hame yaha pr separate variable dena pad rha h aur separate function bna kr usko define krna pad rha h 

ii. Hard to expand -> agar maan lo hame 2-3 aur character ko add krna h toh sabkuch name, health etc wapas add krna hoga aur function bna kr usko define krna hoga

iii. No structured -> yani ko code kafi messi lg rha h aur cod kafi difficult lg rha h agar mai characters aur badhata hu toh is code ko main & modify krne me kafi jyada problem hogi 

To ye sab problem ko solve krne ke liye OOP laya gya h 
'''