"""
Definition of views.
"""
#from turtle import Screen
from .z_module1 import *

from ctypes.wintypes import FLOAT
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from datetime import date

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def WebPage01(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage01.html',
        {
            'title':'WebPage01',
            'message':'Your WebPage01 page.',
            'year':datetime.now().year,
        }
    )

def WebPage02(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage02.html',
        {
            'title':'WebPage01',
            'message':'Your WebPage02 page.',
            'year':datetime.now().year,
        }
    )

def WebPage03(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage03.html',
        {
            'title':'WebPage03',
            'message':'Your WebPage03 page.',
            'year':datetime.now().year,
        }
    )

def WebPage04(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage04.html',
        {
            'title':'WebPage04',
            'message':'Your WebPage04 page.',
            'year':datetime.now().year,
        }
    )

def WebPage05(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage05.html',
        {
            'title':'WebPage05',
            'message':'Your WebPage05 page.',
            'year':datetime.now().year,
        }
    )

def WebPage06(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage06.html',
        {
            'title':'WebPage06',
            'message':'Your WebPage06 page.',
            'year':datetime.now().year,
        }
    )

def WebPage07(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage07.html',
        {
            'title':'WebPage07',
            'message':'Your WebPage07 page.',
            'year':datetime.now().year,
        }
    )

def WebPage08(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage08.html',
        {
            'title':'WebPage08',
            'message':'Your WebPage08 page.',
            'year':datetime.now().year,
        }
    )

def WebPage09(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/WebPage09.html',
        {
            'title':'WebPage09',
            'message':'Your WebPage09 page.',
            'year':datetime.now().year,
        }
    )

def CostM(request):
    # GET THE VALUES FROM HTML
    val03 = float(request.GET["num03"])
    val04 = float(request.GET["num04"])
    val05 = float(request.GET["num05"])
    val06 = float(request.GET["num06"])
    val07 = float(request.GET["num07"])
    
    val11 = request.GET["num11"]
    val12 = request.GET["num12"]
    val13 = request.GET["num13"]
    val14 = request.GET["num14"]
    
    val21 = request.GET["num21"]
    val22 = request.GET["num22"]
    val23 = request.GET["num23"]
    val24 = request.GET["num24"]
    val25 = request.GET["num25"]
    val26 = request.GET["num26"]
    val27 = request.GET["num27"]
    val28 = request.GET["num28"]
    
    oDateToday = date.today()
    #######################################
    # CALL THE CLASS AND DOING CALCULATIONS
    ccScreen = cScreen()    
    ################################
    ccScreen.ScreenWidth        = float(request.GET["num01"])
    ccScreen.ChannelHeight      = float(request.GET["num02"])
    ccScreen.WaterLevel         = float(request.GET["num03"])
    ccScreen.BarSpacing         = float(request.GET["num04"])
    ccScreen.BarThickness       = float(request.GET["num05"])
    ccScreen.BarWidth           = float(request.GET["num06"])
    ccScreen.InclinationDegree  = float(request.GET["num07"])

    ccScreen.SprocketDiameter   = float(request.GET["num61"])    
    ccScreen.Velocity           = float(request.GET["num62"])
    ccScreen.FOS                = float(request.GET["num63"])
    ccScreen.LoadPerMeterSq     = 180
    ccScreen.Eff                = 0.7
    ################################
    ccScreen.MaterialCostLEKG   = float(request.GET["num31"])     
        
    ccScreen.GearMotor          = float(request.GET["num41"])     
    ccScreen.Bearing            = float(request.GET["num42"])     
    ccScreen.Chain              = float(request.GET["num43"])     
    ccScreen.DriveShaft         = float(request.GET["num44"])     
    ccScreen.Sprocket           = float(request.GET["num45"])     
    ccScreen.Rake               = float(request.GET["num46"])     
    ccScreen.Accessories        = float(request.GET["num47"])
    ccScreen.ControlPanel       = float(request.GET["num48"])
    ccScreen.DifferentialLevel  = float(request.GET["num49"])
        
    ccScreen.Supervision        = float(request.GET["num53"]) 
    ccScreen.Manufacturing      = float(request.GET["num54"])   
    ccScreen.Transportation     = float(request.GET["num55"]) 
    ccScreen.Consumables        = float(request.GET["num56"])    
    ccScreen.Packing            = float(request.GET["num57"])    

    ccScreen.MarginFactor       = float(request.GET["num71"])
    ccScreen.RiskFactor         = float(request.GET["num72"])


    ################################
    ################################

    ccScreen.mWeight_calculation()
    ccScreen.mPower_calculation()
    ccScreen.mSpeed_calculation()
    ccScreen.mCost()
    ccScreen.mDrawingCode()



    ooWeight        = ccScreen.weight_result
    ooPower         = ccScreen.power_result
    ooSpeed         = ccScreen.speed_result
    ooDrawingCode   = ccScreen.DrawingCode
    
    ################################
    ################################

    ooMaterialcost          = ccScreen.MaterialCost_result    
    ooStandardCost          = ccScreen.StandardCost_Total_Out
    ooManufacturingCost     = ccScreen.ManufacturingCost_Total_Out
    ooSumOfCost             = ccScreen.SumOfCost_Out
    ooPrice                 = ccScreen.Price
    ooTotalPrice            = ccScreen.TotalPrice

    # SEND VALUES TO NEXT HTML
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CostM.html',
        {
            'oooTEST':              ccScreen.oTest,
            'oooWeight':            ooWeight,
            'oooPower':             ooPower,
            'oooSpeed':             ooSpeed,
            'oooMaterialcost':      ooMaterialcost,
            'oooStandardCost':      ooStandardCost,
            'oooManufacturingCost': ooManufacturingCost,
            'oooSumOfCost':         ooSumOfCost,
            'oooPrice':             ooPrice,
            'oooTotalPrice':        ooTotalPrice,
            'oooDateToday':         oDateToday,
            'oooDrawingCode':       ooDrawingCode,

            'val01':float(request.GET["num01"]),
            'val02':float(request.GET["num02"]),
            'val03':val03,
            'val04':val04,
            'val05':val05,
            'val06':val06,
            'val07':val07,

            'val11':val11,
            'val12':val12,
            'val13':val13,
            'val14':val14,

            'val21':val21,
            'val22':val22,
            'val23':val23,
            'val24':val24,
            'val25':val25,
            'val26':val26,
            'val27':val27,
            'val28':val28,

            'val31':float(request.GET["num31"]),

            'val41':float(request.GET["num41"]),
            'val42':float(request.GET["num42"]),
            'val43':float(request.GET["num43"]),
            'val44':float(request.GET["num44"]),
            'val45':float(request.GET["num45"]),
            'val46':float(request.GET["num46"]),
            'val47':float(request.GET["num47"]),
            'val48':float(request.GET["num48"]),
            'val49':float(request.GET["num49"]),

            'val51':float(request.GET["num51"]),
            'val52':float(request.GET["num52"]),
            'val53':float(request.GET["num53"]),
            'val54':float(request.GET["num54"]),
            'val55':float(request.GET["num55"]),
            'val56':float(request.GET["num56"]),
            'val57':float(request.GET["num57"]),

            'val71':float(request.GET["num71"]),
            'val72':float(request.GET["num72"]),
        },
        {
            'title':'CostM',
            'message':'Your CostM page.',
            'year':datetime.now().year,
        }
    )

def DataSheetM(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/DataSheetM.html',
        {
            'title':'DataSheetM',
            'message':'Your DataSheetM page.',
            'year':datetime.now().year,
        }
    )

def form(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/form.html',
        {
            'title':'form',
            'message':'Your form page.',
            'year':datetime.now().year,
        }
    )

def result(request):
    
    res = 4

    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result.html',
        {'result':res},
        {
            'title':'result',
            'message':'Your result page.',
            'year':datetime.now().year,
        }
    )

