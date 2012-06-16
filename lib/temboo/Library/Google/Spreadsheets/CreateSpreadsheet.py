
###############################################################################
#
# CreateSpreadsheet
# Creates a Google spreadsheet from a CSV file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateSpreadsheet(Choreography):

    """
    Create a new instance of the CreateSpreadsheet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/CreateSpreadsheet')


    def new_input_set(self):
        return CreateSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return CreateSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSpreadsheetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateSpreadsheet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateSpreadsheetInputSet(InputSet):
        """
        Set the value of the UploadFile input for this choreography. ((conditional, multiline) The data to be written to the Google spreadsheet. Should be in CSV format. This is required unless using the VaultCSVFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_UploadFile(self, value):
            InputSet._set_input(self, 'UploadFile', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The name of the new document.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VaultCSVFile input for this choreography. ((optional, vault file) The path to a CSV file stored in the vault. This is required unless you are using the UploadFile input variable. )
        """


"""
A ResultSet with methods tailored to the values returned by the CreateSpreadsheet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateSpreadsheetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Response from Google upload)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateSpreadsheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSpreadsheetResultSet(response, path)
