from django.shortcuts import render
from . import forms
from django.http import HttpResponse
import urllib.request
import pandas as pd
import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as plt1
from sklearn.linear_model import LinearRegression
# Create your views here.

def index(request):
    #my_dict = {'insert_me':"Hello i am from views.py"}
    Date=None
    Open=None
    High=None
    Low=None
    Close=None

    arr=None
    arr2=None
    pred=None
    mpred=None
    xlast=None

    p_arr=None
    q_arr2=None
    plast=None
    p_pred=None
    stkP=forms.stkName()

    if request.method=='POST':
        stkP=forms.stkName(request.POST)

    if stkP.is_valid():
        ticker=stkP.cleaned_data['Select']

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:' + ticker + '&apikey=S5R8PAYIH8YYCJAU&datatype=csv'

        def download_stock_data(csv_url):
            response = urllib.request.urlopen(csv_url)
            csv=response.read()
            csv_str=str(csv,'UTF-8')

            lines = csv_str.split("\\n")
            dest_url='templates/dataset.csv'
            fx=open(dest_url,"w")
            for line in lines:
                fx.write(line + "\n")
            fx.close()
        download_stock_data(url)

        dataset=pd.read_csv('templates/dataset.csv')
        xlast=dataset.iloc[:1,4].values
        X = dataset.iloc[1 : ,4  ].values   # /open
        Y = dataset.iloc[0: dataset.shape[0]-1 ,1].values


        # Date=dataset.iloc[:1,0].values
        Date=np.array(dataset.iloc[:1,0].values).tolist()
        Open=np.array(dataset.iloc[:1,1].values).tolist()
        High=np.array(dataset.iloc[:1,2].values).tolist()
        Low=np.array(dataset.iloc[:1,3].values).tolist()
        Close=np.array(dataset.iloc[:1,4].values).tolist()
        Date=Date[0]
        Open=Open[0]
        High=High[0]
        Low=Low[0]
        Close=Close[0]

        print(type(Date[0]))
        print(Date[0])

        X=X.reshape(-1,1)
        Y=Y.reshape(-1,1)

        regressor=LinearRegression()
        regressor.fit(X,Y)

        y_pred = regressor.predict(X[:1,])

        # X=X.ravel();
        # Y=Y.ravel();
        # print(y_pred.ravel())

        # plt.scatter(X.ravel(), Y.ravel(), color='red')
        # plt.plot(X.ravel(), regressor.predict(X).ravel(), color = 'blue')
        # # plt.scatter(y_pred.ravel(),color='green')
        # plt.title('Open vs Close price (Training set)')
        # plt.xlabel('Close price')
        # plt.ylabel('Open')

        # print(type(X.ravel()))




        # plt.savefig('stockApp/static/mysite/images/new_plot.png')

        arr=np.array(X.ravel()).tolist()
        print(type(pred))
        arr2=np.array(Y.ravel()).tolist()
        pred=np.array(y_pred[0].ravel().astype(int).tolist())
        xlast=np.array(X[0].ravel().astype(int).tolist())
        mpred=pred[0]
        # Date=np.array(Date.astype(int))

        # pred=2500
        # xlast=2700
        # print(type(Date.tostring()))

        ###################################     SVR     #########################################################33
        p=dataset.iloc[:-1,1].values
        p=p.reshape(-1,1)
        q=dataset.iloc[:-1,4].values
        q=q.reshape(-1,1)

        print(p[0])


        #data spliting
        '''from sklearn.model_selection import train_test_split
        p_train,p_test,q_train,q_test=train_test_split(p,q,test_size=0.2,random_state=0)
        '''

        from sklearn.preprocessing import StandardScaler
        sc_p = StandardScaler()
        p_train = sc_p.fit_transform(p)
        #p_test = sc_p.transform(p_test)
        sc_q = StandardScaler()
        q_train = sc_q.fit_transform(q)

        # Fitting SVR to the dataset
        from sklearn.svm import SVR
        regressor = SVR(kernel = 'rbf')
        regressor.fit(p_train, q_train)


        # Predicting a new result
        q_pred = regressor.predict(p_train)
        q_pred = sc_q.inverse_transform(q_pred)
        q_pred=q_pred[0]     #closing price of todaq from yesterdays's closing price

        p_arr=np.array(p.ravel()).tolist()
        q_arr2=np.array(q.ravel()).tolist()
        p_pred=q_pred.astype(np.int64)
        # p_pred=np.array(q_pred[0].astype(int).tolist())
        plast=np.array(p[0].ravel().astype(int).tolist())
        print(type(p_pred))

    return render(request,'index.html',{'stkP':stkP,'xx':arr,'yy':arr2,'pred':pred,'mpred':mpred,'xlast':xlast,'Date':Date,'Open':Open,'High':High,'Low':Low,'Close':Close,
                                        'p_arr':p_arr, 'q_arr2':q_arr2, 'p_pred':p_pred,'plast':plast   })



def form_name_view(request):
    form=forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print("VALID")
        print("NAME:" +form.cleaned_data['name'])

    return render(request,'form_page.html',{'form':form})
