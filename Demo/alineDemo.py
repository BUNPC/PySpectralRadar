# -*- coding: utf-8 -*-

import sys
import numpy as np

from PySpectralRadar import *

print('\n----------------------------------')
print('PySpectralRadar Demo')
print('----------------------------------\n')

input('\nPress ENTER to initiate device handle...')

dev = initDevice()

input('\nPress ENTER to set device parameters...')

triggerType = Device_TriggerType
setTriggerMode(dev,triggerType.Trigger_FreeRunning)
setTriggerTimeoutSec(dev,5)

print('\n----------------------------------')
print('Set trigger mode to free running, timeout = 5 s')
print('----------------------------------\n')

input('\nPress ENTER to initiate probe handle...')

probe = initProbe(dev,'ProbeLKM10-LV')

input('\nPress ENTER to initiate processing handle...')

proc = createProcessingForDevice(dev)

setCameraPreset(dev,probe,proc,0)
print('\n----------------------------------')
print('Set camera preset = 0')
print('----------------------------------\n')

input('\nPress ENTER to initiate acquisition...')

scanPattern = createNoScanPattern(probe,1,1024)
print('\n----------------------------------')
print('Created scan pattern: 1024 A-lines.')
print('----------------------------------\n')

measurementType = AcquisitionType
startMeasurement(dev,scanPattern,measurementType.Acquisition_AsyncContinuous)
rawDataHandle = createRawData()
complexDataHandle = createComplexData()
print('\n----------------------------------')
print('Started measurement. Created data objects.')
print('----------------------------------\n')


getRawData(dev,rawDataHandle)
setComplexDataOutput(proc,complexDataHandle)
executeProcessing(proc,rawDataHandle)

stopMeasurement(dev)
print('\n----------------------------------')
print('Stopped measurement.')
print('----------------------------------\n')


prop = RawDataPropertyInt
rawSize1 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size1)
rawSize2 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size2)
rawSize3 = getRawDataPropertyInt(rawDataHandle,prop.RawData_Size3)
rawNumberOfElements = getRawDataPropertyInt(rawDataHandle,prop.RawData_NumberOfElements)

rawDim = [rawSize1,rawSize2,rawSize3]

print('\n----------------------------------')
print('Raw data dimensions:')
print(rawDim)
print('Raw data number of elements:')
print(rawNumberOfElements)
print('----------------------------------\n')


holder = np.empty(rawDim,dtype=np.uint16)
copyRawDataContent(rawDataHandle,holder)
np.save('alineDemo',holder)
print('\n----------------------------------')
print('Saved raw data array as .npy')
print('----------------------------------\n')

clearScanPattern(scanPattern)
clearRawData(rawDataHandle)
clearComplexData(complexDataHandle)
closeProcessing(proc)
closeProbe(probe)
closeDevice(dev)
print('\n----------------------------------')
print('Cleared objects from memory.')
print('----------------------------------')
