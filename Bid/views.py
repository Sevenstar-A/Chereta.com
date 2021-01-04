from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, Bid, Auction 
from geopy.geocoders import Nominatim
import json
import urllib #for redirecting urls with context data


def index(request):
    return render(request, 'Bid/index.html',{})

def home_page(request):


    all_bids = Bid.objects.all()
    context = {'all_bids':all_bids}
    return render(request,'Bid/user_home_page.html', context)

def user_home_page(request, id):
                    all_bids = Bid.objects.all() #all bids
                    user= Client.objects.filter(id = id)
                    context = {'all_bids':all_bids, 'user':user[0]}
                                    
                    posted_bids = Bid.objects.filter(Uploader= user[0].id)
                                    
                    if posted_bids:
                        posted_bids_detail_list = []

                        for bid in posted_bids:
                            posted_bids_detail_list.append(bid)

                        context['Posted_bids'] = posted_bids_detail_list

                    
                    
                    engaged_auctions = Auction.objects.filter(Client_id = user[0].id) #check if the user has an auction
                    
                    if engaged_auctions:
                        engaged_auctions_detail_list = []

                        for auction in engaged_auctions:
                            bid = Bid.objects.get(id = auction.Bid_id.id)
                            offered_price = auction.Offered_price

                            engaged_auctions_detail_list.append( {'Bid_id': bid.id, 'Title':bid.Title, 'Offered_price':offered_price } )

                        context [ "engaged_auctions"] = engaged_auctions_detail_list
                        
                        
                    return render(request,'Bid/user_home_page.html', context)

            


def new_post(request, id):
    return render(request, 'Bid/new_auction_post_form.html',{'user_id':id})

def new_post_validator(request, id):
    bid = Bid(Title = request.POST['Title'], Description=request.POST['Description'], Catagory= request.POST['Catagory']
    , Base_cost=request.POST['Base_cost'], Date_created = request.POST['Date_created'], Date_closing=request.POST['Date_closing'],
    Total_number_of_biders=0, Uploader=Client.objects.get(id =id)   
    )
    bid.save()

    

    return redirect( "/%s/user_home_page/"%id  )

def bid_detail(request, user_id, bid_id):
    bid = Bid.objects.get(id = bid_id)
    if bid:
        return render(request,'Bid/bid_detail.html', {'bid':bid, 'user_id':user_id})

def bid(request, user_id, bid_id):
    if request.method == 'POST':
        # name=request.POST['name_area']
        # password= request.POST['password_area']

        client = Client.objects.filter(id = user_id)
       
        if (client):
                    user = client[0]              
                    bid = Bid.objects.get(id=bid_id)

                    bid.Total_number_of_biders+=1
                    bid.save()
                
                    auction=Auction(Bid_id=bid, Client_id= Client.objects.get(id = user_id), Offered_price = request.POST['price_area'],Notes=' ')
                    auction.save()
        
    return redirect( "/%s/user_home_page/"%user_id  )

    

def to_login_form(request):
   context =  {'error':"false"}
   return render(request, 'Bid/login_form.html',context)

def login_validator(request):
    if request.method == 'POST':
        name=request.POST['name_area']
        password= request.POST['password_area']

        client = Client.objects.filter(User_name = name)
       
        if (client):
                user = client[0] 
                if user.Password ==  password:
                     return redirect( "/%s/user_home_page/" %user.id  )
                
                else:
                     context ={'error':"True"}
                     return render(request, "Bid/login_form.html", context)


        else:
            context = {'error':"True"}
            return render(request, "Bid/login_form.html", context)

    else:
        name=request.GET['name_area']
        password= request.GET['password_area']

        client = Client.objects.filter(User_name = name)
       
        if (client):
           
            
                user = client[0] 
                if user.Password ==  password:
                    return redirect( "/%s/user_home_page/" %user.id  )
                
                else:
                     context ={'error':"True"}
                     return render(request, "Bid/login_form.html", context)


        else:
            context = {'error':"True"}
            return render(request, "Bid/login_form.html", context)

def to_sing_in_form(request):
    return render(request, 'Bid/sign_in_form.html',{})

def sign_in_validator(request):
       
        client = Client.objects.filter(User_name = request.POST['name_area'])
       
        if (client):
            return render(request,"Bid/sign_in_form.html",{'error':'True'})
        
        firstname_area = request.POST['firstname_area']
        lastname_area = request.POST['lastname_area']
        name_area = request.POST['name_area']
        password_area = request.POST['password_area']

        email = request.POST['email']

        city = request.POST['city']

        phone = request.POST['phone']
        # credit = request.POST['credit_card']

        client = Client(
            First_name= firstname_area, Last_name = lastname_area,User_name = name_area, Password= password_area, Emial=email,
            Phone= phone, City=city, Longitude=89.0, Latitude=90.0, Credit_card= '1000123455')
        
        client.save()


        return redirect( "/%s/user_home_page/" %client.id  )