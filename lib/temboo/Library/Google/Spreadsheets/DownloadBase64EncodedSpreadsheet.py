
###############################################################################
#
# DownloadBase64EncodedSpreadsheet
# Downloads a document with the title you specify, and returns the content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DownloadBase64EncodedSpreadsheet(Choreography):

    """
    Create a new instance of the DownloadBase64EncodedSpreadsheet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/DownloadBase64EncodedSpreadsheet')


    def new_input_set(self):
        return DownloadBase64EncodedSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedSpreadsheetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedSpreadsheet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DownloadBase64EncodedSpreadsheetInputSet(InputSet):
        """
        Set the value of the Format input for this choreography. ((optional, string) The format you want to export the spreadsheet to, such as "txt" or "pdf". The default download format is "txt".)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Link input for this choreography. ((conditional, string) Enter the source links for the document to be retrieved. Required if Title is not specified.)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((conditional, string) The title of the document to download. Required if the source Link is not specifed.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedSpreadsheet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DownloadBase64EncodedSpreadsheetResultSet(ResultSet):
        """
        Retrieve the value for the "FileContents" output from this choreography execution. ((string) The Base64 encoded file content of the downloaded file.)
        """
        def get_FileContents(self):
            return self._output.get('FileContents', None)

class DownloadBase64EncodedSpreadsheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedSpreadsheetResultSet(response, path)
