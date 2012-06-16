
###############################################################################
#
# DescribeDBSnapshot
# Returns information about DB Snapshots.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeDBSnapshot(Choreography):

    """
    Create a new instance of the DescribeDBSnapshot Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DescribeDBSnapshot')


    def new_input_set(self):
        return DescribeDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return DescribeDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeDBSnapshotChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeDBSnapshot
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeDBSnapshotInputSet(InputSet):
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
        Set the value of the DBInstanceIdentifier input for this choreography. ((optional, string) The DB Instance identifier. Should be in all lowercase.)
        """
        def set_DBInstanceIdentifier(self, value):
            InputSet._set_input(self, 'DBInstanceIdentifier', value)

        """
        Set the value of the DBSnapshotIdentifier input for this choreography. ((optional, string) The unique identifier for the db snapshot you're retrieving information for.)
        """
        def set_DBSnapshotIdentifier(self, value):
            InputSet._set_input(self, 'DBSnapshotIdentifier', value)

        """
        Set the value of the MaxRecords input for this choreography. ((optional, integer) The max number of results to return in the response. Defaults to 100. Minimum is 20.)
        """
        def set_MaxRecords(self, value):
            InputSet._set_input(self, 'MaxRecords', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeDBSnapshot choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeDBSnapshotResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeDBSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeDBSnapshotResultSet(response, path)
