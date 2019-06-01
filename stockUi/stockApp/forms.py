from django import forms

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    s=forms.TextInput()

class stkName(forms.Form):
    CHOICES = (('AXISBANK','Axis Bank Ltd'),('BAJAJ-AUTO','Bajaj Auto Ltd'),('HDFCBANK','HDFC Bank Ltd'),('TCS', 'TCS'),('WIPRO', 'WIPRO'),('TECHM','Tech Mahindra Ltd'),)
    Select = forms.ChoiceField(choices=CHOICES)

'''
Adani Ports and Special Economic Zone Ltd.	ADANIPORTS
Asian Paints Ltd.	ASIANPAINT
Axis Bank Ltd.	AXISBANK
Bajaj Auto Ltd.	BAJAJ-AUTO
Bajaj Finance Ltd.	BAJFINANCE
Bajaj Finserv Ltd.	BAJAJFINSV
Bharat Petroleum Corporation Ltd.	BPCL
Bharti Airtel Ltd.	BHARTIARTL
Bharti Infratel Ltd.	INFRATEL
Britannia Industries Ltd.	BRITANNIA
Cipla Ltd.	CIPLA
Coal India Ltd.	COALINDIA
Dr. Reddy's Laboratories Ltd.	DRREDDY
Eicher Motors Ltd.	EICHERMOT
GAIL (India) Ltd.	GAIL
Grasim Industries Ltd.	GRASIM
HCL Technologies Ltd.	HCLTECH
HDFC Bank Ltd.	HDFCBANK
Hero MotoCorp Ltd.	HEROMOTOCO
Hindalco Industries Ltd.	HINDALCO
Hindustan Unilever Ltd.	HINDUNILVR
Housing Development Finance Corporation Ltd.	HDFC
ICICI Bank Ltd.	ICICIBANK
ITC Ltd.	ITC
Indiabulls Housing Finance Ltd.	IBULHSGFIN
Indian Oil Corporation Ltd.	IOC
IndusInd Bank Ltd.	INDUSINDBK
Infosys Ltd.	INFY
JSW Steel Ltd.	JSWSTEEL
Kotak Mahindra Bank Ltd.	KOTAKBANK
Larsen & Toubro Ltd.	LT
Mahindra & Mahindra Ltd.	M&M
Maruti Suzuki India Ltd.	MARUTI
NTPC Ltd.	NTPC
Oil & Natural Gas Corporation Ltd.	ONGC
Power Grid Corporation of India Ltd.	POWERGRID
Reliance Industries Ltd.	RELIANCE
State Bank of India	SBIN
Sun Pharmaceutical Industries Ltd.	SUNPHARMA
Tata Consultancy Services Ltd.	TCS
Tata Motors Ltd.	TATAMOTORS
Tata Steel Ltd.	TATASTEEL
Tech Mahindra Ltd.	TECHM
Titan Company Ltd.	TITAN
UPL Ltd.	UPL
UltraTech Cement Ltd.	ULTRACEMCO
Vedanta Ltd.	VEDL
Wipro Ltd.	WIPRO
Yes Bank Ltd.	YESBANK
Zee Entertainment Enterprises Ltd.	ZEEL
'''
