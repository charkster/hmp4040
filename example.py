#Here is an example usage (it will read all unique settings into a list, reset the instrument and then program the unique settings back into the instrument):

import time
import pyvisa
from hmp4040 import hmp4040

rm = pyvisa.ResourceManager()
hmp4040_ps = rm.open_resource('ASRL6::INSTR')
hmp4040 = hmp4040(pyvisa_instr=hmp4040_ps)

current_setting_list = hmp4040.get_unique_scpi_list()

hmp4040_ps.write('*RST')
time.sleep(2)
for scpi_cmd in current_setting_list:
  hmp4040_ps.write(scpi_cmd)
time.sleep(2)
