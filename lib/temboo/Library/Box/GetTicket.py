
###############################################################################
#
# GetTicket
# Retrieves a ticket from Box.net that is used during authentication to obtain a permanent authorization token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTicket(Choreography):

    """
    Create a new instance of the GetTicket Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/GetTicket')


    def new_input_set(self):
        return GetTicketInputSet()

    def _make_result_set(self, result, path):
        return GetTicketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTicketChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTicket
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTicketInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetTicket choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTicketResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Ticket" output from this choreography execution. ((string) The authentication ticket retrieved from Box.net which is used in the authentication process for retrieving an auth token.)
        """
        def get_Ticket(self):
            return self._output.get('Ticket', None)

class GetTicketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTicketResultSet(response, path)
