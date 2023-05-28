# The purpose of the module is to take the data returned through the 'show cdp neighbor' textfsm template and remove the last 
# string character from the interface name so that it matches the output from other show commands
# Gig becomes Gi, Fas becomes Fa, Ten becomes Te
# This could be extended to support Port-Channel interfaces and other names but for my use case was not needed.
class FilterModule(object):
    def cdp_int_replace(self,cdp):
        parsed_cdp = []
        for i in cdp:
            if i['LOCAL_INTERFACE'].replace('g ', '').count(' ') == 0:
                i['LOCAL_INTERFACE'] = i['LOCAL_INTERFACE'].replace('g ', '')
                parsed_cdp.append(i)
            elif i['LOCAL_INTERFACE'].replace('s ', '').count(' ') == 0:
                i['LOCAL_INTERFACE'] = i['LOCAL_INTERFACE'].replace('s ', '')
                parsed_cdp.append(i)
            elif i['LOCAL_INTERFACE'].replace('n ', '').count(' ') == 0:
                i['LOCAL_INTERFACE'] = i['LOCAL_INTERFACE'].replace('n ', '')
                parsed_cdp.append(i)
            else:
                parsed_cdp.append(i)
                #pass
        return(parsed_cdp)

    def filters(self):
        return({'cdp_int_replace': self.cdp_int_replace})