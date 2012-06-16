
###############################################################################
#
# ModifyDBInstance
# Modify settings for a DB Instance. You can change one or more database configuration parameters by specifying values for the Choreo inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ModifyDBInstance(Choreography):

    """
    Create a new instance of the ModifyDBInstance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/ModifyDBInstance')


    def new_input_set(self):
        return ModifyDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return ModifyDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ModifyDBInstanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ModifyDBInstance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ModifyDBInstanceInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the AllocatedStorage input for this choreography. ((required, integer) Storage amount (in gigabytes) to be configured for the DB. Use 5 to 1024 for MySQL or 10 to 1024 for Oracle. Value supplied must be at least 10% greater than the current value)
        """
        def set_AllocatedStorage(self, value):
            InputSet._set_input(self, 'AllocatedStorage', value)

        """
        Set the value of the AllowMajorVersionUpgrade input for this choreography. ((optional, boolean) Indicates that major version upgrades are allowed. Defaults to 0 (false).)
        """
        def set_AllowMajorVersionUpgrade(self, value):
            InputSet._set_input(self, 'AllowMajorVersionUpgrade', value)

        """
        Set the value of the ApplyImmediately input for this choreography. ((optional, boolean) Specifies whether or not the modifications applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB Instance. Defaults to 0 (false).)
        """
        def set_ApplyImmediately(self, value):
            InputSet._set_input(self, 'ApplyImmediately', value)

        """
        Set the value of the AutoMinorVersionUpgrade input for this choreography. ((optional, boolean) Indicates that minor version upgrades will be applied automatically to the DB Instance during the maintenance window. Defaults to 0 (false).)
        """
        def set_AutoMinorVersionUpgrade(self, value):
            InputSet._set_input(self, 'AutoMinorVersionUpgrade', value)

        """
        Set the value of the BackupRetentionPeriod input for this choreography. ((optional, integer) Number of days to retain automated backups. Setting to a positive number enables backups. Setting to 0 disables automated backups. Must be a value from 0 to 8. Defaults to 0 (disabled).)
        """
        def set_BackupRetentionPeriod(self, value):
            InputSet._set_input(self, 'BackupRetentionPeriod', value)

        """
        Set the value of the DBInstanceClass input for this choreography. ((required, string) Capacity for the DB instance.  (db.m1.small, db.m1.large, db.m1.xlarge, db.m2.xlarge, db.m2.2xlarge, or db.m2.4xlarge).)
        """
        def set_DBInstanceClass(self, value):
            InputSet._set_input(self, 'DBInstanceClass', value)

        """
        Set the value of the DBInstanceIdentifier input for this choreography. ((required, string) The DB Instance identifier. Should be in all lowercase.)
        """
        def set_DBInstanceIdentifier(self, value):
            InputSet._set_input(self, 'DBInstanceIdentifier', value)

        """
        Set the value of the DBParameterGroupName input for this choreography. ((optional, string) The name of the DB Parameter Group to apply to this DB Instance.)
        """
        def set_DBParameterGroupName(self, value):
            InputSet._set_input(self, 'DBParameterGroupName', value)

        """
        Set the value of the DBSecurityGroup input for this choreography. ((optional, string) A DB Security Groups to authorize on this DB Instance.)
        """
        def set_DBSecurityGroup(self, value):
            InputSet._set_input(self, 'DBSecurityGroup', value)

        """
        Set the value of the EngineVersion input for this choreography. ((optional, string) The version number of the database engine to upgrade to.)
        """
        def set_EngineVersion(self, value):
            InputSet._set_input(self, 'EngineVersion', value)

        """
        Set the value of the MasterUserPassword input for this choreography. ((required, string) The new password for the DB Instance master user.)
        """
        def set_MasterUserPassword(self, value):
            InputSet._set_input(self, 'MasterUserPassword', value)

        """
        Set the value of the MultiAZ input for this choreography. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment.)
        """
        def set_MultiAZ(self, value):
            InputSet._set_input(self, 'MultiAZ', value)

        """
        Set the value of the PreferredBackupWindow input for this choreography. ((optional, string) The daily time range during which automated backups are created. Format: hh24:mi-hh24:mi (in UTC). Must be at least 30 minutes. Can not conflict with PreferredMaintenanceWindow setting.)
        """
        def set_PreferredBackupWindow(self, value):
            InputSet._set_input(self, 'PreferredBackupWindow', value)

        """
        Set the value of the PreferredMaintenanceWindow input for this choreography. ((optional, string) The weekly time range (in UTC) during which system maintenance can occur, which may result in an outage. Format: ddd:hh24:mi-ddd:hh24:mi. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun.)
        """
        def set_PreferredMaintenanceWindow(self, value):
            InputSet._set_input(self, 'PreferredMaintenanceWindow', value)


"""
A ResultSet with methods tailored to the values returned by the ModifyDBInstance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ModifyDBInstanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ModifyDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ModifyDBInstanceResultSet(response, path)
