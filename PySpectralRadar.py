# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:18:32 2019
Python wrapper for Thorlabs SpectralRadar SDK
@author: sstucker
Version 0.0.3
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

class Device_CameraPreset(CEnum):

    Device_CameraPreset_Default = 0
    Device_CameraPreset_1 = 1
    Device_CameraPreset_2 = 2
    Device_CameraPreset_3 = 3
    Device_CameraPreset_4 = 4

#Wrapper functions ------------------------------------------------------------

"""
These are of the following format:
    SpectralRadar.sameFunctionNameAsInAPI.argtypes = [~argument type(s) if applicable~]
    SpectralRadar.sameFunctionNameAsInAPI.restype = [~return type if applicable~]
    def sameFunctionNameAsInAPI(~Same argument names as API~):
        return SpectralRadar.sameFunctionNameAsInAPI(~Same argument names as API~)
"""

SpectralRadar.initDevice.restype = OCTDeviceHandle
def initDevice():
    return SpectralRadar.initDevice()

SpectralRadar.initProbe.argtypes = [OCTDeviceHandle, C.c_char_p]
SpectralRadar.initProbe.restype = ProbeHandle
def initProbe(Dev,ProbeFile):
    ProbeFile = C.c_char_p(ProbeFile.encode('utf-8'))
    return SpectralRadar.initProbe(Dev,ProbeFile)

SpectralRadar.createProcessingForDevice.restype = ProcessingHandle
SpectralRadar.createProcessingForDevice.argtypes = [OCTDeviceHandle]
def createProcessingForDevice(Dev):
    return SpectralRadar.createProcessingForDevice(Dev)

SpectralRadar.setProcessingOutput.argtypes = [ProcessingHandle,DataHandle]
def setProcessingOutput(Proc,Spectrum):
    return SpectralRadar.setProcessingOutput(Proc,Spectrum)

SpectralRadar.setComplexDataOutput.argtypes = [ProcessingHandle,ComplexDataHandle]
def setComplexDataOutput(Proc,Complex):
    return SpectralRadar.setComplexDataOutput(Proc,Complex)

SpectralRadar.executeProcessing(Proc,RawData)
SpectralRadar.executeProcessing.argtypes = [ProcessingHandle,RawDataHandle]
def executeProcessing(Proc,RawData):
    return SpectralRadar.executeProcessing(Proc,RawData)

SpectralRadar.createNoScanPattern.restype = ScanPatternHandle
SpectralRadar.createNoScanPattern.argtypes = [ProbeHandle,C.c_int,C.c_int]
def createNoScanPattern(Probe,Scans,NumberOfScans):
    return SpectralRadar.createNoScanPattern(Probe,Scans,NumberOfScans)

SpectralRadar.createBScanPattern.argtypes = [ProbeHandle,C.c_double,C.c_int,BOOL]
SpectralRadar.createBScanPattern.restype = ScanPatternHandle
def createBScanPattern(Probe,Range,AScans,apodization):
    return SpectralRadar.createBScanPattern(Probe,Range,AScans,apodization)

SpectralRadar.createFreeformScanPattern.argtypes = [ProbeHandle,ndpointer(dtype=np.float32,ndim=1,flags='C_CONTIGUOUS'),C.c_int,C.c_int,BOOL]
SpectralRadar.createFreeformScanPattern.restype = ScanPatternHandle
def createFreeformScanPattern(Probe,positions,size_x,size_y,apodization):
    """
    Positions must be a numpy.float32 array of dimension 1, and must have
    length equal to 2 * size_x * size_y. Size_x is the number of points in the
    pattern repeated size_y times, but the positions array is taken as-is.
    """
    if positions.size == 2*size_x*size_y:
        return SpectralRadar.createFreeformScanPattern(Probe,positions,size_x,size_y,apodization)
    else:
        print('PySpectralRadar: WARNING! Scan pattern not created!')

SpectralRadar.rotateScanPattern.argtypes = [ScanPatternHandle,C.c_double]
def rotateScanPattern(Pattern,Angle):
    """
    Changes coordinates of scanPatternHandle by angle in radians.
    """
    return SpectralRadar.rotateScanPattern(Pattern,Angle)

SpectralRadar.createVolumePattern.restype = ScanPatternHandle
SpectralRadar.createVolumePattern.argtypes = [ProbeHandle,C.c_double,C.c_int,C.c_double,C.c_int]
def createVolumePattern(Probe,RangeX,SizeX,RangeY,SizeY):
    return SpectralRadar.createVolumePattern(Probe,RangeX,SizeX,RangeY,SizeY)

SpectralRadar.getWavelengthAtPixel.restype = C.c_double
SpectralRadar.getWavelengthAtPixel.argtypes = [OCTDeviceHandle,C.c_int]
def getWavelengthAtPixel(Dev,Pixel):
    return SpectralRadar.getWavelengthAtPixel(Dev,Pixel)

SpectralRadar.getDevicePropertyFloat.restype = C.c_float
SpectralRadar.getDevicePropertyFloat.argtypes = [OCTDeviceHandle,DevicePropertyFloat]
def getDevicePropertyFloat(Dev,Selection):
    return SpectralRadar.getDevicePropertyFloat(Dev,Selection)

SpectralRadar.getScanPatternLUT.argtypes = [ScanPatternHandle,ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS'),ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')]
def getScanPatternLUT(Pattern,PosX,PosY):
    """
    Replaces PosX and PosY arrays with X and Y coordinates of scan pattern from
    scanner LUT.
    """
    SpectralRadar.getScanPatternLUT(Pattern,PosX,PosY)

SpectralRadar.createData.restype = DataHandle
def createData():
    return SpectralRadar.createData()

SpectralRadar.createRawData.restype = RawDataHandle
def createRawData():
    return SpectralRadar.createRawData()

SpectralRadar.createComplexData.restype = ComplexDataHandle
def createComplexData():
    return SpectralRadar.createComplexData()

SpectralRadar.getRawData.argtypes = [OCTDeviceHandle,RawDataHandle]
def getRawData(Dev,RawData):
    return SpectralRadar.getRawData(Dev,RawData)

SpectralRadar.appendRawData.argtypes = [RawDataHandle,RawDataHandle,Direction]
def appendRawData(Data,DataToAppend,Direction):
    return SpectralRadar.appendRawData(Data,DataToAppend,Direction)

SpectralRadar.getRawData.restype = RawDataHandle
SpectralRadar.getRawDataEx.argtypes = [OCTDeviceHandle,RawDataHandle,C.c_int]
def getRawDataEx(Dev,RawData,CameraIdx):
    return SpectralRadar.getRawDataEx(Dev,RawData,CameraIdx)

SpectralRadar.getComplexDataPropertyInt.argtypes = [ComplexDataHandle,DataPropertyInt]
def getComplexDataPropertyInt(Data,Selection):
    return SpectralRadar.getComplexDataPropertyInt(Data,Selection)

SpectralRadar.getDataPropertyInt.argtypes = [DataHandle,DataPropertyInt]
SpectralRadar.getDataPropertyInt.restype = C.c_int
def getDataPropertyInt(Data,Selection):
    return SpectralRadar.getDataPropertyInt(Data,Selection)

SpectralRadar.getRawDataPropertyInt.argtypes = [RawDataHandle,RawDataPropertyInt]
SpectralRadar.getRawDataPropertyInt.restype = C.c_int
def getRawDataPropertyInt(RawData,Selection):
    return SpectralRadar.getRawDataPropertyInt(RawData,Selection)

SpectralRadar.startMeasurement.argtypes = [OCTDeviceHandle,ScanPatternHandle,AcquisitionType]
def startMeasurement(Dev,Pattern,Type): #Note: named lowercase 'type' in C, which is reserved in Python
    return SpectralRadar.startMeasurement(Dev,Pattern,Type)

SpectralRadar.stopMeasurement.argtypes = [OCTDeviceHandle]
def stopMeasurement(Dev):
    return SpectralRadar.stopMeasurement(Dev)

SpectralRadar.closeDevice.argtypes = [OCTDeviceHandle]
def closeDevice(Dev):
    return SpectralRadar.closeDevice(Dev)

SpectralRadar.closeProcessing.argtypes = [ProcessingHandle]
def closeProcessing(Proc):
    return SpectralRadar.closeProcessing(Proc)

SpectralRadar.clearData.argtypes = [DataHandle]
def clearData(Data):
    return SpectralRadar.clearData(Data)

SpectralRadar.clearRawData.argtypes = [RawDataHandle]
def clearRawData(RawData):
    return SpectralRadar.clearRawData(RawData)

SpectralRadar.clearComplexData.argtypes = [ComplexDataHandle]
def clearComplexData(ComplexData):
    return SpectralRadar.clearComplexData(ComplexData)

SpectralRadar.setProcessingFlag.argtypes = [ProcessingHandle,ProcessingFlag,BOOL]
def setProcessingFlag(Proc,Flag,Value):
    return SpectralRadar.setProcessingFlag(Proc,Flag,Value)

SpectralRadar.setProbeParameterInt.argtypes = [ProbeHandle,ProbeParameterInt,C.c_int]
def setProbeParameterInt(Probe,Selection,Value):
    return SpectralRadar.setProbeParameterInt(Probe,Selection,Value)

SpectralRadar.setCameraPreset.argtypes = [OCTDeviceHandle,ProbeHandle,ProcessingHandle,C.c_int]
def setCameraPreset(Dev,Probe,Proc,Preset):
    return SpectralRadar.setCameraPreset(Dev,Probe,Proc,Preset)

SpectralRadar.setTriggerMode.argtypes = [OCTDeviceHandle,Device_TriggerType]
def setTriggerMode(Dev,TriggerMode):
    return SpectralRadar.setTriggerMode(Dev,TriggerMode)

SpectralRadar.setTriggerTimeoutSec.argtypes = [OCTDeviceHandle,C.c_int]
def setTriggerTimeoutSec(Dev,Timeout):
    return SpectralRadar.setTriggerTimeoutSec(Dev,Timeout)

SpectralRadar.createMemoryBuffer.restype = BufferHandle
def createMemoryBuffer():
    return SpectralRadar.createMemoryBuffer()

SpectralRadar.appendToBuffer.argtypes = [BufferHandle,DataHandle,ColoredDataHandle]
def appendToBuffer(Buffer,Data,ColoredData):
    return SpectralRadar.appendToBuffer(Buffer,Data,ColoredData)

SpectralRadar.clearBuffer.argtypes = [BufferHandle]
def clearBuffer(Buffer):
    return SpectralRadar.clearBuffer(Buffer)

SpectralRadar.exportRawData.argtypes = [RawDataHandle,RawDataExportFormat,C.c_wchar_p]
def exportRawData(Raw,Format,Path):
    return SpectralRadar.exportRawData(Raw,Format,Path)

SpectralRadar.exportComplexData.argtypes = [ComplexDataHandle,ComplexDataExportFormat,C.c_wchar_p]
def exportComplexData(ComplexData,Format,Path):
    return SpectralRadar.exportComplexData(ComplexData,Format,Path)

SpectralRadar.exportData1D.argtypes = [DataHandle,Data1DExportFormat,C.c_wchar_p]
def exportData1D(Data,Format,Path):
    return SpectralRadar.exportData1D(Data,Format,Path)

SpectralRadar.exportData2D.argtypes = [DataHandle,Data2DExportFormat,C.c_wchar_p]
def exportData2D(Data,Format,Path):
    return SpectralRadar.exportData2D(Data,Format,Path)

SpectralRadar.exportData3D.argtypes = [DataHandle,Data3DExportFormat,C.c_wchar_p]
def exportData3D(Data,Format,Path):
    return SpectralRadar.exportData3D(Data,Format,Path)

SpectralRadar.clearScanPattern.argtypes = [ScanPatternHandle]
def clearScanPattern(Pattern):
    return SpectralRadar.clearScanPattern(Pattern)

SpectralRadar.closeProcessing.argtypes = [ProcessingHandle]
def closeProcessing(Proc):
    return SpectralRadar.closeProcessing(Proc)

SpectralRadar.closeDevice.argtypes = [OCTDeviceHandle]
def closeDevice(Dev):
    return SpectralRadar.closeDevice(Dev)

SpectralRadar.closeProbe.argtypes = [ProbeHandle]
def closeProbe(Probe):
    return SpectralRadar.closeProbe(Probe)

def copyComplexDataContent(ComplexDataSource,DataContent):
    """
    Copies complex processed data out of the ComplexDataSource and into the
    numpy object DataContent, which uses PySpectralRadar ctypes structure
    ComplexFloat to hold two 16 bit floats in fields 'real' and 'imag'
    Note: usurps copyComplexDataContent in the wrapper namespace. If you would
    like to move the data to a raw pointer rather than a numpy array, take care
    to call the original function.
    """
    SpectralRadar.copyComplexDataContent.argtypes = [ComplexDataHandle,ndpointer(dtype=np.complex64,ndim=3,flags='C_CONTIGUOUS')]
    return SpectralRadar.copyComplexDataContent(ComplexDataSource,DataContent)

def copyRawDataContent(RawDataSource,DataContent):
    """
    Copies raw data out of the RawDataSource and into the numpy
    object DataContent. DataContent MUST match the dimensions of the
    RawDataSource (use getRawDataPropertyInt and be of type numpy.uint16)
    Note: usurps copyRawDataContent in the wrapper namespace. If you would
    like to move the data to a raw pointer rather than a numpy array, take care
    to call the original function.
    """
    SpectralRadar.copyRawDataContent.argtypes = [RawDataHandle,ndpointer(dtype=np.uint16,ndim=3,flags='C_CONTIGUOUS')]
    SpectralRadar.copyRawDataContent(RawDataSource,DataContent)

def getRawDataShape(rawDataHandle):
    """
    :param rawDataHandle: SpectralRadar raw data handle object
    :return: 3D shape of raw data
    """
    prop = RawDataPropertyInt
    rawSize1 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size1)
    rawSize2 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size2)
    rawSize3 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size3)

    return np.array([rawSize1,rawSize2,rawSize3])
