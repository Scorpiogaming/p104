from collections import Counter
import csv
def mean(tw,te):
    mean=tw/te
    print("mean is "+str(mean))
def median(te,sd):
    if te %2==0:
        median1=float(sd[te//2])
        median2=float(sd[te//2-1])
        median=(median1+median2)/2
    else:
         median=float(sd[te//2])
    print("median is "+str(median))
def mode(sd):
    data=Counter(sd)
    mode_data_for_range = {
                         "75-85": 0, 
                         "85-95": 0, 
                         "95-105": 0,
                         "105-115": 0 ,
                         "115-125": 0 ,
                         "125"-"135": 0 ,
                         "135-145": 0 ,
                         "145-155": 0 ,
                         "155-165": 0 ,
                         "165-175": 0 
                         }
for height,occurence in data.items():
    if 75<float(height)<80:
        mode_data_for_range["75-85"]+=occurence
    elif 85<float(height)<95:
        mode_data_for_range["85-95"]+=occurence
    elif 95<float(height)<105:
        mode_data_for_range["95-105"]+=occurence
    elif 105<float(height)<115:
        mode_data_for_range["105-115"]+=occurence
    elif 115<float(height)<125:
        mode_data_for_range["115-125"]+=occurence
    elif 125<float(height)<135:
        mode_data_for_range["125-135"]+=occurence
    elif 135<float(height)<145:
        mode_data_for_range["135-145"]+=occurence
    elif 145<float(height)<155:
        mode_data_for_range["145-155"]+=occurence
    elif 155<float(height)<165:
        mode_data_for_range["155-165"]+=occurence
    elif 165<float(height)<175:
        mode_data_for_range["165-175"]+=occurence
mode_range,mode_occurence=0,0
for range,occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode=float((mode_range[0]+mode_range[1])/2)
print("mode is "+str(mode))
with open ("hw.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]