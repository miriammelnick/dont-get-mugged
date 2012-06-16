
###############################################################################
#
# DeleteDBSecurityGroup
# Deletes a specified database security group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteDBSecurityGroup(Choreography):

    """
    Create a new instance of the DeleteDBSecurityGroup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DeleteDBSecurityGroup')


    def new_input_set(self):
        return DeleteDBSecurityGroupInputSet()

    def _make_result_set(self, result, path):
        return DeleteDBSecurityGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDBSecurityGroupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteDBSecurityGroup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteDBSecurityGroupInputSet(InputSet):
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
        Set the value of the DBSecurityGroupName input for this choreography. ((required, string) The name for the security group you want to delete.)
        """
        def set_DBSecurityGroupName(self, value):
            InputSet._set_input(self, 'DBSecurityGroupName', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteDBSecurityGroup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteDBSecurityGroupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteDBSecurityGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDBSecurityGroupResultSet(response, path)
