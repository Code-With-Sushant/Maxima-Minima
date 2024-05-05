eqco=input ("Enter the coefficients of quadratic equation: ")
coef=list (map (float,eqco.split()))
defe = []
for k in range(0,len(coef)):
    if (len(coef)-k-1!=0):
        defe.append((len(coef)-k-1)*coef[k])

print('After differentiation the equation: '+str(defe [0])+'x%+f'%(defe [1]))

mai= float (-1*defe[1])/defe[0]

if (coef[0]>=0):
    print('the minima of given equation is at x=%f'%mai)
else:
    print('the maxima of given equation is at x=%f'%mai)