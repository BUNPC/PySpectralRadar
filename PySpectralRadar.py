# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:18:32 2019

Python wrapper for Thorlabs SpectralRadar SDK

@author: sstucker

"""
import ctypes as C
from enum import IntEnum
import numpy as np
from numpy.ctypeslib import ndpointer

#Imports SpectralRadar libraries. Thorlabs software must be installed on machine
SpectralRadar = C.CDLL('SpectralRadar')

# Wrapper typedefs ------------------------------------------------------------

class BOOL(C.c_int):
    pass

FALSE = BOOL(0)
TRUE = BOOL(1)

class ComplexFloat(C.Structure):
    _fields_=(("real",C.c_float),("imag",C.c_float))

# Pointer typedefs ------------------------------------------------------------

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

OCTDeviceHandle = C.POINTER(DeviceStruct)

class ScanPatternStruct(C.Structure):
    pass

ScanPatternHandle = C.POINTER(ScanPatternStruct)

class ProcessingStruct(C.Structure):
    pass

ProcessingHandle = C.POINTER(ProcessingStruct)

class ProbeStruct(C.Structure):
    pass

ProbeHandle = C.POINTER(ProbeStruct)

class BufferStruct(C.Structure):
    pass

BufferHandle = C.POINTER(BufferStruct)

class ColoredDataStruct(C.Structure):
    pass

ColoredDataHandle = C.POINTER(ColoredDataStruct)

# Enum typedefs ---------------------------------------------------------------

class CEnum(IntEnum):
    """
    A ctypes-compatible IntEnum superclass. Thanks Chris Krycho
    www.chriskrycho.com/2015/ctypes-structures-and-dll-exports
    """
    @classmethod
    def from_param(cls, obj):
        return int(obj)

class DevicePropertyFloat(CEnum):

    Device_FullWellCapacity = 0
    Device_zSpacing = 1
    Device_zRange = 2
    Device_SignalAmplitudeMin_dB = 3
    Device_SignalAmplitudeLow_dB = 4
    Device_SignalAmplitudeHigh_dB = 5
    Device_SignalAmplitudeMax_dB = 6
    Device_BinToElectronScaling = 7
    Device_Temperature = 8
    Device_SLD_OnTime_sec = 9
    Device_CenterWavelength_nm = 10
    Device_SpectralWidth_nm = 11
    Device_MaxTriggerFrequency_Hz = 12

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

class Data1DExportFormat(CEnum):

    Data1DExport_RAW = 0
    Data1DExport_TXT = 1
    Data1DExport_CSV = 2
    Data1DExport_TableTXT = 3
    Data1DExport_Fits = 4

class Data2DExportFormat(CEnum):

	Data2DExport_SRM = 0
	Data2DExport_RAW = 1
	Data2DExport_TXT = 2
	Data2DExport_CSV = 3
	Data2DExport_TableTXT = 4
	Data2DExport_Fits = 5

class Data3DExportFormat(CEnum):

	Data3DExport_SRM = 0
	Data3DExport_RAW = 1
	Data3DExport_TXT = 2
	Data3DExport_CSV = 3
	Data3DExport_VFF = 4
	Data3DExport_VTK = 5
	Data3DExport_Fits = 6
	Data3DExport_TIFF = 7

class ComplexDataExportFormat(CEnum):

    ComplexDataExport_RAW = 0

class RawDataExportFormat(CEnum):

	RawDataExport_RAW = 0
	RawDataExport_SRR = 1

class direction(CEnum):

    Direction_1 = 0
    Direction_2 = 1
    Direction_3 = 2

class Device_TriggerType(CEnum):

    Trigger_FreeRunning = 0
    Trigger_TrigBoard_ExternalStart = 1
    Trigger_External_AScan = 2

#Wrapper functions ------------------------------------------------------------

'''

These are of the following format:

    def sameFunctionNameAsInAPI(~Same argument names as API~):
        SpectralRadar.sameFunctionNameAsInAPI.argtypes = [~argument type(s) if applicable~]
        SpectralRadar.sameFunctionNameAsInAPI.restype = [~return type if applicable~]
        return SpectralRadar.sameFunctionNameAsInAPI(~Same argument names as API~)

'''

def initDevice():
    SpectralRadar.initDevice.restype = OCTDeviceHandle
    return SpectralRadar.initDevice()

def initProbe(Dev,ProbeFile):
    ProbeFile = C.c_char_p(ProbeFile.encode('utf-8'))
    SpectralRadar.initProbe.argtypes = [OCTDeviceHandle, C.c_char_p]
    SpectralRadar.initProbe.restype = ProbeHandle
    return SpectralRadar.initProbe(Dev,ProbeFile)

def createProcessingForDevice(Dev):
    SpectralRadar.createProcessingForDevice.argtypes = [OCTDeviceHandle]
    SpectralRadar.createProcessingForDevice.restype = ProcessingHandle
    return SpectralRadar.createProcessingForDevice(Dev)

def setProcessingOutput(Proc,Spectrum):
    SpectralRadar.setProcessingOutput.argtypes = [ProcessingHandle,DataHandle]
    return SpectralRadar.setProcessingOutput(Proc,Spectrum)

def setComplexDataOutput(Proc,Complex):
    SpectralRadar.setComplexDataOutput.argtypes = [ProcessingHandle,ComplexDataHandle]
    return SpectralRadar.setComplexDataOutput(Proc,Complex)

def executeProcessing(Proc,RawData):
    SpectralRadar.executeProcessing.argtypes = [ProcessingHandle,RawDataHandle]
    SpectralRadar.executeProcessing(Proc,RawData)
    return SpectralRadar.executeProcessing(Proc,RawData)

def createNoScanPattern(Probe,Scans,NumberOfScans):
    SpectralRadar.createNoScanPattern.argtypes = [ProbeHandle,C.c_int,C.c_int]
    SpectralRadar.createNoScanPattern.restype = ScanPatternHandle
    return SpectralRadar.createNoScanPattern(Probe,Scans,NumberOfScans)

def createBScanPattern(Probe,Range,AScans,apodization):
    SpectralRadar.createBScanPattern.argtypes = [ProbeHandle,C.c_double,C.c_int,BOOL]
    SpectralRadar.createBScanPattern.restype = ScanPatternHandle
    return SpectralRadar.createBScanPattern(Probe,Range,AScans,apodization)

def createFreeformScanPattern(Probe,positions,size_x,size_y,apodization):
    '''
    Positions must be a numpy.float32 array of dimension 1, and must have
    length equal to 2 * size_x * size_y. Size_x is the number of points in the
    pattern repeated size_y times, but the positions array is taken as-is.
    '''
    if positions.size == 2*size_x*size_y:
        SpectralRadar.createFreeformScanPattern.argtypes = [ProbeHandle,ndpointer(dtype=np.float32,ndim=1,flags='C_CONTIGUOUS'),C.c_int,C.c_int,BOOL]
        SpectralRadar.createFreeformScanPattern.restype = ScanPatternHandle
        return SpectralRadar.createFreeformScanPattern(Probe,positions,size_x,size_y,apodization)
    else:
        print('PySpectralRadar: WARNING! Scan pattern not created!')

def rotateScanPattern(Pattern,Angle):
    SpectralRadar.rotateScanPattern.argtypes = [ScanPatternHandle,C.c_double]
    return SpectralRadar.rotateScanPattern(Pattern,Angle)

def createVolumePattern(Probe,RangeX,SizeX,RangeY,SizeY):
    SpectralRadar.createVolumePattern.argtypes = [ProbeHandle,C.c_double,C.c_int,C.c_double,C.c_int]
    SpectralRadar.createVolumePattern.restype = ScanPatternHandle
    return SpectralRadar.createVolumePattern(Probe,RangeX,SizeX,RangeY,SizeY)

def getWavelengthAtPixel(Dev,Pixel):
    SpectralRadar.getWavelengthAtPixel.argtypes = [OCTDeviceHandle,C.c_int]
    SpectralRadar.getWavelengthAtPixel.restype = C.c_double
    return SpectralRadar.getWavelengthAtPixel(Dev,Pixel)

def getDevicePropertyFloat(Dev,Selection):
    SpectralRadar.getDevicePropertyFloat.argtypes = [OCTDeviceHandle,DevicePropertyFloat]
    SpectralRadar.getDevicePropertyFloat.restype = C.c_float
    return SpectralRadar.getDevicePropertyFloat(Dev,Selection)

def getScanPatternLUT(Pattern,PosX,PosY):
    '''
    Replaces PosX and PosY arrays with X and Y coordinates of scan pattern from
    scanner LUT.
    '''
    SpectralRadar.getScanPatternLUT.argtypes = [ScanPatternHandle,ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS'),ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')]
    SpectralRadar.getScanPatternLUT(Pattern,PosX,PosY)

def createData():
    SpectralRadar.createData.restype = DataHandle
    return SpectralRadar.createData()

def createRawData():
    SpectralRadar.createRawData.restype = RawDataHandle
    return SpectralRadar.createRawData()

def createComplexData():
    SpectralRadar.createComplexData.restype = ComplexDataHandle
    return SpectralRadar.createComplexData()

def getRawData(Dev,RawData):
    SpectralRadar.getRawData.argtypes = [OCTDeviceHandle,RawDataHandle]
    return SpectralRadar.getRawData(Dev,RawData)

def appendRawData(Data,DataToAppend,Direction):
    SpectralRadar.appendRawData.argtypes = [RawDataHandle,RawDataHandle,Direction]
    return SpectralRadar.appendRawData(Data,DataToAppend,Direction)

def getRawDataEx(Dev,RawData,CameraIdx):
    SpectralRadar.getRawDataEx.argtypes = [OCTDeviceHandle,RawDataHandle,C.c_int]
    SpectralRadar.getRawData.restype = RawDataHandle
    return SpectralRadar.getRawDataEx(Dev,RawData,CameraIdx)

def getComplexDataPropertyInt(Data,Selection):
    SpectralRadar.getComplexDataPropertyInt.argtypes = [ComplexDataHandle,DataPropertyInt]
    return SpectralRadar.getComplexDataPropertyInt(Data,Selection)

def getDataPropertyInt(Data,Selection):
    SpectralRadar.getDataPropertyInt.argtypes = [DataHandle,DataPropertyInt]
    SpectralRadar.getDataPropertyInt.restype = C.c_int
    return SpectralRadar.getDataPropertyInt(Data,Selection)

def getRawDataPropertyInt(RawData,Selection):
    SpectralRadar.getRawDataPropertyInt.argtypes = [RawDataHandle,RawDataPropertyInt]
    SpectralRadar.getRawDataPropertyInt.restype = C.c_int
    return SpectralRadar.getRawDataPropertyInt(RawData,Selection)

def startMeasurement(Dev,Pattern,Type): #Note: named lowercase 'type' in C, which is reserved in Python
    SpectralRadar.startMeasurement.argtypes = [OCTDeviceHandle,ScanPatternHandle,AcquisitionType]
    return SpectralRadar.startMeasurement(Dev,Pattern,Type)

def stopMeasurement(Dev):
    SpectralRadar.stopMeasurement.argtypes = [OCTDeviceHandle]
    return SpectralRadar.stopMeasurement(Dev)

def closeDevice(Dev):
    SpectralRadar.closeDevice.argtypes = [OCTDeviceHandle]
    return SpectralRadar.closeDevice(Dev)

def closeProcessing(Proc):
    SpectralRadar.closeProcessing.argtypes = [ProcessingHandle]
    return SpectralRadar.closeProcessing(Proc)

def clearData(Data):
    SpectralRadar.clearData.argtypes = [DataHandle]
    return SpectralRadar.clearData(Data)

def clearRawData(RawData):
    SpectralRadar.clearRawData.argtypes = [RawDataHandle]
    return SpectralRadar.clearRawData(RawData)

def clearComplexData(ComplexData):
    SpectralRadar.clearComplexData.argtypes = [ComplexDataHandle]
    return SpectralRadar.clearComplexData(ComplexData)

def setProcessingFlag(Proc,Flag,Value):
    SpectralRadar.setProcessingFlag.argtypes = [ProcessingHandle,ProcessingFlag,BOOL]
    return SpectralRadar.setProcessingFlag(Proc,Flag,Value)

def setProbeParameterInt(Probe,Selection,Value):
    SpectralRadar.setProbeParameterInt.argtypes = [ProbeHandle,ProbeParameterInt,C.c_int]
    return SpectralRadar.setProbeParameterInt(Probe,Selection,Value)

def setCameraPreset(Dev,Probe,Proc,Preset):
    SpectralRadar.setCameraPreset.argtypes = [OCTDeviceHandle,ProbeHandle,ProcessingHandle,C.c_int]
    return SpectralRadar.setCameraPreset(Dev,Probe,Proc,Preset)

def setTriggerMode(Dev,TriggerMode):
    SpectralRadar.setTriggerMode.argtypes = [OCTDeviceHandle,Device_TriggerType]
    return SpectralRadar.setTriggerMode(Dev,TriggerMode)

def setTriggerTimeoutSec(Dev,Timeout):
    SpectralRadar.setTriggerTimeoutSec.argtypes = [OCTDeviceHandle,C.c_int]
    return SpectralRadar.setTriggerTimeoutSec(Dev,Timeout)

def createMemoryBuffer():
    SpectralRadar.createMemoryBuffer.restype = BufferHandle
    return SpectralRadar.createMemoryBuffer()

def appendToBuffer(Buffer,Data,ColoredData):
    SpectralRadar.appendToBuffer.argtypes = [BufferHandle,DataHandle,ColoredDataHandle]
    return SpectralRadar.appendToBuffer(Buffer,Data,ColoredData)

def clearBuffer(Buffer):
    SpectralRadar.clearBuffer.argtypes = [BufferHandle]
    return SpectralRadar.clearBuffer(Buffer)

def exportRawData(Raw,Format,Path):
    SpectralRadar.exportRawData.argtypes = [RawDataHandle,RawDataExportFormat,C.c_wchar_p]
    return SpectralRadar.exportRawData(Raw,Format,Path)

def exportComplexData(ComplexData,Format,Path):
    SpectralRadar.exportComplexData.argtypes = [ComplexDataHandle,ComplexDataExportFormat,C.c_wchar_p]
    return SpectralRadar.exportComplexData(ComplexData,Format,Path)

def exportData1D(Data,Format,Path):
    SpectralRadar.exportData1D.argtypes = [DataHandle,Data1DExportFormat,C.c_wchar_p]
    return SpectralRadar.exportData1D(Data,Format,Path)

def exportData2D(Data,Format,Path):
    SpectralRadar.exportData2D.argtypes = [DataHandle,Data2DExportFormat,C.c_wchar_p]
    return SpectralRadar.exportData2D(Data,Format,Path)

def exportData3D(Data,Format,Path):
    SpectralRadar.exportData3D.argtypes = [DataHandle,Data3DExportFormat,C.c_wchar_p]
    return SpectralRadar.exportData3D(Data,Format,Path)

def clearScanPattern(Pattern):
    SpectralRadar.clearScanPattern.argtypes = [ScanPatternHandle]
    return SpectralRadar.clearScanPattern(Pattern)

def closeProcessing(Proc):
    SpectralRadar.closeProcessing.argtypes = [ProcessingHandle]
    return SpectralRadar.closeProcessing(Proc)

def closeDevice(Dev):
    SpectralRadar.closeDevice.argtypes = [OCTDeviceHandle]
    return SpectralRadar.closeDevice(Dev)

def closeProbe(Probe):
    SpectralRadar.closeProbe.argtypes = [ProbeHandle]
    return SpectralRadar.closeProbe(Probe)

def copyComplexDataContent(ComplexDataSource,DataContent):
    '''
    Copies complex processed data out of the ComplexDataSource and into the
    numpy object DataContent, which uses PySpectralRadar ctypes structure
    ComplexFloat to hold two 16 bit floats in fields 'real' and 'imag'

    Note: usurps copyComplexDataContent in the wrapper namespace. If you would
    like to move the data to a raw pointer rather than a numpy array, take care
    to call the original function.
    '''
    SpectralRadar.copyComplexDataContent.argtypes = [ComplexDataHandle,ndpointer(dtype=np.complex64,ndim=3,flags='C_CONTIGUOUS')]
    return SpectralRadar.copyComplexDataContent(ComplexDataSource,DataContent)

def copyRawDataContent(RawDataSource,DataContent):
    '''
    Copies raw data out of the RawDataSource and into the numpy
    object DataContent. DataContent MUST match the dimensions of the
    RawDataSource (use getRawDataPropertyInt and be of type numpy.uint16)

    Note: usurps copyRawDataContent in the wrapper namespace. If you would
    like to move the data to a raw pointer rather than a numpy array, take care
    to call the original function.
    '''
    SpectralRadar.copyRawDataContent.argtypes = [RawDataHandle,ndpointer(dtype=np.uint16,ndim=3,flags='C_CONTIGUOUS')]
    SpectralRadar.copyRawDataContent(RawDataSource,DataContent)
