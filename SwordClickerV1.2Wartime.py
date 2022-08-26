import time

import os
import random
import tkinter
#------------------------------------Things To Do-----------------------------------------------#
#1. Create a function which constanlty updates and saves the file data for most scenarios
#2. Change the war sequence so that it repeats with an if statement and lbl.after(1000,warFight)
#3. Create a Radio button system to switch between Sword Types
#4. Create more swords and acheivements
#5. Create Username system

war=[]
# This Creates a directory in the PC
if os.path.exists('C:\SwordMaker'):
    print('Youve played before!')
else:
    print('File Created.')
    os.mkdir('C:\SwordMaker')
    

if os.path.exists('C:\SwordMaker\War'):
    print('Youve played before!')
else:
    print('File Created.')
    os.mkdir('C:\SwordMaker\War')
    

if os.path.exists('C:\SwordMaker\War\WarPeople'):
    print('Youve played before!')
else:
    print('File Created.')
    os.mkdir('C:\SwordMaker\War\WarPeople')
    

if os.path.exists('C:\SwordMaker\War\EnemyPeople'):
    print('Youve played before!')
else:
    print('File Created.')
    os.mkdir('C:\SwordMaker\War\EnemyPeople')
#--------------------------------Wood Files-------------------------------------#
    
# Creates a file for the wood   
if os.path.exists('C:\SwordMaker\Wood.txt'):
    print('Youve played before!')
    woodfile=open('C:\SwordMaker\Wood.txt','r')
    wood=int(woodfile.read())
    
    woodfile.close()
else:
    print('File Created.')
    
    f=open('C:\SwordMaker\Wood.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\Wood.txt','r')
    wood=int(woodfile.read())
    
    woodfile.close()


    
    
# Creates a file for Wooden Swords

if os.path.exists('C:\SwordMaker\WoodSword.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\WoodSword.txt','r')
    woodsword=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\WoodSword.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\WoodSword.txt','r')
    woodsword=int(woodfile.read())
    
    woodfile.close()




#Creates a file for gold made    
if os.path.exists('C:\SwordMaker\Gold.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\Gold.txt','r')
    gold=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\Gold.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\Gold.txt','r')
    gold=int(woodfile.read())
    
    woodfile.close()

    

#Creates a file for Wood Lumberers
if os.path.exists('C:\SwordMaker\AutoClickerWood.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\AutoClickerWood.txt','r')
    autoClickWood=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\AutoClickerWood.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\AutoClickerWood.txt','r')
    autoClickWood=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:\SwordMaker\AutoClickerWSword.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\AutoClickerWSword.txt','r')
    autoClickWSword=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\AutoClickerWSword.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\AutoClickerWSword.txt','r')
    autoClickWSword=int(woodfile.read())
    
    woodfile.close()


    

if os.path.exists('C:\SwordMaker\AutoClickerSWSword.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\AutoClickerSWSword.txt','r')
    autoClickSWSword=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\AutoClickerSWSword.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\AutoClickerSWSword.txt','r')
    autoClickSWSword=int(woodfile.read())
    
    woodfile.close()


    
#---------------------------------Stone Files----------------------------------#
    
#Creates a file for stone
if os.path.exists('C:\SwordMaker\Stone.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\Stone.txt','r')
    stone=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\Stone.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\Stone.txt','r')
    stone=int(woodfile.read())
    
    woodfile.close()

#Stone Sword File
if os.path.exists('C:\SwordMaker\StoneSword.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\StoneSword.txt','r')
    stoneSword=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\StoneSword.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\StoneSword.txt','r')
    stoneSword=int(woodfile.read())
    
    woodfile.close()



    
#Auto Stone Miner
if os.path.exists('C:\SwordMaker\StoneMiner.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\StoneMiner.txt','r')
    stoneMiner=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\StoneMiner.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\StoneMiner.txt','r')
    stoneMiner=int(woodfile.read())
    
    woodfile.close()

    
#Auto Stone Sword Maker
if os.path.exists('C:\SwordMaker\AutoStoneSword.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\AutoStoneSword.txt','r')
    autoStoneSword=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\AutoStoneSword.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\AutoStoneSword.txt','r')
    autoStoneSword=int(woodfile.read())
    
    woodfile.close()





    
#Auto Stone Sword Seller
if os.path.exists('C:\SwordMaker\StoneSwordSell.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\StoneSwordSell.txt','r')
    stoneSwordSell=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\StoneSwordSell.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:\SwordMaker\StoneSwordSell.txt','r')
    stoneSwordSell=int(woodfile.read())
    
    woodfile.close()





#-------------------------------Wood Per Click Files--------------------------------#



if os.path.exists('C:\SwordMaker\woodpc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\woodpc.txt','r')
    wpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\woodpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\woodpc.txt','r')
    wpc=int(woodfile.read())
    
    woodfile.close()






    

if os.path.exists('C:\SwordMaker\woodSwordpc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\woodSwordpc.txt','r')
    wspc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\woodSwordpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\woodSwordpc.txt','r')
    wspc=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:\SwordMaker\goldpc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\goldpc.txt','r')
    gpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\goldpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\goldpc.txt','r')
    gpc=int(woodfile.read())
    
    woodfile.close()






if os.path.exists('C:/SwordMaker/autowoodpc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autowoodpc.txt','r')
    awpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autowoodpc.txt','w+')
    f.write('1')
    f.close()
    
    woodfile=open('C:/SwordMaker/autowoodpc.txt','r')
    awpc=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:/SwordMaker/autowoodSwordpc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autowoodSwordpc.txt','r')
    awspc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autowoodSwordpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:/SwordMaker/autowoodSwordpc.txt','r')
    awspc=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:/SwordMaker/autogoldpc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autogoldpc.txt','r')
    agpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autogoldpc.txt','w+')
    f.write('2')
    f.close()
    woodfile=open('C:/SwordMaker/autogoldpc.txt','r')
    agpc=int(woodfile.read())
    
    woodfile.close()
#-------------------------------Stone Per Click Files--------------------------#

if os.path.exists('C:\SwordMaker\stonepc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\stonepc.txt','r')
    spc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\stonepc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\stonepc.txt','r')
    spc=int(woodfile.read())
    
    woodfile.close()



    

if os.path.exists('C:\SwordMaker\stoneSwordpc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\stoneSwordpc.txt','r')
    sspc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\stoneSwordpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\stoneSwordpc.txt','r')
    sspc=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:\SwordMaker\sgoldpc.txt'):
    print('Youve played before!')
    f=open('C:\SwordMaker\sgoldpc.txt','r')
    sgpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:\SwordMaker\sgoldpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:\SwordMaker\sgoldpc.txt','r')
    sgpc=int(woodfile.read())
    
    woodfile.close()






if os.path.exists('C:/SwordMaker/autostonepc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autostonepc.txt','r')
    aspc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autostonepc.txt','w+')
    f.write('1')
    f.close()
    
    woodfile=open('C:/SwordMaker/autostonepc.txt','r')
    aspc=int(woodfile.read())
    
    woodfile.close()

    

if os.path.exists('C:/SwordMaker/autoStoneSwordpc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autoStoneSwordpc.txt','r')
    asspc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autoStoneSwordpc.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:/SwordMaker/autoStoneSwordpc.txt','r')
    asspc=int(woodfile.read())
    
    woodfile.close()

if os.path.exists('C:/SwordMaker/autosgoldpc.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/autosgoldpc.txt','r')
    asgpc=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/autosgoldpc.txt','w+')
    f.write('2')
    f.close()
    woodfile=open('C:/SwordMaker/autosgoldpc.txt','r')
    asgpc=int(woodfile.read())
    
    woodfile.close()

if os.path.exists('C:/SwordMaker/StoneYes.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/StoneYes.txt','r')
    stoneYes=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/StoneYes.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:/SwordMaker/StoneYes.txt','r')
    stoneYes=int(woodfile.read())
    
    woodfile.close()

#-------------------------------War time Game----------------------------------#

if os.path.exists('C:/SwordMaker/War/War People.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/War People.txt','r')
    for x in f:
        war.append(x)
        
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/War People.txt','w+')
    f.write('')
    
    f.close()
    woodfile=open('C:/SwordMaker/War/War People.txt','r')
    for x in woodfile:
        war.append(x)
    
    
    woodfile.close()

if os.path.exists('C:/SwordMaker/War/War Count.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/War Count.txt','r')
    warCount=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/War Count.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:/SwordMaker/War/War Count.txt','r')
    warCount=int(woodfile.read())
    
    woodfile.close()



if os.path.exists('C:/SwordMaker/War/War Time.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/War Time.txt','r')
    waveTime=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/War Time.txt','w+')
    f.write('180')
    f.close()
    woodfile=open('C:/SwordMaker/War/War Time.txt','r')
    waveTime=int(woodfile.read())
    
    woodfile.close()

if os.path.exists('C:/SwordMaker/War/Wave Num.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/Wave Num.txt','r')
    waveNum=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/Wave Num.txt','w+')
    f.write('1')
    f.close()
    woodfile=open('C:/SwordMaker/War/Wave Num.txt','r')
    waveNum=int(woodfile.read())
    
    woodfile.close()


if os.path.exists('C:/SwordMaker/War/Your Health.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/Your Health.txt','r')
    yourHealth=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/Your Health.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:/SwordMaker/War/Your Health.txt','r')
    yourHealth=int(woodfile.read())
    
    woodfile.close()

if os.path.exists('C:/SwordMaker/War/EnemyHealth.txt'):
    print('Youve played before!')
    f=open('C:/SwordMaker/War/EnemyHealth.txt','r')
    enemyHealth=int(f.read())
    
    f.close()
else:
    print('File Created.')
    f=open('C:/SwordMaker/War/EnemyHealth.txt','w+')
    f.write('0')
    f.close()
    woodfile=open('C:/SwordMaker/War/EnemyHealth.txt','r')
    enemyHealth=int(woodfile.read())
    
    woodfile.close()
    
#-------------------------------Wood Sword Functions---------------------------#
    
def woodclick():
    global wood
    global wpc
    f=open('C:\SwordMaker\Wood.txt','w+')
    g=open('C:\SwordMaker\woodpc.txt','w+')
    wood+=wpc
    if wpc == 1:
        
        if wood >= 300:
            print('You collected 300 wood! Your wood clicks have double the effeincey')
            wpc+=1

    
        
    print(wood)
    

    f.write(str(wood))
    g.write(str(wpc))
    f.close()
    g.close()

def woodswordclick():
    global wood
    global woodsword
    
   
    f=open('C:\SwordMaker\WoodSword.txt','w+')
    g=open('C:\SwordMaker\Wood.txt','w+')
    if wood >= 3:
        woodsword+=1
        wood-=3
        
    if wood < 3:
        print('You dont have enough for this.')
   
    print(woodsword)
    f.write(str(woodsword))  
    g.write(str(wood))
    f.close()
    g.close()

def swordsell():
    global gold
    global woodsword
    global war
    
    f=open('C:\SwordMaker\WoodSword.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    if woodsword >= 1:
        gold+=2
        woodsword-=1
        war.append('1')
        h=open('C:/SwordMaker/War/War People.txt','a')
        h.write('\n')
        h.write('1')
        h.close()
        
    if woodsword < 1:
        print('You dont have enough for this.')
   
    print(gold)
    f.write(str(woodsword))  
    g.write(str(gold))
    f.close()
    g.close()

#----------------------------------Update Function----------------------------#

def update_func():
    global wcost
    global wscost
    global swscost
    global woodPerSec
    global woodSwordPerSec
    global goldPerSec
    global gold
    global stone
    global stoneSword
    global stoneMiner
    global scost
    global stoneYes
    global waveTime
    
    
    if stoneYes ==0:
        if gold >= 500:
            f=open('C:/SwordMaker/StoneYes.txt','w+')
            btnStone.config(state='normal',text='Mine Stone')
            btnStoneSword.config(state='normal',text='Stone Sword')
            btnStoneSell.config(state='normal',text='Sell Sword')
            btnAutoStone.config(text='Stone Drill',state='normal')
            btnAutoStoneSword.config(text='Stone Sword Smith',state='normal')
            btnAutoStoneSell.config(text='Stone Sword Broker',state='normal')
            stoneYes+=1
            f.write(str(stoneYes))
            f.close
        
    wcost=autoClickWood**2

    wscost=(autoClickWSword+10)**2

    swscost=(autoClickSWSword+15)**2

    scost=(stoneMiner+18)**2

    woodPerSec=(autoClickWood*awpc)-(3*(autoClickWSword*awspc))

    woodSwordPerSec=(awspc*autoClickWSword)-autoClickSWSword

    goldPerSec=autoClickSWSword*2
    
    lblwood.config(text="Wood: "+str(wood))
    lblwoodsword.config(text="Wood Sword: "+str(woodsword))
    lblgold.config(text="Gold: "+str(gold))
    lblwoodAutoClick.config(text="Wood Choppers: "+str(autoClickWood))
    lblwoodAutoCost.config(text="Cost: "+str(wcost)+' gold')
    lblwoodAutoSword.config(text="Wood Sword Smiths: "+str(autoClickWSword))
    lblwoodAutoSwordCost.config(text="Cost: "+str(wscost)+' gold')
    lblwoodAutoGold.config(text="Wood Sword Brokers: "+str(autoClickSWSword))
    lblwoodAutoGoldCost.config(text="Cost: "+str(swscost)+' gold')
    
    lblWoodPerSec.config(text="Wood/sec: "+str(woodPerSec))

    lblWoodSwordPerSec.config(text="Wood Sword/sec: "+str(woodSwordPerSec))

    lblGoldPerSec.config(text="Gold/sec: "+str(goldPerSec))

    lblStone.config(text="Stone: "+str(stone))
    
    lblStoneSword.config(text="Stone Sword: "+str(stoneSword))

    lblStoneAuto.config(text="Stone Miner: "+str(stoneMiner))

    lblStoneAutoCost.config(text="Cost: "+str(scost))

    lblWaveTime.config(text="Time: "+str(waveTime))


    
    lblwood.after(1, update_func)

def WaveTimes():
    global waveTime
    global warCount
    global waveNum
    global war
    global yourHealth
    global enemyHealth
    global waveEnd
    if waveTime == 0:
        
        for i in war:
            if i == '1':
                warCount+=1
                hp=5
                yourHealth+=hp
                
                attack=5
                f=open('C:/SwordMaker/War/WarPeople/'+str(warCount)+'.txt','w+')
                f.write(str(hp))
                f.write("\n")
                f.write(str(attack))
                f.close()
                
        
        enemies=waveNum*3
        for j in range(1,(enemies+1)):
            enemychoice=random.choice(['1','2'])
            if enemychoice == '1':
                ehp=4
                enattack=3
                enemyHealth+=ehp
                g=open('C:/SwordMaker/War/EnemyPeople/'+str(j)+'.txt','w+')
                g.write(str(ehp))
                g.write("\n")
                g.write(str(enattack))
                g.close()

            if enemychoice == '2':
                ehp=7
                enattack=6
                enemyHealth+=ehp
                g=open('C:/SwordMaker/War/EnemyPeople/'+str(j)+'.txt','w+')
                g.write(str(ehp))
                g.write("\n")
                g.write(str(enattack))
                g.close()
        waveEnd=False
        waveFight()
        waveTime=60
        f=open('C:/SwordMaker/War/War Time.txt','w+')
        f.write(str(waveTime))
        f.close()
        warcount=0
    if waveTime > 0:
        waveTime-=1
        f=open('C:/SwordMaker/War/War Time.txt','w+')
        f.write(str(waveTime))
        f.close()
        lblWaveTime.after(1000, WaveTimes)
        
        


def waveFight():
    global warCount
    global yourHealth
    global enemyHealth
    global enemies
    global waveEnd
    global war
    attacker=1
    enattacker=1

    while waveEnd == False:
        attack=False
        enemy=False
        while attack==False:
            
            
            if os.path.exists('C:/SwordMaker/War/WarPeople/'+str(attacker)+'.txt'):
                  f=open('C:/SwordMaker/War/WarPeople/'+str(attacker)+'.txt','r')
                  playerHP=int(f.readline())
                  playerAtt=int(f.readline())
                  attack=True
                  f.close()
            else:
                  attacker+=1
                  
        while enemy == False:
            
            if os.path.exists('C:/SwordMaker/War/EnemyPeople/'+str(enattacker)+'.txt'):
                  f=open('C:/SwordMaker/War/EnemyPeople/'+str(enattacker)+'.txt','r')
                  enemyHP=int(f.readline())
                  enemyAtt=int(f.readline())
                  enemy=True
                  f.close()
            else:
                  enattacker+=1
        enemyHP-=playerAtt
        playerHP-=enemyAtt
        
        
        if playerHP <= 0:
            os.remove('C:/SwordMaker/War/WarPeople/'+str(attacker)+'.txt')
            enemyAtt+=playerHP
        if enemyHP <= 0:
            os.remove('C:/SwordMaker/War/EnemyPeople/'+str(enattacker)+'.txt')
            playerAtt+=enemyHP

        yourHealth-=enemyAtt
        enemyHealth-=playerAtt
        f=open('C:/SwordMaker/War/Your Health.txt','w+')
        f.write(str(yourHealth))
        f.close()
        f=open('C:/SwordMaker/War/EnemyHealth.txt','w+')
        f.write(str(enemyHealth))
        f.close()
        if enemyHealth <=0:
            waveEnd=True
            war=[]
        if yourHealth <= 0:
            waveEnd=True
            war=[]
        f=open('C:/SwordMaker/War/War People.txt','w+')
        f.write('')
        f.close()

#---------------------------------Wood Auto Clicker Functions------------------#
# Hey look a change was made here
def AutoClickWood():
    global gold
    global awpc
    global wcost
    global autoClickWood
    
    f=open('C:\SwordMaker\AutoClickerWood.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    h=open('C:/SwordMaker/autowoodpc.txt','w+')
    if gold >= wcost:
        autoClickWood+=1
        gold -= wcost
        
        if autoClickWood == 10:
            print('You have made 10 choppers. They now produce twice as much!')
            awpc+=1
        
        
    else:
        print('You do not have enough.')

    f.write(str(autoClickWood))  
    g.write(str(gold))
    h.write(str(awpc))
    f.close()
    g.close()
    h.close()

def AutoClickWSword():
    global gold
    global awspc
    global wscost
    global autoClickWSword

    pleaseHelpMe = 1
    f=open('C:\SwordMaker\AutoClickerWSword.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    
    if gold >= wscost:
        autoClickWSword+=1
        gold-=wscost
        if autoClickWSword == 10:
            print('Wow you hired 10 Wooden Sword Smiths. Each Sword Smith Doubles there production!')
            awspc+=1
        
    else:
        print('You do not have enough.')
    
    
        

    f.write(str(autoClickWSword))  
    g.write(str(gold))
    f.close()
    g.close()

def AutoClickGold():
    global gold
    
    global swscost
    global autoClickSWSword
    
    f=open('C:\SwordMaker\AutoClickerSWSword.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    
    if gold >= swscost:
        autoClickSWSword+=1
        gold-=swscost
        
        
    else:
        print('You do not have enough.')

    f.write(str(autoClickSWSword))  
    g.write(str(gold))
    f.close()
    g.close()


#----------------------------Auto Clicker Update Function----------------------#
def AutoClickerUpdate():
    global autoClickWood
    global wood
    global window
    global gold
    global woodsword
    global autoClickWSword
    global autoClickSWSword
    global awspc
    global awpc
    global stone
    global stoneMiner
    global war
    f=open('C:\SwordMaker\Wood.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    h=open('C:\SwordMaker\WoodSword.txt','w+')
    wood+= autoClickWood*awpc
    
    if autoClickWSword >= 1:
        for d in range(0,(autoClickWSword*awspc)):
            if wood >=3:
                wood-=3
                woodsword+=1
                
    if autoClickSWSword >=1:        
        for i in range(0,autoClickSWSword):
            if woodsword >=1:
                woodsword-=1
                gold+=2
                war.append('1')
                a=open('C:/SwordMaker/War/War People.txt','a')
                a.write('\n')
                a.write('1')
                a.close()
    stone+=stoneMiner
            
    
    f.write(str(wood))
    h.write(str(woodsword))
    g.write(str(gold))
    
    f.close()
    h.close()
    g.close()
    lblwood.after(1000, AutoClickerUpdate)
    



#-----------------------------Stone Functions----------------------------------#
def stoneClick():
    global stone
    global spc
    f=open('C:\SwordMaker\Stone.txt','w+')
    stone+=spc

    f.write(str(stone))
    f.close

def stoneSwordClick():
    global stone
    global wood
    global stoneSword
    global sspc
    f=open('C:\SwordMaker\Stone.txt','w+')
    g=open('C:\SwordMaker\StoneSword.txt','w+')
    h=open('C:\SwordMaker\Wood.txt','w+')

    if stone >= 10 and wood >=3:
        stone-=10
        wood-=3
        stoneSword+=sspc
    else:
        print(" ")

    f.write(str(stone))
    g.write(str(stoneSword))
    h.write(str(wood))

    f.close()
    g.close()
    h.close()
    
def stoneSwordSells():
    global stoneSword
    global sgpc
    global gold
    g=open('C:\SwordMaker\StoneSword.txt','w+')
    h=open('C:\SwordMaker\Gold.txt','w+')
    
    if stoneSword >= 1:
        gold+=10*sgpc
        stoneSword-=1
        
    if stoneSword < 1:
        print('You dont have enough for this.')

    g.write(str(stoneSword))
    h.write(str(gold))
    g.close()
    h.close
def stoneAutoClick():#--Allows you to buy stone collectors--#
    
    global gold
   
    global scost
    global stoneMiner
    
    f=open('C:\SwordMaker\StoneMiner.txt','w+')
    g=open('C:\SwordMaker\Gold.txt','w+')
    
    if gold >= scost:
        stoneMiner+=1
        gold -= scost
        
        
        
        
    else:
        print('You do not have enough.')

    f.write(str(stoneMiner))  
    g.write(str(gold))
    
    f.close()
    g.close()
    
def stoneSwordAutoClick():
    print('a')
def stoneSwordAutoSell():
    print('a')

def updateFiles():#--------------Update all your files----#
    a=open('C:\SwordMaker\Wood.txt','w+')
    b=open('C:\SwordMaker\WoodSword.txt','w+')
    
    
    c=open('C:\SwordMaker\AutoClickerWood.txt','w+')
    d=open('C:\SwordMaker\AutoClickerWSword.txt','w+')
    e=open('C:\SwordMaker\AutoClickerSWSword.txt','w+')
    f=open('C:\SwordMaker\Stone.txt','w+')
    g=open('C:\SwordMaker\StoneSword.txt','w+')
    h=open('C:\SwordMaker\StoneMiner.txt','w+')
    i=open('C:\SwordMaker\AutoStoneSword.txt','w+')
    j=open('C:\SwordMaker\StoneSwordSell.txt','w+')
    k=open('C:\SwordMaker\woodpc.txt','w+')
    l=open('C:\SwordMaker\woodSwordpc.txt','w+')
    m=open('C:\SwordMaker\goldpc.txt','w+')
    n=open('C:/SwordMaker/autowoodpc.txt','w+')
    o=open('C:/SwordMaker/autowoodSwordpc.txt','w+')
    p=open('C:/SwordMaker/autogoldpc.txt','w+')
    q=open('C:\SwordMaker\stonepc.txt','w+')
    r=open('C:\SwordMaker\stoneSwordpc.txt','w+')
    s=open('C:\SwordMaker\sgoldpc.txt','w+')
    t=open('C:/SwordMaker/autostonepc.txt','w+')
    u=open('C:/SwordMaker/autoStoneSwordpc.txt','w+')
    v=open('C:/SwordMaker/autosgoldpc.txt','w+')
    w=open('C:/SwordMaker/StoneYes.txt','w+')
    x=open('C:/SwordMaker/War/War Count.txt','w+')
    y=open('C:/SwordMaker/War/Wave Num.txt','w+')
    z=open('C:/SwordMaker/War/Your Health.txt','w+')
    aa=open('C:/SwordMaker/War/EnemyHealth.txt','w+')
    bb=open('C:\SwordMaker\Gold.txt','w+')

    a.write()
    b.write()
    c.write()
    d.write()
    e.write()
    f.write()
    g.write()
    h.write()
    i.write()
    j.write()
    k.write()
    l.write()
    m.write()
    n.write()
    o.write()
    p.write()
    q.write()
    r.write()
    s.write()
    t.write()
    u.write()
    v.write()
    w.write()
    x.write()
    y.write()
    z.write()
    aa.write()
    bb.write()
    
    
#------------------------------Other Variables---------------------------------#
wcost=autoClickWood**2

wscost=(autoClickWSword+10)**2

swscost=(autoClickSWSword+15)**2

scost=(stoneMiner+18)**2

sscost=(autoStoneSword+22)**2

ssscost=(stoneSwordSell+25)**2

woodPerSec=(autoClickWood*awpc)-(3*(autoClickWSword*awspc))

woodSwordPerSec=(awspc*autoClickWSword)-autoClickSWSword

goldPerSec=autoClickSWSword*2

window= tkinter.Tk()
#draw the window and start the application

#set window size
window.title('Robot Interface')
window.geometry("1000x900")
window.config(bg='white')



btnup=tkinter.Button(window, text="Collect wood", bg='lightblue', command = woodclick)
btndown=tkinter.Button(window, text="Create Sword", bg='lightblue',command = woodswordclick)
btnleft=tkinter.Button(window, text="Sell Sword", bg='lightblue', command=swordsell)


btnAutoWood=tkinter.Button(window, text="Wood Chopper", bg='lightblue', command = AutoClickWood)

btnAutoWSword=tkinter.Button(window, text="Wood Sword Smith", bg='lightblue', command = AutoClickWSword)

btnAutoGold=tkinter.Button(window, text="Wood Sword Broker", bg='lightblue', command = AutoClickGold)


btnStone=tkinter.Button(window, text="???", bg='lightblue', command=stoneClick)

btnStoneSword=tkinter.Button(window, text="???", bg='lightblue', command=stoneSwordClick)

btnStoneSell=tkinter.Button(window, text="???", bg='lightblue', command=stoneSwordSells)


btnAutoStone=tkinter.Button(window, text="???", bg='lightblue', command=stoneAutoClick)

btnAutoStoneSword=tkinter.Button(window, text="???", bg='lightblue')

btnAutoStoneSell=tkinter.Button(window, text="???", bg='lightblue')


lblwood=tkinter.Label(window, text="Wood: "+str(wood))

lblwoodsword=tkinter.Label(window, text="Wood Sword: "+str(woodsword))

lblgold=tkinter.Label(window, text="Gold: "+str(gold))

lblwoodAutoClick=tkinter.Label(window, text="Wood Choppers: "+str(autoClickWood))

lblwoodAutoCost=tkinter.Label(window, text="Cost: "+str(wcost))

lblwoodAutoSword=tkinter.Label(window, text="Wood Sword Smiths: "+str(autoClickWSword))

lblwoodAutoSwordCost=tkinter.Label(window, text="Cost: "+str(wscost))

lblwoodAutoGold=tkinter.Label(window, text="Wood Sword Brokers: "+str(autoClickSWSword))

lblwoodAutoGoldCost=tkinter.Label(window, text="Cost: "+str(swscost))

lblWoodPerSec=tkinter.Label(window, text="Wood/sec: "+str(woodPerSec))

lblWoodSwordPerSec=tkinter.Label(window, text="Wood Sword/sec: "+str(woodSwordPerSec))

lblGoldPerSec=tkinter.Label(window, text="Gold/sec: "+str(goldPerSec))

lblStone=tkinter.Label(window, text="Stone: "+str(stone))

lblStoneSword=tkinter.Label(window, text="Stone Sword: "+str(stoneSword))

lblStoneAuto= tkinter.Label(window, text="Stone Miners: "+str(stoneMiner))

lblStoneAutoCost=tkinter.Label(window, text="Cost: "+str(scost)+' gold')

lblWave= tkinter.Label(window, text="Wave: "+str(waveNum))

lblWaveTime= tkinter.Label(window, text="Time: "+str(waveTime))

lblYourArmyHealth=tkinter.Label(window, text="Your Health: "+str(yourHealth))

lblTheirArmyHealth=tkinter.Label(window, text="Enemy Health: "+str(enemyHealth))

update_func()
AutoClickerUpdate()
WaveTimes()


btnup.place(x=30,y= 100)
btnup.config(width=10, height=5)
btndown.place(x=30,y=200)
btndown.config(width=10, height=5)
btnleft.place(x=30,y=300)
btnleft.config(width=10, height=5)

btnAutoWood.place(x=30,y=450)
btnAutoWood.config(width=10, height=1)
btnAutoWSword.place(x=30,y=500)
btnAutoWSword.config(width=10, height=1)
btnAutoGold.place(x=30,y=550)
btnAutoGold.config(width=10, height=1)

btnStone.place(x=290,y=100)
btnStoneSword.place(x=290,y=200)
btnStoneSell.place(x=290,y=300)
btnAutoStone.place(x=290,y=400)
btnAutoStoneSword.place(x=290,y=500)
btnAutoStoneSell.place(x=290,y=550)

btnStone.config(state='disabled', width=10, height=5)
btnStoneSword.config(state='disabled',width=10, height=5)
btnStoneSell.config(state='disabled', width=10, height=5)
btnAutoStone.config(state='disabled',width=10, height=2)
btnAutoStoneSword.config(state='disabled',width=10, height=1)
btnAutoStoneSell.config(state='disabled',width=10, height=1)



lblwood.place(x=150,y=10)

lblwoodsword.place(x=150,y=50)

lblgold.place(x=150,y=90)

lblwoodAutoClick.place(x=150,y=130)

lblwoodAutoCost.place(x=150,y=170)

lblwoodAutoSword.place(x=150,y=190)

lblwoodAutoSwordCost.place(x=150,y=210)

lblwoodAutoGold.place(x=150,y=230)

lblwoodAutoGoldCost.place(x=150,y=250)

lblWoodPerSec.place(x=150,y=600)

lblWoodSwordPerSec.place(x=150,y=630)

lblGoldPerSec.place(x=150,y=660)

lblStone.place(x=370,y=10)

lblWaveTime.place(x=700,y=550)

lblWave.place(x=700,y=580)

lblYourArmyHealth.place(x=700,y=610)

lblTheirArmyHealth.place(x=700,y=640)

window.mainloop()



    

    


