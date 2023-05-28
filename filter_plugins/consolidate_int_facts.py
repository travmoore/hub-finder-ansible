# Older version of the consolidation module. To be removed upon further testing of _exempt module.
class FilterModule(object):
    def consolidate_int_facts(self, int_pow, int_cdp, int_stat, int_mac):
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

            parsed_interface.append(x)


        return(parsed_interface)

    def filters(self):
        return({'consolidate_int_facts': self.consolidate_int_facts})