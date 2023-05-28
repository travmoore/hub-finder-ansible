# This module will consolidate all of the structured data taken from the other fsm templates and filter plugins and provide
# one uniform dictionary for each interface on every switch.
class FilterModule(object):
    def consolidate_int_facts_exempt(self, int_pow, int_cdp, int_stat, int_mac, interface_exemption):
        device_key = 'DEVICE'
        parsed_interface = []
        for x in int_stat:
            for c in int_cdp:
                if c['LOCAL_INTERFACE'] == x['PORT']:
                    x.update({'NEIGHBOR': c['NEIGHBOR']})

            for p in int_pow:
                if p['INTF'] == x['PORT']:
                    x.update({'DEVICE': p['DEVICE']})
            
            x.update({'MAC_ADDRESS': []})
            for mac in int_mac:
                if mac['DESTINATION_PORT'] == x['PORT'] and mac['DESTINATION_ADDRESS'] not in x['MAC_ADDRESS']:
                    x['MAC_ADDRESS'].append(mac['DESTINATION_ADDRESS'])

            x.update({'NETWORK-EXEMPT': False })
            x.update({'USER-EXCEPTION': False})
            for i in interface_exemption:
                if i['PORT'] == x['PORT']:
                    x['NETWORK-EXEMPT'] = i['NETWORK-EXEMPT']
                    x['USER-EXCEPTION'] = i['USER-EXCEPTION']
            
            if device_key not in x:
                x.update({'DEVICE': ''})
            

            parsed_interface.append(x)


        return(parsed_interface)

    def filters(self):
        return({'consolidate_int_facts_exempt': self.consolidate_int_facts_exempt})