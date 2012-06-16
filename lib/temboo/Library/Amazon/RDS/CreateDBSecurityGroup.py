
###############################################################################
#
# CreateDBSecurityGroup
# Creates a new database security group which you can use to control the access to the database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateDBSecurityGroup(Choreography):

    """
    Create a new instance of the CreateDBSecurityGroup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/CreateDBSecurityGroup')


    def new_input_set(self):
        return CreateDBSecurityGroupInputSet()

    def _make_result_set(self, result, path):
        return CreateDBSecurityGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBSecurityGroupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateDBSecurityGroup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateDBSecurityGroupInputSet(InputSet):
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
        Set the value of the DBSecurityGroupDescription input for this choreography. ((required, string) A description for the security group you're creating.)
        """
        def set_DBSecurityGroupDescription(self, value):
            InputSet._set_input(self, 'DBSecurityGroupDescription', value)

        """
        Set the value of the DBSecurityGroupName input for this choreography. ((required, string) A unique name for the security group you want to create.)
        """
        def set_DBSecurityGroupName(self, value):
            InputSet._set_input(self, 'DBSecurityGroupName', value)


"""
A ResultSet with methods tailored to the values returned by the CreateDBSecurityGroup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateDBSecurityGroupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateDBSecurityGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDBSecurityGroupResultSet(response, path)
