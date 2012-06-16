
###############################################################################
#
# CreateDBSnapshot
# Creates a snapshot of an existing database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateDBSnapshot(Choreography):

    """
    Create a new instance of the CreateDBSnapshot Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/CreateDBSnapshot')


    def new_input_set(self):
        return CreateDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return CreateDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBSnapshotChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateDBSnapshot
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateDBSnapshotInputSet(InputSet):
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
        Set the value of the DBInstanceIdentifier input for this choreography. ((required, string) The DB Instance identifier. Should be in all lowercase.)
        """
        def set_DBInstanceIdentifier(self, value):
            InputSet._set_input(self, 'DBInstanceIdentifier', value)

        """
        Set the value of the DBSnapshotIdentifier input for this choreography. ((required, string) The unique identifier for the db snapshot you're creating.)
        """
        def set_DBSnapshotIdentifier(self, value):
            InputSet._set_input(self, 'DBSnapshotIdentifier', value)


"""
A ResultSet with methods tailored to the values returned by the CreateDBSnapshot choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateDBSnapshotResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateDBSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDBSnapshotResultSet(response, path)
