from django.shortcuts import render
from joblib import load



heart_scaler, heart_model = load(filename="pickles/heart_model.pkl")
cerv_scaler, cerv_model = load(filename="pickles/cervical_canc_model.pkl")
kidney_data, kidney_scaler, kidney_model = load(filename="pickles/kidney_models.pkl")



# Create your views here.

def render_home(request):
    
    return render(request, "index.html")



def render_heart(request):
    
    print(request.method)
    
    if request.method == "POST":
        print(request.POST)
        age = int(request.POST.get("age"))
        sex = int(request.POST.get("sex"))
        cp = int(request.POST.get("cp"))
        trestbps = int(request.POST.get("trestbps"))
        chol = int(request.POST.get("chol"))
        fbs = int(request.POST.get("fbs"))
        restecg = int(request.POST.get("restecg"))
        thalach = int(request.POST.get("thalach"))
        exang = int(request.POST.get("exang"))
        oldpeak = int(request.POST.get("oldpeak"))
        slope = int(request.POST.get("slope"))
        ca = int(request.POST.get("ca"))
        thal = int(request.POST.get("thal"))
                
        data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        result = heart_model.predict(heart_scaler.transform([data]))
        print(result)
    
        return render(request, "heart/heartres.html", {'res': result})
    
    return render(request, 'heart/heart.html')



def render_kidney(request):
    
    print(request.method)
    
    if request.method == "POST":
        data = [
            int(request.POST.get('age')),
            int(request.POST.get('bp')),
            float(request.POST.get('sg')),  # Specific Gravity might have decimal values
            int(request.POST.get('al')),
            int(request.POST.get('su')),
            float(request.POST.get('rbc')),  # Red Blood Cells might have decimal values
            int(request.POST.get('pc')),
            int(request.POST.get('pcc')),
            int(request.POST.get('ba')),
            int(request.POST.get('bgr')),
            int(request.POST.get('bu')),
            float(request.POST.get('sc')),  # Serum Creatinine might have decimal values
            int(request.POST.get('sod')),
            float(request.POST.get('pot')),  # Potassium might have decimal values
            float(request.POST.get('hemo')),  # Hemoglobin might have decimal values
            int(request.POST.get('pcv')),
            int(request.POST.get('wc')),
            float(request.POST.get('rc')),  # Red Blood Cell Count might have decimal values
            int(request.POST.get('htn')),
            int(request.POST.get('dm')),
            int(request.POST.get('cad')),
            int(request.POST.get('appet')),
            int(request.POST.get('pe')),
            int(request.POST.get('ane'))
        ]
              
        result = kidney_model.predict(kidney_scaler.transform([data]))
        print(result)
        
        return render(request, "kidney/kidneyres.html", {"res": result})
    
    return render(request, "kidney/kidney.html")



def render_cervical(request):
    
    print(request.method)
    
    if request.method == 'POST':
        data = [
            int(request.POST.get("age")),
            int(request.POST.get("num_sex_partners")),
            int(request.POST.get("first_sex_intercourse")),
            int(request.POST.get("num_pregnancies")),
            int(request.POST.get("smokes")),
            int(request.POST.get("smokes_years")),
            int(request.POST.get("smokes_packs_per_year")),
            int(request.POST.get("hormonal_contraceptives")),
            int(request.POST.get("hormonal_contraceptives_years")),
            int(request.POST.get("iud")),
            int(request.POST.get("iud_years")),
            int(request.POST.get("stds")),
            int(request.POST.get("stds_number")),
            int(request.POST.get("stds_condylomatosis")),
            int(request.POST.get("stds_cervical_condylomatosis")),
            int(request.POST.get("stds_vaginal_condylomatosis")),
            int(request.POST.get("stds_vulvo_perineal_condylomatosis")),
            int(request.POST.get("stds_syphilis")),
            int(request.POST.get("stds_pelvic_inflammatory_disease")),
            int(request.POST.get("stds_genital_herpes")),
            int(request.POST.get("stds_molluscum_contagiosum")),
            int(request.POST.get("stds_aids")),
            int(request.POST.get("stds_hiv")),
            int(request.POST.get("stds_hepatitis_b")),
            int(request.POST.get("stds_hpv")),
            int(request.POST.get("stds_number_of_diagnosis")),
            int(request.POST.get("dx_cancer")),
            int(request.POST.get("dx_cin")),
            int(request.POST.get("dx_hpv")),
            int(request.POST.get("dx")),
            int(request.POST.get("hinselmann")),
            int(request.POST.get("schiller")),
            int(request.POST.get("citology")),
        ]
        
        result = cerv_model.predict(cerv_scaler.transform([data]))
        
        return render(request, "cervical/cervres.html", {"res": result})

    return render(request, "cervical/cerv.html")       