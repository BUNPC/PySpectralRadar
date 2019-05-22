# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:18:32 2019

Python wrapper for Thorlabs SpectralRadar SDK

@author: sstucker

"""

import ctypes as C
from enum import IntEnum

#Imports SpectralRadar libraries. Thorlabs software must be installed on machine
SpectralRadar = C.CDLL('SpectralRadar')


#Wrapper typedefs --------------------------------------------------------------

class BOOL(C.c_int):
    pass

class ComplexFloat(C.Structure):
    _fields_=[("data",C.c_float*2)]

#Pointer typedefs --------------------------------------------------------------

class RawDataStruct(C.Structure):
    pass

RawDataHandle = C.POINTER(RawDataStruct)

class DataStruct(C.Structure):
    pass

DataHandle = C.POINTER(DataStruct)

class ComplexDataStruct(C.Structure):
    pass

ComplexDataHandle = C.POINTER(ComplexDataStruct)

class OCTFileStruct(C.Structure):
    pass

OCTFileHandle = C.POINTER(OCTFileStruct)

class BufferStruct(C.Structure):
    pass

BufferHandle = C.POINTER(BufferStruct)

class ImageFieldStruct(C.Structure):
    pass

ImageFieldHandle = C.POINTER(ImageFieldStruct)

class DeviceStruct(C.Structure):
    pass

DeviceHandle = C.POINTER(DeviceStruct)

class ScanPatternStruct(C.Structure):
    pass

ScanPatternHandle = C.POINTER(ScanPatternStruct)

class ProcessingStruct(C.Structure):
    pass

ProcessingHandle = C.POINTER(ProcessingStruct)

class ProbeStruct(C.Structure):
    pass

ProbeHandle = C.POINTER(ProbeStruct)


# Enum typedefs ----------------------------------------------------------------

class AcquisitionType(IntEnum):

    Acquisition_AsyncContinuous = 0
    Acquisition_AsyncFinite = 1
    Acquisition_Sync = 2

    def __init__(self,value):
        self._as_parameter = int(value)


#Wrapper functions ------------------------------------------------------------

'''
These are of the following format:

    def sameFunctionNameAsInAPI(~Same argument names as API~):
        SpectralRadar.sameFunctionNameAsInAPI.argtypes = [~argument type(s) if applicable~]
        SpectralRadar.sameFunctionNameAsInAPI.restypes = [~return type if applicable~]
        return SpectralRadar.sameFunctionNameAsInAPI(~Same argument names as API~)
'''

def initDevice():
    SpectralRadar.initDevice.restype = DeviceHandle
    return SpectralRadar.initDevice()


def initProbe(Dev,ProbeFile):
    SpectralRadar.initProbe.restype = ProbeHandle
    SpectralRadar.initProbe.argtypes = [DeviceHandle, C.c_char_p]
    return SpectralRadar.initProbe(Dev,ProbeFile)


def createProcessingForDevice(Dev):
    SpectralRadar.createProcessingForDevice.argtypes = [DeviceHandle]
    SpectralRadar.createProcessingForDevice.restype = [ProcessingHandle]
    return SpectralRadar.createProcessingForDevice(Dev)

def createBScanPattern(Probe,Range,AScans,apodization):
    SpectralRadar.createBScanPattern.restype = ScanPatternHandle
    SpectralRadar.createBScanPattern.argtypes = [ProbeHandle,C.c_double,C.c_int,BOOL]
    return SpectralRadar.createBScanPattern(Probe,Range,AScans,apodization)

def createRawData():
    SpectralRadar.createRawData.restypes = RawDataHandle
    return SpectralRadar.createRawData()

def getRawData(Dev,RawData):
    SpectralRadar.getRawData.argtypes = [DeviceHandle,RawDataHandle]
    SpectralRadar.getRawData.restype = RawDataHandle
    return SpectralRadar.getRawData(Dev,RawData)

def getRawDataEx(Dev,RawData,CameraIdx):
    SpectralRadar.getRawDataEx.argtypes = [DeviceHandle,RawDataHandle,C.c_int]
    SpectralRadar.getRawData.restype = RawDataHandle
    return SpectralRadar.getRawDataEx(Dev,RawData,CameraIdx)

def startMeasurement(Dev,Pattern,Type): #Note: lowercase 'type' in C API, which is reserved in Python
    SpectralRadar.startMeasurement.argtypes = [DeviceHandle,ScanPatternHandle,AcquisitionType]
    return SpectralRadar.startMeasurement(Dev,Pattern,Type)

def stopMeasurement(Dev):
    SpectralRadar.stopMeasurement.argtypes = [DeviceHandle]
    return SpectralRadar.stopMeasurement(Dev)

'''
Steps for recreation of demo :

initialize device (handle)

initialize processing routine (handle)

initialize probe (handle)

create raw data object (no handle)

set a processing flag (enum)

set an acquisition type (enum)

set processing output (handle)

create a scan pattern (handle)

start the measurement(function)

get raw data (function)

'''
