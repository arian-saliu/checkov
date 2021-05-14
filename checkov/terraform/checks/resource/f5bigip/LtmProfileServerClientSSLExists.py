from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class LtmProfileServerClientSSLExists(BaseResourceCheck):
    def __init__(self):
        name = "Make sure hot adding cpu is enabled."
        id = "CKV_BIP_2"
        supported_resources = ['bigip_ltm_profile_server_ssl', 'bigip_ltm_profile_client_ssl']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    # WIP
    def scan_resource_conf(self, conf):
        if 'name' in conf.keys():
            self.evaluated_keys = 'name'
            if conf['name'] and conf['defaults_from'] and conf['partition']:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = LtmProfileServerClientSSLExists()
