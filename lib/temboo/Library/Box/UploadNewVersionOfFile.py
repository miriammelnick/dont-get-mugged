
###############################################################################
#
# UploadNewVersionOfFile
# Uploads a new version of an existing file in a user’s account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadNewVersionOfFile(Choreography):

    """
    Create a new instance of the UploadNewVersionOfFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/UploadNewVersionOfFile')


    def new_input_set(self):
        return UploadNewVersionOfFileInputSet()

    def _make_result_set(self, result, path):
        return UploadNewVersionOfFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadNewVersionOfFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadNewVersionOfFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadNewVersionOfFileInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64 encoded file contents of the file you want to upload. Required unless using the VaultFile alias (an advanced option available when executing Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The APIKey provided by Box when registering for a developer account.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
        Set the value of the FileID input for this choreography. ((required, string) The unique id of the file that you want to update. This id is returned in various API calls such as GetAccountTree. It is also viewable in your browser's URL bar when viewing the doc at box.com.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file to upload to Box.net.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadNewVersionOfFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadNewVersionOfFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Box.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadNewVersionOfFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadNewVersionOfFileResultSet(response, path)
