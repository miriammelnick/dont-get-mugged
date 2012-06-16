
###############################################################################
#
# ShowServerIndex
# Display an index of all servers in a Rightscale account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowServerIndex(Choreography):

    """
    Create a new instance of the ShowServerIndex Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/ShowServerIndex')


    def new_input_set(self):
        return ShowServerIndexInputSet()

    def _make_result_set(self, result, path):
        return ShowServerIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowServerIndexChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowServerIndex
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowServerIndexInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((string) Enter a Righscale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

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
A ResultSet with methods tailored to the values returned by the ShowServerIndex choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowServerIndexResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowServerIndexChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowServerIndexResultSet(response, path)
