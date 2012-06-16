
###############################################################################
#
# RetrieveWorksheets
# Retrieves a list of worksheets in a given Google spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveWorksheets(Choreography):

    """
    Create a new instance of the RetrieveWorksheets Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveWorksheets')


    def new_input_set(self):
        return RetrieveWorksheetsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveWorksheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveWorksheetsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveWorksheets
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveWorksheetsInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((string) The unique for key for the spreadsheet associated with the worksheet(s) you want to retrieve. Can be retrieved from RetrieveSpreadsheets Choreo.)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveWorksheets choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveWorksheetsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveWorksheetsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveWorksheetsResultSet(response, path)
