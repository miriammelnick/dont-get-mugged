
###############################################################################
#
# DownloadBase64EncodedFile
# Retrieves the content of a specified file from your Box.net account, and returns it as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DownloadBase64EncodedFile(Choreography):

    """
    Create a new instance of the DownloadBase64EncodedFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/DownloadBase64EncodedFile')


    def new_input_set(self):
        return DownloadBase64EncodedFileInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DownloadBase64EncodedFileInputSet(InputSet):
        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The ID of the file to download from Box.net.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)


"""
A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DownloadBase64EncodedFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from Box.net. The response will contain the file content as Base64 encoded data.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DownloadBase64EncodedFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedFileResultSet(response, path)
