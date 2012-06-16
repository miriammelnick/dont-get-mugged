
###############################################################################
#
# RestoreDBInstanceFromDBSnapshot
# Creates a new DB Instance from a DB snapshot.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RestoreDBInstanceFromDBSnapshot(Choreography):

    """
    Create a new instance of the RestoreDBInstanceFromDBSnapshot Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/RestoreDBInstanceFromDBSnapshot')


    def new_input_set(self):
        return RestoreDBInstanceFromDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return RestoreDBInstanceFromDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestoreDBInstanceFromDBSnapshotChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RestoreDBInstanceFromDBSnapshot
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RestoreDBInstanceFromDBSnapshotInputSet(InputSet):
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
        Set the value of the AutoMinorVersionUpgrade input for this choreography. ((optional, boolean) Indicates that minor version upgrades will be applied automatically to the DB Instance during the maintenance window. Defaults to 0 (false).)
        """
        def set_AutoMinorVersionUpgrade(self, value):
            InputSet._set_input(self, 'AutoMinorVersionUpgrade', value)

        """
        Set the value of the AvailabilityZone input for this choreography. ((optional, string) The EC2 Availability Zone that the database instance will be created in. A random one is chose if not provided. Can not be specified if the MultiAZ parameter is set to 1 (true).)
        """
        def set_AvailabilityZone(self, value):
            InputSet._set_input(self, 'AvailabilityZone', value)

        """
        Set the value of the DBInstanceClass input for this choreography. ((optional, string) The compute and memory capacity of the Amazon RDS DB instance. Valid Values: db.m1.small | db.m1.large | db.m1.xlarge | db.m2.2xlarge | db.m2.4xlarge.)
        """
        def set_DBInstanceClass(self, value):
            InputSet._set_input(self, 'DBInstanceClass', value)

        """
        Set the value of the DBInstanceIdentifier input for this choreography. ((required, string) The identifier for the new DB instance that will be created from the specified Snapshot.)
        """
        def set_DBInstanceIdentifier(self, value):
            InputSet._set_input(self, 'DBInstanceIdentifier', value)

        """
        Set the value of the DBName input for this choreography. ((optional, string) The database name for the restored DB Instance. Note that this parameter doesn't apply to the MySQL engine.)
        """
        def set_DBName(self, value):
            InputSet._set_input(self, 'DBName', value)

        """
        Set the value of the DBSnapshotIdentifier input for this choreography. ((required, string) The name of the DB Snapshot to use.)
        """
        def set_DBSnapshotIdentifier(self, value):
            InputSet._set_input(self, 'DBSnapshotIdentifier', value)

        """
        Set the value of the Engine input for this choreography. ((optional, string) The database engine to use for the new instance. Valid Values: MySQL | oracle-se1 | oracle-se | oracle-ee.)
        """
        def set_Engine(self, value):
            InputSet._set_input(self, 'Engine', value)

        """
        Set the value of the LicenseModel input for this choreography. ((optional, string) License model information for the restored DB Instance. Valid values: license-included | bring-your-own-license | general-public-license.)
        """
        def set_LicenseModel(self, value):
            InputSet._set_input(self, 'LicenseModel', value)

        """
        Set the value of the MultiAZ input for this choreography. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment. Do not specify the AvailabilityZone parameter if the MultiAZ parameter is set to 1 (true).)
        """
        def set_MultiAZ(self, value):
            InputSet._set_input(self, 'MultiAZ', value)

        """
        Set the value of the Port input for this choreography. ((optional, integer) The port number on which the database accepts connections.)
        """
        def set_Port(self, value):
            InputSet._set_input(self, 'Port', value)


"""
A ResultSet with methods tailored to the values returned by the RestoreDBInstanceFromDBSnapshot choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RestoreDBInstanceFromDBSnapshotResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RestoreDBInstanceFromDBSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RestoreDBInstanceFromDBSnapshotResultSet(response, path)
