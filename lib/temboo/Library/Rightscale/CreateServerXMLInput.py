
###############################################################################
#
# CreateServerXMLInput
# Creates a Rightscale server instance using a given XML template.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateServerXMLInput(Choreography):

    """
    Create a new instance of the CreateServerXMLInput Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Rightscale/CreateServerXMLInput')


    def new_input_set(self):
        return CreateServerXMLInputInputSet()

    def _make_result_set(self, result, path):
        return CreateServerXMLInputResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateServerXMLInputChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateServerXMLInput
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateServerXMLInputInputSet(InputSet):
        """
        Set the value of the ServerParameters input for this choreography. ((XML) An XML file containing the required parameters for the server creation. See documentation for XML schema.)
        """
        def set_ServerParameters(self, value):
            InputSet._set_input(self, 'ServerParameters', value)

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
        Set the value of the Username input for this choreography. ((string) Enter a Rightscale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateServerXMLInput choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateServerXMLInputResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ()
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateServerXMLInputChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateServerXMLInputResultSet(response, path)
