
###############################################################################
#
# DownloadSpreadsheet
# Downloads a specified spreadsheet in a user's Zoho Sheet Account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DownloadSpreadsheet(Choreography):

    """
    Create a new instance of the DownloadSpreadsheet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/Sheet/DownloadSpreadsheet')


    def new_input_set(self):
        return DownloadSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return DownloadSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadSpreadsheetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DownloadSpreadsheet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DownloadSpreadsheetInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BookId input for this choreography. ((required, integer) Specifies the unique spreadsheet id to download.)
        """
        def set_BookId(self, value):
            InputSet._set_input(self, 'BookId', value)

        """
        Set the value of the DownloadFormat input for this choreography. ((required, string) Specifies the file format in which the documents need to be downloaded. Possible values for documents: xls, xlsx, ods, sxc, pdf, html, csv, tsv.)
        """
        def set_DownloadFormat(self, value):
            InputSet._set_input(self, 'DownloadFormat', value)

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
A ResultSet with methods tailored to the values returned by the DownloadSpreadsheet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DownloadSpreadsheetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Zoho. Corresponds to the DownloadFormat input.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DownloadSpreadsheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadSpreadsheetResultSet(response, path)
