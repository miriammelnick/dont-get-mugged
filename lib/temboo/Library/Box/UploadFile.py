
###############################################################################
#
# UploadFile
# Uploads files to your Box.net account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadFile(Choreography):

    """
    Create a new instance of the UploadFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/UploadFile')


    def new_input_set(self):
        return UploadFileInputSet()

    def _make_result_set(self, result, path):
        return UploadFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadFileInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64 encoded file contents of the file you want to upload. Required unless using the VaultFile alias (an advanced option available when executing Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the ContentType input for this choreography. ((required, string) The Content-Type of the file you're uploading (i.e. applcation/pdf, image/jpeg, text/plain, etc.).)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file to upload to Box.net.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the FolderID input for this choreography. ((optional, string) The ID of the target folder to upload the file to. Defaults to 0 which is the root folder.)
        """
        def set_FolderID(self, value):
            InputSet._set_input(self, 'FolderID', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadFileResultSet(response, path)
