from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class VirtualMachineMemoryHotEnabled(BaseResourceCheck):
    def __init__(self):
        name = "Make sure hot adding memory is enabled"
        id = "CKV_VSP_4"
        supported_resources = ['vsphere_virtual_machine']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'memory_hot_add_enabled' in conf.keys():
            self.evaluated_keys = 'memory_hot_add_enabled'
            if conf['memory_hot_add_enabled'] == [True] and conf['memory_hot_add_enabled']:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = VirtualMachineMemoryHotEnabled()
