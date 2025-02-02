import unittest

import hcl2

from checkov.terraform.checks.resource.azure.SQLServerAuditPolicyRetentionPeriod import check
from checkov.common.models.enums import CheckResult


class TestSQLServerAuditingEnabled(unittest.TestCase):

    def test_failure(self):
        hcl_res = hcl2.loads("""
resource "azurerm_mssql_database_extended_auditing_policy" "example" {
  database_id                             = azurerm_mssql_database.examplea.id
  storage_endpoint                        = azurerm_storage_account.examplea.primary_blob_endpoint
  storage_account_access_key              = azurerm_storage_account.examplea.primary_access_key
  storage_account_access_key_is_secondary = false
  retention_in_days                       = 89
}
               """)
        resource_conf = hcl_res['resource'][0]['azurerm_mssql_database_extended_auditing_policy']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)
 
    def test_missingisfailure(self):
        hcl_res = hcl2.loads("""
resource "azurerm_mssql_database_extended_auditing_policy" "example" {
  database_id                             = azurerm_mssql_database.examplea.id
  storage_endpoint                        = azurerm_storage_account.examplea.primary_blob_endpoint
  storage_account_access_key              = azurerm_storage_account.examplea.primary_access_key
  storage_account_access_key_is_secondary = false
}
               """)
        resource_conf = hcl_res['resource'][0]['azurerm_mssql_database_extended_auditing_policy']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        hcl_res = hcl2.loads("""
            resource "azurerm_mssql_database_extended_auditing_policy" "example" {
  database_id                             = azurerm_mssql_database.examplea.id
  storage_endpoint                        = azurerm_storage_account.examplea.primary_blob_endpoint
  storage_account_access_key              = azurerm_storage_account.examplea.primary_access_key
  storage_account_access_key_is_secondary = false
  retention_in_days                       = 90
}
                """)
        resource_conf = hcl_res['resource'][0]['azurerm_mssql_database_extended_auditing_policy']['example']
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()
