
###############################################################################
#
# Login
# Retrieves a ticket number from Zoho.  If a previously generated ticket has expired, the Login Choreo will retrieve a new one.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Login(Choreography):

    """
    Create a new instance of the Login Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/Login')


    def new_input_set(self):
        return LoginInputSet()

    def _make_result_set(self, result, path):
        return LoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LoginChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Login
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LoginInputSet(InputSet):
        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Service input for this choreography. ((required, string) The service that is being accessed.)
        """
        def set_Service(self, value):
            InputSet._set_input(self, 'Service', value)


"""
A ResultSet with methods tailored to the values returned by the Login choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LoginResultSet(ResultSet):
        """
        Retrieve the value for the "TicketStatus" output from this choreography execution. ()
        """
        def get_TicketStatus(self):
            return self._output.get('TicketStatus', None)
        """
        Retrieve the value for the "Ticket" output from this choreography execution. ((string) Stores the ticket that is archived in the vault as well as all new tickets retrieved when expired tickets are detected.)
        """
        def get_Ticket(self):
            return self._output.get('Ticket', None)

class LoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LoginResultSet(response, path)
