# This module will parse the data created by the facts consolidation module and create a per-switch compliance report
# for devices that likely have an unmanaged switch attached. It will also track exceptions and exemptions
class FilterModule(object):
    def int_comply(self,int_data):
        parsed_interfaces = {
            'compliant': {'list':[], 'count': 0},
            'non-compliant': {'list':[], 'count': 0},
            'network-exempt': {'list':[], 'count': 0},
            'user-exception': {'list':[], 'count': 0},
            'mac-summary': {'is_compliant': False, 'has_exceptions': False}
        }
        
        for i in int_data:
            if len(i['MAC_ADDRESS']) <= 1:
                parsed_interfaces['compliant']['list'].append(i['PORT'])
                parsed_interfaces['compliant']['count'] += 1
            elif len(i['MAC_ADDRESS']) >= 2:
                if len(i['MAC_ADDRESS']) == 2 and 'IP Phone' in i['DEVICE']:
                    parsed_interfaces['compliant']['list'].append(i['PORT'])
                    parsed_interfaces['compliant']['count'] += 1
                elif i['NETWORK-EXEMPT']:
                    parsed_interfaces['network-exempt']['list'].append(i['PORT'])
                    parsed_interfaces['network-exempt']['count'] += 1
                elif i['USER-EXCEPTION']:
                    parsed_interfaces['user-exception']['list'].append(i['PORT'])
                    parsed_interfaces['user-exception']['count'] += 1
                else:
                    parsed_interfaces['non-compliant']['list'].append(i['PORT'])
                    parsed_interfaces['non-compliant']['count'] += 1
            else:
                print('THERE WAS AN ERROR PARSING CONSOLIDATED INTERFACE DATA USING THE int_comply FILTER MODULE')

        if parsed_interfaces['non-compliant']['count'] == 0:
            parsed_interfaces['mac-summary']['is_compliant'] = True

        if parsed_interfaces['user-exception']['count'] >= 1:
            parsed_interfaces['mac-summary']['has_exceptions'] = True

        return(parsed_interfaces)

    def filters(self):
        return({'int_comply': self.int_comply})