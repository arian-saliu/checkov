from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck

class num_cpus(BaseResourceCheck):
    def __init__(self):
        name = "Upper limit for number of CPUs"
        id = "CKV_VSP_2"
        supported_resources = ['vsphere_virtual_machine']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'num_cpus' in conf.keys():
            self.evaluated_keys = 'num_cpus'
            if conf['num_cpus'] >= [5]:
                return CheckResult.FAILED
        return CheckResult.PASSED

check = num_cpus()