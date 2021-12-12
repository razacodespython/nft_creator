from thirdweb import ThirdwebSdk, SdkOptions, MintArg
from dotenv import load_dotenv
import os


#network = "https://polygon-rpc.com"
network = "https://rinkeby-light.eth.linkpool.io/"

sdk = ThirdwebSdk(SdkOptions(), network)

load_dotenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

sdk.set_private_key(PRIVATE_KEY)

nft_smart_contract_address = "0x9310918FD886C69B65Ad88BccdE31638b3A93cFD"
nft_module = sdk.get_nft_module(nft_smart_contract_address)