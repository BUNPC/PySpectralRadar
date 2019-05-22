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

class CEnum(IntEnum):
    """
    A ctypes-compatible IntEnum superclass. Thanks Chris Krycho
    www.chriskrycho.com/2015/ctypes-structures-and-dll-exports
    """
    @classmethod
    def from_param(cls, obj):
        return int(obj)


class AcquisitionType(CEnum):

    Acquisition_AsyncContinuous = 0
    Acquisition_AsyncFinite = 1
    Acquisition_Sync = 2

class ProcessingFlag(CEnum):

		Processing_UseOffsetErrors = 0
		Processing_RemoveDCSpectrum = 1
		Processing_RemoveAdvancedDCSpectrum = 2
		Processing_UseApodization = 3
		Processing_UseScanForApodization = 4
		Processing_UseUndersamplingFilter = 5
		Processing_UseDispersionCompensation = 6
		Processing_UseDechirp = 7
		Processing_UseExtendedAdjust = 8
		Processing_FullRangeOutput = 9
		Processing_FilterDC = 10
		Processing_UseAutocorrCompensation = 11
		Processing_UseDEFR = 12
		Processing_OnlyWindowing = 13
		Processing_RemoveFixedPattern = 14

class ProbeParameterInt(CEnum):

        Probe_ApodizationCycles = 0
        Probe_Oversampling = 1
        Probe_WhiteBalanceAutomatic = 2
        Probe_Oversampling_SlowAxis = 3
        Probe_SpeckleReduction = 4
        Probe_MaxScanRangeShape = 5

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

def startMeasurement(Dev,Pattern,Type): #Note: named lowercase 'type' in C, which is reserved in Python
    SpectralRadar.startMeasurement.argtypes = [DeviceHandle,ScanPatternHandle,AcquisitionType]
    return SpectralRadar.startMeasurement(Dev,Pattern,Type)

def stopMeasurement(Dev):
    SpectralRadar.stopMeasurement.argtypes = [DeviceHandle]
    return SpectralRadar.stopMeasurement(Dev)

def setProcessingFlag(Proc,Flag,Value):
    SpectralRadar.setProcessingFlag.argtypes = [ProcessingHandle,ProcessingFlag,BOOL]
    return SpectralRadar.setProcessingFlag(Proc,Flag,Value)

def setProbeParameterInt(Probe,Selection,Value):
    SpectralRadar.setProbeParameterInt.argtypes = [ProbeHandle,ProbeParameterInt,C.c_int]


probeName = 'ProbeLKM10'

# Testing ----------------------------------------------------------------------

from time import Sleep

print('Attempting to initialize device...')
device = initDevice() #Will crash kernel if not connected to DAQ
sleep(2)

print('Attempting to create processing routine for device...')
proc = createProcessingForDevice(dev)
sleep(2)

print('Attempting to create probe for device...')
probe = initProbe(device,probeName)
sleep(2)

print('Attempting to create raw data instance')
raw = createRawData()
sleep(2)

print('Attempting to assign acquisition type...')
acquisitionType = AcquisitionType()
sleep(2)
