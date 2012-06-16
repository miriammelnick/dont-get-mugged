
###############################################################################
#
# Upload
# Upload a file to RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Upload(Choreography):

    """
    Create a new instance of the Upload Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/Upload')


    def new_input_set(self):
        return UploadInputSet()

    def _make_result_set(self, result, path):
        return UploadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Upload
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64 encoded contents of the file you want to upload. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file you want to upload)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the Folder input for this choreography. ((optional, integer) The id of the folder you want to upload the file to)
        """
        def set_Folder(self, value):
            InputSet._set_input(self, 'Folder', value)

        """
        Set the value of the Login input for this choreography. ((required, string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the VaultFile input for this choreography. (The path to a file in your vault to upload. Required if FileContents input variable is not specified.)
        """


"""
A ResultSet with methods tailored to the values returned by the Upload choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare formatted in commas separated values.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadResultSet(response, path)
