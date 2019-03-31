# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
from time import time
import datetime
from statistics import mean
import numpy as np

def get_data(cap, op, opWrapper):
    ret, frame = cap.read()
    # Process Image
    datum = op.Datum()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop([datum])

    cv2.imshow('frame', datum.cvOutputData)

    body_points=datum.poseKeypoints

    return body_points

def collect_data(cap, op, opWrapper, file):
    f = open(file, "a+")
    start = time()
    while time() - start < 10:
        try:
            body_points = get_data(cap, op, opWrapper)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            neck=body_points[0][1]
            hip=body_points[0][8]
            print("neck keypoint: \n" + str(neck[0]) + '\t' + str(neck[1]) + '\t' + str(neck[2]))
            print("hip keypoint: \n" + str(hip[0]) + '\t' + str(hip[1]) + '\t' + str(hip[2]))
            data = str(neck[0]) + ',' + str(neck[1]) + ',' + str(neck[2]) + ','
            data = data + str(hip[0]) + ',' + str(hip[1]) + ',' + str(hip[2]) + '\n'
            f.write(data)
        except Exception as e:
            print("Error found, passing: " + str(e))
            pass
    f.close()


def collect_neck_and_hip(cap, op, params):
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    #get current date and times
    date_min=str(datetime.datetime.now())[0:16]
    print("date time is:"+date_min)
    print("***SIT STRAIGHT***")
    collect_data(cap, op, opWrapper, "../../RU_Slouching/data/data_preSlouch"+date_min+".txt")
    print("***SLOUCH NOW, MY PEASANT***")
    break_start = time()
    while time() - break_start < 5:
        ret, frame = cap.read()
        # Process Image
        datum = op.Datum()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])
        cv2.imshow('frame', datum.cvOutputData)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    collect_data(cap, op, opWrapper, "../../RU_Slouching/data/data_slouching"+date_min+".txt")
    print("***DATA COLLECTED***")
    print("***RESUMING KILLING ALL HUMANS***")

def getAnglefromFile(preslouch_file, slouch_file):
    file = open(preslouch_file, "r")
    neckData=[]
    hipData=[]
    lineNum=0
    for line in file:
        lineData=line.split(',')
        neck=lineData[0:3]
        hip=lineData[3:6]
        neckData.append(neck)
        hipData.append(hip)
    neckData=np.array(neckData).astype(np.float)
    hipData=np.array(hipData).astype(np.float)
    #neckData=np.reshape(neckData, (np.shape(neckData)[1],np.shape(neckData)[0]))
    #print(neckData)
    neckMean=np.mean(neckData,axis=0)
    hipMean=np.mean(hipData,axis=0)
    #print("mean : ",neckMean,"\n",hipMean)
    u=neckMean-hipMean

    fileS = open(slouch_file, "r")
    neckDataS=[]
    hipDataS=[]
    lineNumS=0
    for line in fileS:
        lineData=line.split(',')
        neckS=lineData[0:3]
        hipS=lineData[3:6]
        neckDataS.append(neckS)
        hipDataS.append(hipS)
    neckDataS=np.array(neckDataS).astype(np.float)
    hipDataS=np.array(hipDataS).astype(np.float)
    #neckData=np.reshape(neckData, (np.shape(neckData)[1],np.shape(neckData)[0]))
    #print(neckData)
    neckMeanS=np.mean(neckDataS,axis=0)
    hipMeanS=np.mean(hipDataS,axis=0)
    #print("mean : ",neckMeanS,"\n",hipMeanS)
    k=neckMeanS-hipMeanS
    print("u is: ",u)
    print("k is: ",k)
    dot_product=np.dot(u,k)
    print("dot product: ",dot_product)
    norms=(np.linalg.norm(u)*np.linalg.norm(k))
    print("norms: ",norms)
    theta=np.arccos(dot_product/norms)
    print("theta: ",theta*180/np.pi)
    return theta





def main():

    # Import Openpose (Windows/Ubuntu/OSX)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:

        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append('../python');
        # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
        # sys.path.append('/usr/local/python')
        from openpose import pyopenpose as op
    except ImportError as e:
        print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e

    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = "../../models/"
    params["number_people_max"] = 1



    #get video
    cap = cv2.VideoCapture(1)
    collect_neck_and_hip(cap, op, params)

    '''
    while True:
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Process Image
        datum = op.Datum()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])

        cv2.imshow('frame', datum.cvOutputData)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Display Image
        body_points=datum.poseKeypoints
        neck=body_points[0][1]
        hip=body_points[0][8]
        print("neck keypoint: \n" + str(neck[0]) + '\t' + str(neck[1]) + '\t' + str(neck[2]))
        print("hip keypoint: \n" + str(hip[0]) + '\t' + str(hip[1]) + '\t' + str(hip[2]))

        preSlouch.write(str(neck[0]) + '\t' + str(neck[1]) + '\t' + str(neck[2]) + '\n')
        #slouch.write(str(hip[0]) + '\t' + str(hip[1]) + '\t' + str(hip[2]) + '\n')
    '''

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    getAnglefromFile('/home/milkkarten/Open_Pose/RU_Slouching/data/data_preSlouch2019-03-31 18:19.txt','/home/milkkarten/Open_Pose/RU_Slouching/data/data_slouching2019-03-31 18:19.txt' )
