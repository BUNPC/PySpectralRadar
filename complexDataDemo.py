# -*- coding: utf-8 -*-

import sys
from PySpectralRadar import *

print('PySpectralRadar Demo')

path = input('Folder-level save path for data: ')

input('Press ENTER to initiate device handle...')

dev = initDevice()

input('Press ENTER to set device parameters...')

triggerType = Device_TriggerType
setTriggerMode(dev,triggerType.Trigger_FreeRunning)
setTriggerTimeoutSec(dev,5)

print('Set trigger mode to free running, timeout = 5 s')

input('Press ENTER to initiate probe handle...')

probe = initProbe(dev,'ProbeLKM10-LV')

input('Press ENTER to initiate processing handle...')

proc = createProcessingForDevice(dev)

setCameraPreset(dev,probe,proc,0)
print('Set camera preset = 0')

input('Press ENTER to initiate acquisition...')

scanPattern = createNoScanPattern(probe,100,1000)
print('Created non-scanning pattern. NumberOfScans = 1000')

measurementType = AcquisitionType
startMeasurement(dev,scanPattern,measurementType.Acquisition_AsyncContinuous)
rawDataHandle = createRawData()
complexDataHandle = createComplexData()
print('Started measurement. Created data objects.')

rawDataHandle = getRawData(dev,rawDataHandle)
setComplexDataOutput(proc,complexDataHandle)
executeProcessing(proc,rawDataHandle)

stopMeasurement(dev)
print('Stopped measurement.')

complexExportFormat = ComplexDataExportFormat
rawExportFormat = RawDataExportFormat
debugPathComplex = 'C:/Users/sstucker/OneDrive/Documents/BOAS_OCT_motion_corr/demo_complexdata.raw'
debugPathRAW = 'C:/Users/sstucker/OneDrive/Documents/BOAS_OCT_motion_corr/demo_rawdata.raw'
exportComplexData(complexDataHandle,complexExportFormat.ComplexDataExport_RAW,debugPath)
exportRawData(rawDataHandle,rawExportFormat.RawDataExport_RAW,debugPathRAW)
print('Exported data.')

clearScanPattern(scanPattern)
clearRawData(rawDataHandle)
clearComplexData(complexDataHandle)
closeProcessing(proc)
closeProbe(probe)
closeDevice(dev)
print('Cleared memory.')


