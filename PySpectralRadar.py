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

class DataPropertyInt(CEnum):

	Data_Dimensions = 0
	Data_Size1 = 1
	Data_Size2 = 2
	Data_Size3 = 3
	Data_NumberOfElements = 4
	Data_SizeInBytes = 5
	Data_BytesPerElement = 6

class RawDataPropertyInt(CEnum):

	RawData_Size1 = 0
	RawData_Size2 = 1
	RawData_Size3 = 2
	RawData_NumberOfElements = 3
	RawData_SizeInBytes = 4
	RawData_BytesPerElement = 5
	RawData_LostFrames = 6

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
    SpectralRadar.initProbe.argtypes = [DeviceHandle, C.c_char_p]
    SpectralRadar.initProbe.restype = ProbeHandle
    return SpectralRadar.initProbe(Dev,ProbeFile)

def createProcessingForDevice(Dev):
    SpectralRadar.createProcessingForDevice.argtypes = [DeviceHandle]
    SpectralRadar.createProcessingForDevice.restype = [ProcessingHandle]
    return SpectralRadar.createProcessingForDevice(Dev)

def setProcessingOutput(Proc,Spectrum):
    SpectralRadar.setProcessingOutput.argtypes = [ProcessingHandle,DataHandle]
    return SpectralRadar.setProcessingOutput(Proc,Spectrum)

def executeProcessing(Proc,RawData):
    SpectralRadar.executeProcessing.argtypes = [ProcessingHandle,RawDataHandle]
    SpectralRadar.executeProcessing(Proc,RawData)
    return SpectralRadar.executeProcessing(Proc,RawData)

def createBScanPattern(Probe,Range,AScans,apodization):
    SpectralRadar.createBScanPattern.argtypes = [ProbeHandle,C.c_double,C.c_int,BOOL]
    SpectralRadar.createBScanPattern.restype = ScanPatternHandle
    return SpectralRadar.createBScanPattern(Probe,Range,AScans,apodization)

def createData():
    SpectralRadar.createData.restype = DataHandle
    return SpectralRadar.createData()

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

def getDataPropertyInt(Data,Selection):
    SpectralRadar.getDataPropertyInt.argtypes = [DataHandle,DataPropertyInt]
    SpectralRadar.getDataPropertyInt.restype = C.c_int
    return SpectralRadar.getDataPropertyInt(Data,Selection)

def getRawDataPropertyInt(RawData,Selection):
    SpectralRadar.getDataPropertyInt.argtypes = [RawDataHandle,RawDataPropertyInt]
    SpectralRadar.getDataPropertyInt.restype = C.c_int
    return SpectralRadar.getDataPropertyInt(RawData,Selection)

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
    return SpectralRadar.setProbeParameterInt(Probe,Selection,Value)

def setCameraPreset(Dev,Probe,Proc,Preset):
    SpectralRadar.setCameraPreset.argtypes = [DeviceHandle,ProbeHandle,ProcessingHandle,C.c_int]
    return SpectralRadar.setCameraPreset(Dev,Probe,Proc,Preset)


#Rewrite. This is not useful
# def copyDataContent(DataSource,Destination):
#     SpectralRadar.copyDataContent.argtypes = [DataHandle,RETURNS float* !!!! UH OH]
#
#     SpectralRadarDemo.copyDataContent(DataSource,Destination)

# Bridge code ------------------------------------------------------------------

import numpy.ctypeslib.as_array


def make_nd_array(c_pointer, shape, dtype=np.float64, order='C', own_data=True):
    '''
    Uses buffer to convert from c_void_p type to a numpy array. Defaults to float64
    Thanks to wordy: https://stackoverflow.com/a/33837141/11540004
    '''
    arr_size = np.prod(shape[:]) * np.dtype(dtype).itemsize
    if sys.version_info.major >= 3:
        buf_from_mem = ctypes.pythonapi.PyMemoryView_FromMemory
        buf_from_mem.restype = ctypes.py_object
        buf_from_mem.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
        buffer = buf_from_mem(c_pointer, arr_size, 0x100)
    else:
        buf_from_mem = ctypes.pythonapi.PyBuffer_FromMemory
        buf_from_mem.restype = ctypes.py_object
        buffer = buf_from_mem(c_pointer, arr_size)
    arr = np.ndarray(tuple(shape[:]), dtype, buffer, order=order)
    if own_data and not arr.flags.owndata:
        return arr.copy()
    else:
        return arr

def DataToNumpyArray(Data):
    size0 = getDataPropertyInt(Data,0).value
    size1 = getDataPropertyInt(Data,1).value
    arrC = C.c_float*size0*size1
    SpectralRadar.copyDataContent.argtypes = [DataHandle,c_float*size0*size1]
    SpectralRadar.copyDataContent(Data,arrC)
    return as_array(arrC)

def RawDataToNumpyArray(RawData):
    size0 = getRawDataPropertyInt(RawData,0).value
    size1 = getRawDataPropertyInt(RawData,1).value
    arrC = C.c_float*size0*size1
    SpectralRadar.copyRawDataContent.argtypes = [RawDataHandle,c_float*size0*size1]
    SpectralRadar.copyRawDataContent(RawData,arrC)
    return as_array(arrC)



# Testing ----------------------------------------------------------------------

probeName = 'ProbeLKM10'

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
