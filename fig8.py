# -*- coding: utf-8 -*-

import sys
import numpy as np

from PySpectralRadar import *

#-------------------------------------------------------------------------------

def generateFigureEightPositions(size,alinesPer8,rpt=1):
    '''
    Generates 1D list of positon pairs for use with SpectralRadar 3.X
    createFreeformScanPattern, which takes units of mm, therefore size argument
    is also in mm. By default, the figure-8 has height and width of 1 mm.
    '''
    if rpt > 0:
        t = np.linspace(0,2*np.pi,alinesPer8,dtype=np.float32)
        x = np.cos(t)
        y = np.sin(2*t)
        pos = np.empty(int(2*alinesPer8), dtype=np.float32)
        pos[0::2] = x
        pos[1::2] = y
        posRepeated = np.repeat(pos,rpt)
        return posRepeated.astype(np.float32)

#-------------------------------------------------------------------------------

print('\n----------------------------------')
print('PySpectralRadar Figure-8 Scanner')
print('----------------------------------\n')

###input('\nPress ENTER to initiate device handle...')

dev = initDevice()

###input('\nPress ENTER to set device parameters...')

triggerType = Device_TriggerType
setTriggerMode(dev,triggerType.Trigger_FreeRunning)
setTriggerTimeoutSec(dev,5)

print('\n----------------------------------')
print('Set trigger mode to free running, timeout = 5 s')
print('----------------------------------\n')

###input('\nPress ENTER to initiate probe handle...')

probe = initProbe(dev,'ProbeFigureEight')

###input('\nPress ENTER to initiate processing handle...')

proc = createProcessingForDevice(dev)

setCameraPreset(dev,probe,proc,0)
print('\n----------------------------------')
print('Set camera preset = 0')
print('----------------------------------\n')

###input('\nPress ENTER to initiate acquisition...')

FALSE = BOOL(0)
TRUE = BOOL(1)

ascans = 200
repeats = 400

fig8pos = generateFigureEightPositions(0.3,ascans,rpt=repeats)
print('\n----------------------------------')
print('Figure-8 Positions array:')
print(fig8pos)
print('Size:')
print(fig8pos.size)
print('----------------------------------\n')

scanPattern = createFreeformScanPattern(probe,fig8pos,ascans*repeats,1,FALSE)

print('\n----------------------------------')
print('Created scan pattern: 10X figure-8.')
print('----------------------------------\n')

acq = AcquisitionType
startMeasurement(dev,scanPattern,acq.Acquisition_AsyncContinuous)
rawDataHandle = createRawData()
print('\n----------------------------------')
print('Tried to start measurement. Created data objects.')
print('----------------------------------\n')

getRawData(dev,rawDataHandle)

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

print('\n----------------------------------')
print('Raw data:')
print(holder)
print('----------------------------------\n')

np.save('figure8Demo',holder)
print('\n----------------------------------')
print('Saved raw data array as .npy')
print('----------------------------------\n')

clearScanPattern(scanPattern)
clearRawData(rawDataHandle)
closeProcessing(proc)
closeProbe(probe)
closeDevice(dev)
print('\n----------------------------------')
print('Cleared objects from memory.')
print('----------------------------------')
