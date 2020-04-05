#nokte : dar in ravesh halgheye while namikhahad az 1 ta n bar becharkhad be tedade bozorg tarin adade donbaleye fibonacci kochiktar mosavie n micharkhad
#masalan agar n 20 vared shavad tanha be tedade (1,2,3,5,8,13) yani 6 bar micharkhad 
#menha ha ra dar har dor haleghe be tedade faseleye do adade fibonacci chap karde va jaye khode adade fibonacci mosabt gozashte
#dar inn ravesh az hadeaghal dor haleghe estefade shod
#ba in raveshe code nevisi memory kamtari estefade mishavad va sorat bala tar miravad
#mohem hala felan in baraye shoma nist vali goftm ke bedanid
n=int(input())
output='+'
a=1
b=1
while a+b<=n:
    tmp=b
    b+=a
    a=tmp
    output+='-'*(b-a-1) 
    output+='+'
output+='-'*(n-b)
print (output)
