import pandas as pd

url = "https://www.hcpcsdata.com/Codes"    #url of website

df = pd.read_html(url)#Data Frame

df=df[0]   # indexing
df.rename(columns={"HCPCS Codes":"Group","Description":"Category"},inplace=True)

LongDescription=['Ambulance service, outside state per mile, transport (medicaid only)','Hemostatic agent, gastrointestinal, topical','Cellular therapy','Administration of influenza virus vaccine','Alcohol and/or drug assessment','Injection, tetracycline, up to 250 mg','	Standard wheelchair','Cervical, semi-rigid, adjustable (plastic collar)','Medical Services','Cellular therapy','Cephalin floculation, blood','Cardiokymography','Transportation of portable ekg to facility or location, per patient','Exemestane, 25 mg','Nursing assessment / evaluation','Cdc 2019 novel coronavirus (2019-ncov) real-time rt-pcr diagnostic panel',	'Frames, purchases']
df['Long Description']=LongDescription

ShortDescription=['Outdide state ambulance service','Enter feed supkit syr by day','Hemostatic agent, gi, topic','Cane adjust/fixed with tip','	Admin influenza virus vac','Alcohol and/or drug assess','Tetracyclin injection','Standard wheelchair','Cervical semi-rigid adjustab','Cellular therapy','Cephalin floculation test','Cardiokymography','Transport portable ekg','Exemestane, 25 mg','Nursing assessment/evaluatn','2019-ncov diagnostic p','Vision svcs frames purchases']
df['Short Description']=ShortDescription

print(df)
df.to_csv('data.csv',index=False)
