
###############################################################################
#
# RetrieveSpreadsheets
# Retrieves a list of spreadsheets that exist in your Google account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveSpreadsheets(Choreography):

    """
    Create a new instance of the RetrieveSpreadsheets Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveSpreadsheets')


    def new_input_set(self):
        return RetrieveSpreadsheetsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSpreadsheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSpreadsheetsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveSpreadsheets
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveSpreadsheetsInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveSpreadsheets choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveSpreadsheetsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveSpreadsheetsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveSpreadsheetsResultSet(response, path)
