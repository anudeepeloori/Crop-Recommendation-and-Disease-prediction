from django.shortcuts import render
from django.http import HttpResponse
from osgeo import ogr, osr, gdal
import numpy as np
import rasterio
import imageio
from rasterio.warp import transform
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create your views here.

def startPage(request):
    return render(request,'startPage.html')


def home(request):
    return render(request,'home.html')

def cropPage(request):
    return render(request,'cropPage.html')

def sendDataForDiseasePred(request):

    temp=request.GET["Temperature"]
    Humidity=request.GET["Humidity"]
    cropType=request.GET["cropType"]

    print(cropType)

    res1=[]


    if cropType=="Paddy":
        filename = r'C:\Users\DELL\Downloads\AgroTHON\paddycropdisease_model.sav'
        loaded_model=pickle.load(open(filename, 'rb'))

        val1=[Humidity,temp]
        res1=loaded_model.predict([val1])

    if cropType=="Corn":
        filename = r'C:\Users\DELL\Downloads\AgroTHON\corncropdisease_model.sav'
        loaded_model=pickle.load(open(filename, 'rb'))

        val1=[Humidity,temp]
        res1=loaded_model.predict([val1])
        

    return render(request,'sendDataForDiseasePred.html',{'result':res1[0],'temp':temp,'hum':Humidity,'crop':cropType})


def sendData(request):
    x=request.GET["x_co"]
    y=request.GET["y_co"]

    # print(v1, v2)
    # return render(request,'data.html',{'x':v1,'y':v2})

# Load the GeoTIFF image
    ds = gdal.Open(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\final_sentinel_preprocessed_image.tif")  #sentinal-1

    col, row, band = ds.RasterXSize, ds.RasterYSize, ds.RasterCount
    print(col, row, band)

    xoff, a, b, yoff, d, e = ds.GetGeoTransform()
    print(xoff, a, b, yoff, d, e)

# details about the params: GDAL affine transform parameters
# xoff,yoff = left corner 
# a,e = weight,height of pixels
# b,d = rotation of the image (zero if image is north up)



    def pixel2coord(x, y):
        xp = a * float(x) + b * float(y) + xoff
        yp = d * float(x) + e * float(y) + yoff
        return(xp, yp)

    result = pixel2coord(x,y)
    return render(request,'data.html',{'long':round(result[0],4),'lat':round(result[1],4)})
    
    
def sendLongLat(request):
    v1=request.GET["long"]
    v2=request.GET["lat"]
    B1 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B1_subset_5_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B2 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B2_subset_6_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B3 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B3_subset_8_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B4 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B4_subset_9_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B5 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B5_subset_10_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B6 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B6_subset_11_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B7 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B7_subset_12_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B8 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B8_subset_13_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B8A = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B8A_subset_14_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B9 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B9_subset_15_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B11 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B11_subset_16_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    B12 = imageio.imread(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B12_subset_17_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    
    src=rasterio.open(r"C:\Users\DELL\Downloads\MAJOR_PROJECT\project\Fused_outputs\ultra final\sentinel-2\B1_subset_5_of_S2A_MSIL2A_20220925T050701_N0400_R019_T44QKE_20220925T100854_resampled.tif")
    # test=imageio.imread(r"D:\Downloads\dwt_fused3.jpg")

    # print('shapeee',test.shape)
# Convert the latitude/longitude values to the CRS of the TIFF file
    lon, lat = float(v1), float(v2)
    x, y = transform('EPSG:4326', src.crs, [lon], [lat])    
# Convert the CRS coordinates to pixel coordinates
    row, col = src.index(x, y)
# Print the pixel coordinates
    print('shape',B1.shape)
    print('row',row)
    print('col',col)

    val1=[B1[row[0]][col[0]],B2[row[0]][col[0]],B3[row[0]][col[0]],B4[row[0]][col[0]],B5[row[0]][col[0]],B6[row[0]][col[0]],B7[row[0]][col[0]],B8[row[0]][col[0]],B8A[row[0]][col[0]],B9[row[0]][col[0]],B11[row[0]][col[0]],B12[row[0]][col[0]]]
    filename = r"C:\Users\DELL\Downloads\AgroTHON\\agrothon_model.sav"
    filename_n=r"C:\Users\DELL\Downloads\\AgroTHON\\n_agrothon_model.sav"
    filename_k=r"C:\Users\DELL\Downloads\\AgroTHON\\k_agrothon_model.sav"
    loaded_model_n=pickle.load(open(filename_n, 'rb'))
    loaded_model = pickle.load(open(filename, 'rb'))
    loaded_model_k=pickle.load(open(filename_k, 'rb'))
    
    res_p=loaded_model.predict([val1])
    res_n=loaded_model_n.predict([val1])
    res_k=loaded_model_k.predict([val1])


    return render(request,'result.html',{'predicted_Phosphorous_value':round(res_p[0],3),'predicted_Nitrogen_value':round(res_n[0],3),'predicted_Potassium_value':round(res_k[0],3),'long_value':lon,'lat_value':lat})


def sendNPKData(request):
    n=request.GET["Nitrogen"]
    k=request.GET["Potassium"]
    p=request.GET["Phosphorous"]
    temp=request.GET["Temperature"]
    humid=request.GET["Humidity"]
    ph=request.GET["PH"]

    filename = r"C:\Users\DELL\Downloads\AgroTHON\cropRecommendation_model.sav"
    loaded_model=pickle.load(open(filename, 'rb'))

    val1=[n,p,k,humid,temp,ph]
    
    res1=loaded_model.predict([val1])
    # loaded_model.probability=True
    res=loaded_model.predict_proba([val1])
    print(res1)
    print(res)
    for i in range(0,len(res[0])):
        res[0][i]=round(res[0][i],2)*100


    
    return render(request,'base.html',{'crop':res1[0], 'GroundNut':res[0][0],'Cotton':res[0][1],'Jowar':res[0][2],'Maize':res[0][3],'Paddy':res[0][4]} )