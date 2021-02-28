import time

class hmp4040():

    def __init__(self, pyvisa_instr):
        self.hmp4040 = pyvisa_instr # this is the pyvisa instrument, rm.open_resource('ASRL6::INSTR')
        self.channel_list = [1, 2, 3, 4]

    def get_inst_state(self):
        all_scpi_list = []
        for channel in self.channel_list:
            self.hmp4040.write('INSTrument:NSELect {0}'.format(channel))
            voltage          = float(self.hmp4040.query('SOURce:VOLTage?'))
            current_lim      = float(self.hmp4040.query('SOURce:CURRent?'))
            status           = int(self.hmp4040.query('OUTPut:STATe?'))
            current          = float(self.hmp4040.query('MEASure:CURRent?'))
            volt_prot        = float(self.hmp4040.query('VOLTage:PROTection?'))
            volt_prot_active = self.hmp4040.query('VOLTage:PROTection:MODE?').rstrip('\r\n')
            print "Channel %d voltage is %.02f V, overvoltage limit is %.02f overvolt config is %s, current limit is %.02f A, current is %.03f A status is %s" % (channel,voltage,volt_prot,volt_prot_active,current_lim,current,status)

    def get_channel_scpi_list(self, channel=1):
        result_list = []
        self.hmp4040.write('INSTrument:NSELect {0}'.format(channel))
        result_list.append('INSTrument:NSELect {0}'.format(channel))
        for command in self.cmd_dict:
            result = (self.hmp4040.query(command.format("?"))).rstrip('\r\n')
            result = " " + result
            result_list.append(command.format(result))
            time.sleep(0.1)
        return result_list

    def get_unique_scpi_list(self):
        unique_scpi_list = []
        unique_scpi_channel_list = []
        for channel in self.channel_list:
            channel_settings_list = self.get_channel_scpi_list(channel)
            found = 0
            unique_scpi_channel_list = []
            for setting in channel_settings_list:
                if (setting not in self.por_scpi_list):
                    found = 1
                    unique_scpi_channel_list.append(setting)
            if (found == 1):
                unique_scpi_list.append(channel_settings_list[0]) # this is the channel selection
                unique_scpi_list.extend(unique_scpi_channel_list)
        return unique_scpi_list


    select_cmd_dict = {
        "INSTrument:NSELect {0}": "Selects a channel by number" }

    activate_cmd_dict = {
        "OUTPut:GENeral {0}": "Enables the outputs for all activated channels",
        "OUTPut:SELect {0}": "Activites a selected channel" }

    cmd_dict = {
        "SOURce:VOLTage{0}"          : "Sets/Queries the voltage value of the selected channel",
        "SOURce:CURRent{0}"          : "Sets/Queries the current limit value of the selected channel",
        "VOLTage:PROTection:MODE{0}" : "Sets/Queries the voltage protection mode, measured or protected",
        "OUTPut:STATe{0}"            : "Activates and enables the output for a selected channel"
    }

    query_cmd_dict = {
        "MEASure:VOLTage?" : "Measures voltage of selected channel",
        "MEASure:CURRent?" : "Measures voltage of selected channel"
    }

    por_scpi_list = [
        'INSTrument:NSELect 1',
        'INSTrument:NSELect 2',
        'INSTrument:NSELect 3',
        'INSTrument:NSELect 4',
        'SOURce:CURRent 0.1000',
        'SOURce:VOLTage 0.000',
        'VOLTage:PROTection:MODE measured',
        'OUTPut:STATe 0' ]
