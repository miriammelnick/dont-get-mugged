
###############################################################################
#
# CreateDeployment
# Create a Rightscale Deployment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateDeployment(Choreography):

    """
    Create a new instance of the CreateDeployment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/CreateDeployment')


    def new_input_set(self):
        return CreateDeploymentInputSet()

    def _make_result_set(self, result, path):
        return CreateDeploymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDeploymentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateDeployment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateDeploymentInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((integer) Enter a Rightscale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the DeploymentDefaultEC2AvailabilityZone input for this choreography. ((optional, string) Enter the default EC2 availability zone for this deployment.)
        """
        def set_DeploymentDefaultEC2AvailabilityZone(self, value):
            InputSet._set_input(self, 'DeploymentDefaultEC2AvailabilityZone', value)

        """
        Set the value of the DeploymentDefaultVPCSubnetHref input for this choreography. ((optional, string) Enter the href of the vpc subnet.)
        """
        def set_DeploymentDefaultVPCSubnetHref(self, value):
            InputSet._set_input(self, 'DeploymentDefaultVPCSubnetHref', value)

        """
        Set the value of the DeploymentDescription input for this choreography. ((optional, string)  Describe the deployment being created.)
        """
        def set_DeploymentDescription(self, value):
            InputSet._set_input(self, 'DeploymentDescription', value)

        """
        Set the value of the DeploymentNickname input for this choreography. ((string) Enter the nickname of the deployment being created.)
        """
        def set_DeploymentNickname(self, value):
            InputSet._set_input(self, 'DeploymentNickname', value)

        """
        Set the value of the Password input for this choreography. ((string) Enter a Rightscale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) Enter a Rightscale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateDeployment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateDeploymentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateDeploymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDeploymentResultSet(response, path)
