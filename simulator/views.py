from django.shortcuts import render, HttpResponse


# Create your views here.

def handle_simulator(request):
    return render(request, 'simulator/simulator.html', {})


def handle_output(request):
    currancy_type = request.POST.get('cType', 'LTC')
    invest_year = request.POST.get('investYear', '2014')
    invest_ammount = int(request.POST.get('investAmmount', '1'))

    if currancy_type == "BTC":
        if invest_year == "2014":
            ans = invest_ammount + invest_ammount * 57
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 5700})

        if invest_year == "2019":
            ans = invest_ammount + invest_ammount * 10.84
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 1084})

    if currancy_type == "LTC":
        if invest_year == "2014":
            ans = invest_ammount + invest_ammount * 155.5
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 15550})

        if invest_year == "2019":
            ans = invest_ammount + invest_ammount * 9.5
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 950})

    if currancy_type == "NMC":
        if invest_year == "2014":
            ans = invest_ammount + invest_ammount * 9.43
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 943})

        if invest_year == "2019":
            ans = invest_ammount + invest_ammount * 0.9
            return render(request, 'simulator/output.html', {'answer': ans, 'return': 90})

    return HttpResponse("Some Unexpected Input")
