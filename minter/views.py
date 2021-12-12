from django.shortcuts import redirect, render, HttpResponse
from . import nft_network
from thirdweb import ThirdwebSdk, SdkOptions, MintArg


def home(request):
    
    file_url = nft_network.nft_module.balance()
    
    if request.method == 'POST' and request.FILES['home']:
        upload = request.FILES['home']
        
        name_nft = "Wing_02"
        description_nft = "My-Wing"
        image_nft = upload.read()
        prop = {}

        nft_network.nft_module.mint(MintArg(name=name_nft,description=description_nft,image_uri=image_nft, properties=prop))
        
        return redirect("success")
     
    return render(request, "index.html", {'file_url': file_url})


def success(request):
    return HttpResponse("successfully uploaded")
