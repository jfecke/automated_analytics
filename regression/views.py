from django.shortcuts import render
import pandas as pd

df = None

def index(request):
    if "GET" == request.method:
        return render(request, 'regression/index.html', {})
    elif "POST == request.method":
        
        if len(request.FILES) != 0:

            excel_file = request.FILES["excel_file"]

            # you may put validations here to check extension or file size

            df = pd.read_excel(excel_file)

            df_dict = df.to_dict()

            return render(request, 'regression/index.html', {"excel_data":df_dict})

        else:

            return render(request, 'regression/index.html', {"test_case":request})