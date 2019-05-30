# -*- coding: utf-8 -*-

import sys
from PySpectralRadar import *

print('PySpectralRadar Demo')

#path = ###('Folder-level save path for data: ')

###('Press ENTER to initiate device handle...')

dev = initDevice()

###('Press ENTER to set device parameters...')

triggerType = Device_TriggerType
setTriggerMode(dev,triggerType.Trigger_FreeRunning)
setTriggerTimeoutSec(dev,5)

print('Set trigger mode to free running, timeout = 5 s')

###('Press ENTER to initiate probe handle...')

probe = initProbe(dev,'ProbeLKM10-LV')

###('Press ENTER to initiate processing handle...')

proc = createProcessingForDevice(dev)

setCameraPreset(dev,probe,proc,0)
print('Set camera preset = 0')

###('Press ENTER to initiate acquisition...')

scanPattern = createNoScanPattern(probe,100,512)
print('Created scan pattern.')

measurementType = AcquisitionType
startMeasurement(dev,scanPattern,measurementType.Acquisition_AsyncContinuous)
rawDataHandle = createRawData()
complexDataHandle = createComplexData()
print('Started measurement. Created data objects.')

getRawData(dev,rawDataHandle)
setComplexDataOutput(proc,complexDataHandle)
executeProcessing(proc,rawDataHandle)

stopMeasurement(dev)
print('Stopped measurement.')

complexExportFormat = ComplexDataExportFormat
rawExportFormat = RawDataExportFormat
debugPathComplex = C.c_wchar_p("C:/Users/OCT/PySpectralRadar/demo_complexdata.raw")
debugPathRAW = C.c_wchar_p("C:/Users/OCT/PySpectralRadar/demo_rawdata.raw")
exportComplexData(complexDataHandle,complexExportFormat.ComplexDataExport_RAW,debugPathComplex)
exportRawData(rawDataHandle,rawExportFormat.RawDataExport_RAW,debugPathRAW)
print('Exported data.')

clearScanPattern(scanPattern)
clearRawData(rawDataHandle)
clearComplexData(complexDataHandle)
closeProcessing(proc)
closeProbe(probe)
closeDevice(dev)
print('Cleared memory.')
