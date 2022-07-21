from threading import Thread
import keyboard,time,analyzer
from time import sleep
__import__('sys').stdin=open('input.txt','r')#sys.__stdin__
#__import__('sys').stdout=open('output.txt','w')
startoffset=float(input())
name=input()
filename_=input()
filename=f'{name}\\{filename_}.adofai'
timlist_old=[0.0]+analyzer.analyze(filename)[0]
mapoffset=analyzer.analyze(filename)[1]
timlist_old2=timlist_old.copy()
'''

'''
timlist=[]
keylist=[]
isrighthand=True
lefthand=['a','s','d','f','v','g']
righthand=[';','l','k','j','n','h']
lefthand_unavail1=[['a','s','d','v','g'],['a','s','v','g'],['v','g']]
righthand_unavail1=[[';','l','k','n','h'],[';','l','n','h'],['n','h']]
onekey_maxbpm=600
K1MAX=1/(onekey_maxbpm/60)
K2MAX=K1MAX/2
K4MAX=K1MAX/4
K8MAX=K1MAX/8
# Starting from tile 1 -> J should be used -> spacebar (tweaks)
for x in range(len(timlist_old)):
    if x==0:
        keylist.append(righthand[3])
        continue
    # X Changing hands before the end
    elif isrighthand==True:
        # RH #
        if timlist_old[x]>=K2MAX:
            # 2K #
            '''
            ABLE FACTORS:
            Pressed J (irh=True) (related to righthand) -> to F (irh=false)
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed righthand (irh=True) (i.e. 4 64Beats) -> to F (irh=false)
            '''
            if keylist[-1] in righthand or keylist[-1] in righthand_unavail1[0]: # First Factor
                isrighthand=False
                keylist.append(lefthand[3])
            elif keylist[-1] in lefthand: # Second Factor
                isrighthand=True
                keylist.append(righthand[3])
            else:
                print('error in r2K'+f' {keylist[-1]} {len(keylist)}')
        elif K4MAX<=timlist_old[x] and timlist_old[x]<K2MAX:
            # 4K #
            '''
            ABLE FACTORS:
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed J (irh=True) -> to K (irh=True)
            Pressed K (irh=True) (related to righthand) -> to F (irh=false)
            Pressed righthand (irh=True) -> to F (irh=false)
            '''
            if keylist[-1] in lefthand: # First Factor
                isrighthand=True
                keylist.append(righthand[3])
            elif keylist[-1]==righthand[3]: # Second Factor
                keylist.append(righthand[2])
                isrighthand=True
            elif keylist[-1] in righthand or keylist[-1] in righthand_unavail1[1]: # Third Factor
                keylist.append(lefthand[3])
                isrighthand=False
            else:
                print('error in r4K'+f' {keylist[-1]} {len(keylist)}')
        elif K8MAX<=timlist_old[x] and timlist_old[x]<K4MAX:
            # 8K #
            '''
            ABLE FACTORS:
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed J (irh=True) -> to K (irh=True)
            Pressed K (irh=True) -> to L (irh=True)
            Pressed L (irh=True) -> to ; (irh=True)
            Pressed ; (irh=True) -> to F (irh=false)
            '''
            if keylist[-1] in lefthand: # First Factor
                isrighthand=True
                keylist.append(righthand[3])
            elif keylist[-1]==righthand[3]: # Second Factor
                isrighthand=True
                keylist.append(righthand[2])
            elif keylist[-1]==righthand[2]: # Third Factor
                isrighthand=True
                keylist.append(righthand[1])
            elif keylist[-1]==righthand[1]: # Fourth Factor
                isrighthand=True
                keylist.append(righthand[0])
            elif keylist[-1]==righthand[0] or keylist[-1] in righthand_unavail1[2]: # Fifth Factor
                keylist.append(lefthand[3])
                isrighthand=False
            else:
                print('error in r8K'+f' {keylist[-1]} {len(keylist)}')
        else:
            # 12K #
            '''
            ABLE FACTORS:
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed J (irh=True) -> to K (irh=True)
            Pressed K (irh=True) -> to L (irh=True)
            Pressed L (irh=True) -> to ; (irh=True)
            Pressed ; (irh=True) -> to H (irh=True)
            Pressed H (irh=True) -> to N (irh=True)
            Pressed N (irh=True) -> to F (irh=False)
            '''
            if keylist[-1] in lefthand: # First Factor
                isrighthand=True
                keylist.append(righthand[3])
            elif keylist[-1]==righthand[3]: # Second Factor
                isrighthand=True
                keylist.append(righthand[2])
            elif keylist[-1]==righthand[2]: # Third Factor
                isrighthand=True
                keylist.append(righthand[1])
            elif keylist[-1]==righthand[1]: # Fourth Factor
                isrighthand=True
                keylist.append(righthand[0])
            elif keylist[-1]==righthand[0]: # Fifth Factor
                isrighthand=True
                keylist.append(righthand[4])
            elif keylist[-1]==righthand[4]: # Sixth Factor
                isrighthand=True
                keylist.append(righthand[5])
            elif keylist[-1]==righthand[5]: # Seventh Factor
                isrighthand=False
                keylist.append(lefthand[3])
            else:
                print('error in r12K'+f' {keylist[-1]} {len(keylist)}')
    elif isrighthand==False:
        # RH #
        if timlist_old[x]>=K2MAX:
            # 2K #
            '''
            ABLE FACTORS:
            Pressed lefthand (irh=false) -> to J (irh=True)
            Pressed righthand (irh=True) -> to F (irh=false)
            '''
            if keylist[-1] in lefthand or keylist[-1] in lefthand_unavail1[0]: # First Factor
                isrighthand=True
                keylist.append(righthand[3])
            elif keylist[-1] in righthand: # Second Factor
                isrighthand=False
                keylist.append(lefthand[3])
            else:
                print('error in l2K'+f' {keylist[-1]} {len(keylist)}')
        elif K4MAX<=timlist_old[x] and timlist_old[x]<K2MAX:
            # 4K #
            '''
            ABLE FACTORS:
            Pressed righthand (irh=false) -> to F (irh=false)
            Pressed F (irh=false) -> to D (irh=false)
            Pressed D (irh=false) (related to lefthand) -> to J (irh=True)
            Pressed lefthand (irh=false) -> to J (irh=True)
            '''
            if keylist[-1] in righthand: # First Factor
                isrighthand=False
                keylist.append(lefthand[3])
            elif keylist[-1]==lefthand[3]: # Second Factor
                keylist.append(lefthand[2])
                isrighthand=False
            elif keylist[-1] in lefthand or keylist[-1] in lefthand_unavail1[1]: # Third Factor
                keylist.append(righthand[3])
                isrighthand=True
            else:
                print('error in l4K'+f' {keylist[-1]} {len(keylist)}')
        elif K8MAX<=timlist_old[x] and timlist_old[x]<K4MAX:
            # 8K #
            '''
            ABLE FACTORS:
            Pressed righthand (irh=false) -> to F (irh=false)
            Pressed F (irh=false) -> to D (irh=false)
            Pressed D (irh=false) -> to S (irh=false)
            Pressed S (irh=false) -> to A (irh=false)
            Pressed A (irh=false) -> to J (irh=True)
            '''
            if keylist[-1] in righthand or keylist[-1] in lefthand_unavail1[2]: # First Factor
                isrighthand=True
                keylist.append(lefthand[3])
            elif keylist[-1]==lefthand[3]: # Second Factor
                keylist.append(lefthand[2])
            elif keylist[-1]==lefthand[2]: # Third Factor
                keylist.append(lefthand[1])
            elif keylist[-1]==lefthand[1]: # Fourth Factor
                keylist.append(lefthand[0])
            elif keylist[-1]==lefthand[0]: # Fifth Factor
                keylist.append(righthand[3])
                isrighthand=False
            else:
                print('error in l8K'+f' {keylist[-1]} {len(keylist)}')
        else:
            # 12K #
            '''
            ABLE FACTORS:
            Pressed righthand (irh=false) -> to F (irh=false)
            Pressed F (irh=False) -> to D (irh=False)
            Pressed D (irh=False) -> to S (irh=False)
            Pressed S (irh=False) -> to A (irh=False)
            Pressed A (irh=False) -> to G (irh=False)
            Pressed G (irh=False) -> to V (irh=False)
            Pressed V (irh=False) -> to J (irh=True)
            '''
            if keylist[-1] in righthand: # First Factor
                isrighthand=False
                keylist.append(lefthand[3])
            elif keylist[-1]==lefthand[3]: # Second Factor
                isrighthand=False
                keylist.append(lefthand[2])
            elif keylist[-1]==lefthand[2]: # Third Factor
                isrighthand=False
                keylist.append(lefthand[1])
            elif keylist[-1]==lefthand[1]: # Fourth Factor
                isrighthand=False
                keylist.append(lefthand[0])
            elif keylist[-1]==lefthand[0]: # Fifth Factor
                isrighthand=False
                keylist.append(lefthand[4])
            elif keylist[-1]==lefthand[4]: # Sixth Factor
                isrighthand=False
                keylist.append(lefthand[5])
            elif keylist[-1]==lefthand[5]: # Seventh Factor
                isrighthand=True
                keylist.append(righthand[3])
            else:
                print('error in l12K'+f' {keylist[-1]} {len(keylist)}')
''' Lower Code is Exit code for checking keys. COMMENTIZE IT'''
#exit(0)
'''
   660BPM(Beats Per Minute)
-> 11BPS(Beats Per Second)
-> MAX 0.0909090909 SPB(Secs Per Beat)
-> MAX 0.04545454545 SPB in 2K
-> MAX 0.02272727272 SPB in 4K
-> MAX 0.01136363636 SPB in 8K Till Here
'''
for x in range(len(timlist_old2)):timlist.append(sum(timlist_old2[0:x+1]))
#낙서터:
def samehand(prev,nextt):
    #print(prev,nextt,True if ((prev in lefthand and nextt in lefthand) or (prev in righthand and nextt in righthand)) else False)
    return True if ((prev in lefthand and nextt in lefthand) or (prev in righthand and nextt in righthand)) else False

presstime=[]
for x in range(0,len(timlist)-2):
    if x==0:
        if samehand(keylist[x],keylist[x+1]):
            presstime.append(timlist_old[x+1]*(2/3))
        else:
            presstime.append(0.05)
    else:
        if samehand(keylist[x],keylist[x+1]):
            presstime.append(timlist_old[x+1]+timlist_old[x+2]*(2/3))
        else:
            presstime.append(timlist_old[x+1]*(2/3))
presstime.append(timlist_old[len(timlist)-1]*(2/3))
presstime.append(1)

def presers(key,x):
    global presstime
    keyboard.press(key)
    sleep(presstime[x])
    keyboard.release(key)
def do(x):
    global timlist,keylist
    time.sleep(timlist[x]-time.time()+start if timlist[x]-time.time()+start>=0 else timlist[x])
    Thread(target=presers,args=(keylist[x],x,)).start()

#for x in range(len(timlist)):timlist[x]*=6
''' Upper code is for DEBUG -> COMMENTIZE IT '''
'''
2939 3939

'''
print('A Dance of Fire and Ice 탭으로 이동해주세요.')
while not keyboard.is_pressed('space'):continue
time.sleep(startoffset/1000)
start=time.time()
for x in range(len(timlist)):
    Thread(target=do,args=(x,)).start()