
###############################################################################
#
# UploadDocument
# Uploads a document to your OfficeDrop account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadDocument(Choreography):

    """
    Create a new instance of the UploadDocument Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/UploadDocument')


    def new_input_set(self):
        return UploadDocumentInputSet()

    def _make_result_set(self, result, path):
        return UploadDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadDocumentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadDocument
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadDocumentInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The Base64-encoded file contents for the file you want to upload. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the ContentType input for this choreography. ((optional, string) The Content-Type of the file you are uploading. Defaults to text/plain.)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The filename to attach to the file being uploaded.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the FolderId input for this choreography. ((optional, integer) The ID of the folder to which you want to upload the file (if left empty, the file destination will be the root folder).)
        """
        def set_FolderId(self, value):
            InputSet._set_input(self, 'FolderId', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your OfficeDrop password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your OfficeDrop username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadDocument choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadDocumentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadDocumentResultSet(response, path)
