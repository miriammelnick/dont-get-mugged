
###############################################################################
#
# CreateSubaccount
# Create a Twilio subaccount.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateSubaccount(Choreography):

    """
    Create a new instance of the CreateSubaccount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/CreateSubaccount')


    def new_input_set(self):
        return CreateSubaccountInputSet()

    def _make_result_set(self, result, path):
        return CreateSubaccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSubaccountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateSubaccount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateSubaccountInputSet(InputSet):
        """
        Set the value of the AccountSID input for this choreography. ((conditional, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        def set_AccountSID(self, value):
            InputSet._set_input(self, 'AccountSID', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the FriendlyName input for this choreography. ((optional, string) Enter a name for the subaccount being created.)
        """
        def set_FriendlyName(self, value):
            InputSet._set_input(self, 'FriendlyName', value)


"""
A ResultSet with methods tailored to the values returned by the CreateSubaccount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateSubaccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twilio.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateSubaccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSubaccountResultSet(response, path)
