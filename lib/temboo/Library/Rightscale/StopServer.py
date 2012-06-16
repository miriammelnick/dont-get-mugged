
###############################################################################
#
# StopServer
# Stop a Rightscale server instance. Optionally, this Choreo can also poll the stop process and verify server termination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StopServer(Choreography):

    """
    Create a new instance of the StopServer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/StopServer')


    def new_input_set(self):
        return StopServerInputSet()

    def _make_result_set(self, result, path):
        return StopServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StopServerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StopServer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StopServerInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((integer) Enter your Rightscale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the Password input for this choreography. ((string) Enter a Rightscale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PollingTimeLimit input for this choreography. ((optional, integer) Specify a time limit - in minutes - for the duration of the server state polling.)
        """
        def set_PollingTimeLimit(self, value):
            InputSet._set_input(self, 'PollingTimeLimit', value)

        """
        Set the value of the ServerID input for this choreography. ((integer) Enter the Rightscale Server ID that is to be stopped.)
        """
        def set_ServerID(self, value):
            InputSet._set_input(self, 'ServerID', value)

        """
        Set the value of the Username input for this choreography. ((string) Enter a Rightscale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the StopServer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StopServerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "State" output from this choreography execution. ((string) The server 'state' parsed from the Rightscale response.)
        """
        def get_State(self):
            return self._output.get('State', None)

class StopServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StopServerResultSet(response, path)
