
###############################################################################
#
# ShowDeploymentIndex
# Retrieve a list of server assets grouped within a particular Rightscale Deployment ID. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowDeploymentIndex(Choreography):

    """
    Create a new instance of the ShowDeploymentIndex Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/ShowDeploymentIndex')


    def new_input_set(self):
        return ShowDeploymentIndexInputSet()

    def _make_result_set(self, result, path):
        return ShowDeploymentIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowDeploymentIndexChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowDeploymentIndex
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowDeploymentIndexInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((string) Enter a Righscale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the DeploymentID input for this choreography. ((integer) Enter the DeploymentID to only list servers in this particular RightScale deployment.)
        """
        def set_DeploymentID(self, value):
            InputSet._set_input(self, 'DeploymentID', value)

        """
        Set the value of the Password input for this choreography. ((string) Enter a Rightscale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ServerSettings input for this choreography. ((optional, string) Enter true to display additional information about this Righscale deployment.)
        """
        def set_ServerSettings(self, value):
            InputSet._set_input(self, 'ServerSettings', value)

        """
        Set the value of the Username input for this choreography. ((string) Enter a Rightscale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ShowDeploymentIndex choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowDeploymentIndexResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowDeploymentIndexChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowDeploymentIndexResultSet(response, path)
