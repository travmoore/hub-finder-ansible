# This module will take data collected from the 'show mac address-table' command and shorten the full interface name down to the first two letters
class FilterModule(object):
    def mac_port_shorten(self,mac_port):
        parsed_mac_port = []
        for i in mac_port:
            if i['DESTINATION_PORT'].startswith('GigabitEthernet'):
                i['DESTINATION_PORT'] = i['DESTINATION_PORT'].replace('gabitEthernet', '')
                parsed_mac_port.append(i)
            elif i['DESTINATION_PORT'].startswith('TenGigabitEthernet'):
                i['DESTINATION_PORT'] = i['DESTINATION_PORT'].replace('nGigabitEthernet', '')
                parsed_mac_port.append(i)
            elif i['DESTINATION_PORT'].startswith('FastEthernet'):
                i['DESTINATION_PORT'] = i['DESTINATION_PORT'].replace('stEthernet', '')
                parsed_mac_port.append(i)            
            elif i['DESTINATION_PORT'].startswith('Port-channel'):
                i['DESTINATION_PORT'] = i['DESTINATION_PORT'].replace('rt-channel', '')
                parsed_mac_port.append(i)            
            else:
                parsed_mac_port.append(i)
                #pass
        return(parsed_mac_port)

    def filters(self):
        return({'mac_port_shorten': self.mac_port_shorten})