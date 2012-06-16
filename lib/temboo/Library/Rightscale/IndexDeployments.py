
###############################################################################
#
# IndexDeployments
# Retrieve a list of server assets grouped within a particular Rightscale Deployment. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class IndexDeployments(Choreography):

    """
    Create a new instance of the IndexDeployments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/IndexDeployments')


    def new_input_set(self):
        return IndexDeploymentsInputSet()

    def _make_result_set(self, result, path):
        return IndexDeploymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IndexDeploymentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the IndexDeployments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class IndexDeploymentsInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((string) Enter a Righscale Account ID)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the Filter input for this choreography. ((optional, string) Specify an attributeName=AttributeValue pair. For example: nickname=mynick; OR description<>mydesc)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

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
        Set the value of the inputFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the IndexDeployments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class IndexDeploymentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class IndexDeploymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return IndexDeploymentsResultSet(response, path)
