timlist_old=[] # Time list,(i.e. [0, 0.0390625, 0.0390625, 0.0390625, 1.1328124623870863, 1.25, 0.9375, 1.5625, 1.25, 1.25, 0.46875, 0.46875, 1.5625, 1.25, 1.25, 0.46875, 0.46875, 1.5625, 1.25, 1.25, 1.25, 0.3125, 0.15625, 0.15625, 0.3125, 0.3125,...])
keylist=[] #Key list,(i.e. ['J', 'K', 'F', 'D', 'J', 'F', 'J', 'F', 'J',...])
K2MAX=0.04545454545 # The Limit of keyboard key with 2K
K4MAX=0.02272727272 # The Limit of keyboard key with 4K
K8MAX=0 # Unused
lefthand=['A','S','D','F'] # Keys with Left Hand
righthand=['J','K','L',';'] # Keys with Right Hand
for x in range(len(timlist_old)):
    if x==0:
        keylist.append('J')
        continue
    # X Changing hands before the end
    if isrighthand==True:
        # RH #
        if timlist_old[x]>=K2MAX:
            # 2K #
            '''
            ABLE FACTORS:
            Pressed J (irh=True) (related to righthand) -> to F (irh=false)
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed righthand (irh=True) (i.e. 4 64Beats) -> to F (irh=false)
            '''
            if keylist[-1] in righthand: # First Factor
                isrighthand=False
                keylist.append('F')
            elif keylist[-1] in lefthand: # Second Factor
                isrighthand=True
                keylist.append('J')
            else:
                print('error in r2K'+f' {keylist[-1]} {len(keylist)}')
        elif timlist_old[x]>=K4MAX:
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
                keylist.append('J')
            elif keylist[-1]=='J': # Second Factor
                keylist.append('K')
                isrighthand=True
            elif keylist[-1] in righthand: # Third Factor
                keylist.append('F')
                isrighthand=False
            else:
                print('error in r4K'+f' {keylist[-1]} {len(keylist)}')
        else:
            # 8K #
            '''
            fdsajkl;
            ABLE FACTORS:
            Pressed lefthand (irh=True) -> to J (irh=True)
            Pressed J (irh=True) -> to K (irh=True)
            Pressed K (irh=True) -> to L (irh=True)
            Pressed L (irh=True) -> to ; (irh=True)
            Pressed ; (irh=True) -> to F (irh=false)
            '''
            if keylist[-1] in lefthand: # First Factor
                isrighthand=True
                keylist.append('J')
            elif keylist[-1]=='J': # Second Factor
                isrighthand=True
                keylist.append('K')
            elif keylist[-1]=='K': # Third Factor
                isrighthand=True
                keylist.append('L')
            elif keylist[-1]=='L': # Fourth Factor
                isrighthand=True
                keylist.append(';')
            elif keylist[-1]==';': # Fifth Factor
                keylist.append('F')
                isrighthand=False
            else:
                print('error in r8K'+f' {keylist[-1]} {len(keylist)}')
    if isrighthand==False:
        # RH #
        if timlist_old[x]>=K2MAX:
            # 2K #
            '''
            ABLE FACTORS:
            Pressed lefthand (irh=false) -> to J (irh=True)
            Pressed righthand (irh=True) -> to F (irh=false)
            '''
            if keylist[-1] in lefthand: # First Factor
                isrighthand=True
                keylist.append('J')
            elif keylist[-1] in righthand: # Second Factor
                isrighthand=False
                keylist.append('F')
            else:
                print('error in l2K'+f' {keylist[-1]} {len(keylist)}')
        elif timlist_old[x]>=K4MAX:
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
                keylist.append('F')
            elif keylist[-1]=='F': # Second Factor
                keylist.append('D')
                isrighthand=False
            elif keylist[-1] in lefthand: # Third Factor
                keylist.append('J')
                isrighthand=True
            else:
                print('error in l4K'+f' {keylist[-1]} {len(keylist)}')
        else:
            # 8K #
            '''
            fdsajkl;
            ABLE FACTORS:
            Pressed righthand (irh=false) -> to F (irh=false)
            Pressed F (irh=false) -> to D (irh=false)
            Pressed D (irh=false) -> to S (irh=false)
            Pressed S (irh=false) -> to A (irh=false)
            Pressed A (irh=false) -> to J (irh=True)
            '''
            if keylist[-1] in righthand: # First Factor
                isrighthand=True
                keylist.append('F')
            elif keylist[-1]=='F': # Second Factor
                keylist.append('D')
            elif keylist[-1]=='D': # Third Factor
                keylist.append('S')
            elif keylist[-1]=='S': # Fourth Factor
                keylist.append('A')
            elif keylist[-1]=='A': # Fifth Factor
                keylist.append('J')
                isrighthand=False
            else:
                print('error in l8K'+f' {keylist[-1]} {len(keylist)}')
