
###############################################################################
#
# RetrieveSpreadsheetDetailsByName
# Retrieves spreadsheet and worksheet IDs with a given spreadsheet name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveSpreadsheetDetailsByName(Choreography):

    """
    Create a new instance of the RetrieveSpreadsheetDetailsByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveSpreadsheetDetailsByName')


    def new_input_set(self):
        return RetrieveSpreadsheetDetailsByNameInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSpreadsheetDetailsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSpreadsheetDetailsByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveSpreadsheetDetailsByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveSpreadsheetDetailsByNameInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SpreadsheetName input for this choreography. ((required, string) The title of the spreadsheet you want to retrieve details for.)
        """
        def set_SpreadsheetName(self, value):
            InputSet._set_input(self, 'SpreadsheetName', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveSpreadsheetDetailsByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveSpreadsheetDetailsByNameResultSet(ResultSet):
        """
        Retrieve the value for the "SpreadsheetDetails" output from this choreography execution. ((xml) The spreadsheet details including spreadsheet name and key. Worksheet names and IDs associated with the spreadsheet are also included.)
        """
        def get_SpreadsheetDetails(self):
            return self._output.get('SpreadsheetDetails', None)

class RetrieveSpreadsheetDetailsByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveSpreadsheetDetailsByNameResultSet(response, path)
