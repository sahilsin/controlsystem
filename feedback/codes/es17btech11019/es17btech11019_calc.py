#part (a)
Vt=25
Ie=2

re = Vt/Ie
print("re=",re)

beta=100
Ic=(beta/beta+1)*(Ie/Vt)
gm= Ic*Vt

print("gm=",gm)

rpie=beta/gm

print("rpie=",rpie)

ft=500*(10^6)
fbeta = ft/beta
print("fbeta=",fbeta)


Cmu= 2*(10^(-12))
Cpie=(gm/(2*3.14*ft))-Cmu
print("Cpie=",Cpie)




#Part (b)
Vtb=25
reb=25
Ieb=Vtb/reb
print("Ie=",Ieb)

gmb=Ieb/Vtb
print("gm=",gmb)


Cmub=2 * (10^(-12))
Cpieb=10.7*(10^(-12))
fbetab=4*(10^6)
rpieb=1/(2*3.14*(Cmub+Cpieb)*fbetab)
print("rpie=",rpieb)


betab=gmb*rpieb
print("beta=",betab)


ftb=betab*fbetab
print("ft=",ftb)

#Part (c)
ftC=500*(10^6)
betaC=100
fbetaC=ftC/betaC
print("fbeta=",fbetaC)

rpieC=2500
gmC=betaC/rpieC
print("gm=",gmC)

VtC=25
IeC=gmC*VtC
print("Ie=",IeC)


reC=VtC/IeC
print("re=",reC)

CpieC=10.7*(10^(-12))
ftC=500*(10^8)
CmuC=(gmC/2*3.14*ftC)-CpieC
print("Cmu=",CmuC)


#Part(d)
VtD=25
IeD=10
reD=VtD/IeD
print("re=",reD)

gmD=IeD/VtD
print("gm=",gmD)

betaD=100
rpieD=betaD/gmD
print("rpie=",rpieD)

ftD=500*(10^6)
fbetaD=ftD/betaD
print("fbeta=",fbetaD)


CmuD=2*(10^(-12))

CpieD=(gmD/2*3.14*ftD)-CmuD
print("Cmu=",CmuD)

#Part(e)

VtE=25
IeE=0.1
reE=VtE/IeE
print("re=",reE)

gmE=IeE/VtE
print("gm=",gmE)

betaE=100
rpieE=betaE/gmE
print("rpie=",rpieE)

ftE=150*(10^6)
fbetaE=ftE/betaE
print("fbeta=",fbetaE)


CmuE=2*(10^(-12))

CpieE=(gmE/2*3.14*ftE)-CmuE
print("Cpie=",CpieE)

#Part(f)

VtF=25
IeF=1
reF=VtF/IeF
print("re=",reE)

gmF=IeF/VtF
print("gm=",gmF)

betaF=10
rpieF=betaF/gmF
print("rpie=",rpieF)

ftF=500*(10^6)
fbetaF=ftF/betaF
print("fbeta=",fbetaF)

CmuF=2*(10^(-12))

CpieF=(gmF/2*3.14*ftF)-CmuF
print("Cpie=",CpieF)

#Part(g)

ftG=800*(10^6)
fbetaG=80*(10^6)
betaG = ftG/fbetaG
print("beta=",betaG)

CmuG=1 * (10^(-12))
CpieG=9*(10^(-12))
rpieG=1/(2*3.14*(CmuG+CpieG)*fbetaG)
print("rpie=",rpieG)

gmG=betaG/rpieG
print("gm=",gmG)

VtG=0.025
IeG=gmG*VtG

reG=VtG/IeG
print("re=",reG)
