from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
from django.db import connection
# Create your views here.

def fun(request):
    
    return render(request, 'index.html')

def display(request,data,size):
   

        Test.objects.all().delete()
        ans=data.split(",")
        ss=size.split("=")
        length=int(ss[1])

        for x in range(0,len(ans),length):
        
            if length==1:
               obj=Test(c10=ans[x])
               obj.save()
        
            elif length==2:
                obj=Test(c10=ans[x],c11=ans[x+1])
                obj.save()

            elif length==3:

                obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2])
                obj.save()

            elif length==4:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3])
                 obj.save()
        
            elif length==5:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4])
                 obj.save()

            elif length==6:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5])
                 obj.save()

            elif length==7:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6])
                 obj.save()
        
            elif length==8:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7])
                 obj.save()

            elif length==9:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8])
                 obj.save()
        
            elif length==10:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8],c20=ans[x+9])
                 obj.save()

            elif length==11:
                obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8],c20=ans[x+9],c21=ans[x+10])
                obj.save()

            elif length==12:
                obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8],c20=ans[x+9],c21=ans[x+10],c22=ans[x+11])
                obj.save()


            elif length==13:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8],c20=ans[x+9],c21=ans[x+10],c22=ans[x+11],c23=ans[x+12])
                 obj.save()

            elif length==14:
                 obj=Test(c10=ans[x],c11=ans[x+1],c12=ans[x+2],c13=ans[x+3],c14=ans[x+4],c15=ans[x+5],c17=ans[x+6],c18=ans[x+7],c19=ans[x+8],c20=ans[x+9],c21=ans[x+10],c22=ans[x+11],c23=ans[x+12],c24=ans[x+13])
                 obj.save()
        
            

    

        return render(request, 'disp.html',{'data':data,'length':length})
     
