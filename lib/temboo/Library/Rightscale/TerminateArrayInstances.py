
###############################################################################
#
# TerminateArrayInstances
# Terminate an array instance.

#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TerminateArrayInstances(Choreography):

    """
    Create a new instance of the TerminateArrayInstances Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/TerminateArrayInstances')


    def new_input_set(self):
        return TerminateArrayInstancesInputSet()

    def _make_result_set(self, result, path):
        return TerminateArrayInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TerminateArrayInstancesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TerminateArrayInstances
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TerminateArrayInstancesInputSet(InputSet):
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
        Set the value of the ServerArrayID input for this choreography. ((integer) Enter the ID of a server array.)
        """
        def set_ServerArrayID(self, value):
            InputSet._set_input(self, 'ServerArrayID', value)

        """
        Set the value of the Username input for this choreography. ((string) Enter a Rightscale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the TerminateArrayInstances choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TerminateArrayInstancesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TerminateArrayInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TerminateArrayInstancesResultSet(response, path)
