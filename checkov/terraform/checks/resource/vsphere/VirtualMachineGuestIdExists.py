from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class VirtualMachineGuestIdExists(BaseResourceCheck):
    def __init__(self):
        name = "Make sure that the Guest ID is defined."
        id = "CKV_VSP_5"
        supported_resources = ['vsphere_virtual_machine']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'guest_id' in conf.keys():
            self.evaluated_keys = 'guest_id'
            if conf['guest_id']:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = VirtualMachineGuestIdExists()
