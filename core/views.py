from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Element, CriticalConstantsAndAFIOC, DensityOfIOL, EnthalpyandGibbs, HeatCapacityAtConstantPOIOLhyperbolic, HeatCapacityAtConstantPOIOLpolynomial, HeatCapacityOIOL, HeatofVaporizationOIOL, ThermalConductivityofIOL, Vapor_Pressure_Of_IOL, VaporThermalofIOS, VaporViscosityIOS, ViscosityofIOL
from django.db.models import Q
from .forms import ElementSearchForm
import datetime
from datetime import datetime


def home(request):
    return render (request, 'index.html')


def pro_home(request):
    queryset = Element.objects.all().order_by('id')
    now = datetime.date(datetime.now())
    
    paginator = Paginator(queryset, 100)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    form = ElementSearchForm(request.POST or None)
    if request.method == 'POST':
        queryset = Element.objects.filter(
									name__icontains=form['name'].value(),
									)
    context = {
        "queryset": queryset,
        'form': form,
        'now': now,
        
    }
    return render (request, 'pro.html', context)

def element_detail(request, id):
    ele = get_object_or_404(Element, id = id)
    vpiol = Vapor_Pressure_Of_IOL.objects.filter(el = ele).first()
    diol = DensityOfIOL.objects.filter(el = ele).first()
    ccioc = CriticalConstantsAndAFIOC.objects.filter(el = ele).first()
    hviol = HeatofVaporizationOIOL.objects.filter(el = ele).first()
    hciol = HeatCapacityOIOL.objects.filter(el = ele).first()
    hccpiolp = HeatCapacityAtConstantPOIOLpolynomial.objects.filter(el = ele).first()
    hccpiolh = HeatCapacityAtConstantPOIOLhyperbolic.objects.filter(el = ele).first()
    eandg = EnthalpyandGibbs.objects.filter(el = ele).first()
    vvios = VaporViscosityIOS.objects.filter(el = ele).first()
    viol = ViscosityofIOL.objects.filter(el = ele).first()
    vtios = VaporThermalofIOS.objects.filter(el = ele).first()
    tciol = ThermalConductivityofIOL.objects.filter(el = ele).first()
    now = datetime.date(datetime.now())
    context = {
        'ele': ele,
        'vpiol': vpiol,
        'diol': diol,
        'ccioc': ccioc,
        'hviol': hviol,
        'hciol': hciol,
        'hccpiolp': hccpiolp,
        'hccpiolh': hccpiolh,
        'eandg': eandg,
        'vvios': vvios,
        'viol': viol,
        'vtios': vtios,
        'tciol': tciol,
        'now': now,
    }
    return render (request, 'pro_detail.html', context)
