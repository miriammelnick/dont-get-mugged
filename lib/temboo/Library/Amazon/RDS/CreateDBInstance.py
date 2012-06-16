
###############################################################################
#
# CreateDBInstance
# Creates a new database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateDBInstance(Choreography):

    """
    Create a new instance of the CreateDBInstance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/CreateDBInstance')


    def new_input_set(self):
        return CreateDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return CreateDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBInstanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateDBInstance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateDBInstanceInputSet(InputSet):
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
        Set the value of the AllocatedStorage input for this choreography. ((required, integer) Storage amount (in gigabytes) to be configured for the DB. Use 5 to 1024 for MySQL or 10 to 1024 for Oracle.)
        """
        def set_AllocatedStorage(self, value):
            InputSet._set_input(self, 'AllocatedStorage', value)

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
        Set the value of the DBName input for this choreography. ((required, string) For MySQL, this is the name of the db that is created on the instance. For Oracle, it refers to the SID.)
        """
        def set_DBName(self, value):
            InputSet._set_input(self, 'DBName', value)

        """
        Set the value of the Engine input for this choreography. ((required, string) The name of the database engine to use for the instance. Options are: MySQL, oracle-se1, oracle-se, and oracle-ee.)
        """
        def set_Engine(self, value):
            InputSet._set_input(self, 'Engine', value)

        """
        Set the value of the MasterUserPassword input for this choreography. ((required, string) The master password for the DB instance.)
        """
        def set_MasterUserPassword(self, value):
            InputSet._set_input(self, 'MasterUserPassword', value)

        """
        Set the value of the MasterUsername input for this choreography. ((required, string) The master username for the DB instance.)
        """
        def set_MasterUsername(self, value):
            InputSet._set_input(self, 'MasterUsername', value)


"""
A ResultSet with methods tailored to the values returned by the CreateDBInstance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateDBInstanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDBInstanceResultSet(response, path)
