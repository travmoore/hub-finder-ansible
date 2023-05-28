# This module will build the final data model used to create the final report from jinja2 template.

class FilterModule(object):
    def report_builder(self, report_data):
        reportb = {'hub_total': 0,
                   'non_comp': [],
                   'compliant': []
                  }
        for host in report_data:
            if host['is_compliant'] == False:
                reportb['hub_total'] += host['hub_count']
                reportb['non_comp'].append(host)
            elif host['is_compliant'] == True:
                reportb['compliant'].append(host)
            
        return(reportb)

    def filters(self):
        return({'report_builder': self.report_builder})